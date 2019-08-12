import datetime
import logging

from django.core.cache import cache
from django.db.models import Sum
from django.db import transaction

from Achievegoals import celery_app
from goals import weixin
from celery.task.schedules import crontab
from celery.decorators import periodic_task

from goals.models import Goal,Supervise,Acknowledgement,Wallet,TransactionRecord,Clock

#check goals and perferm some operations
@celery_app.task
def check_and_perferm(goal_id):
    logging.info("check whether the goal has finished")
    goal=Goal.objects.get(pk=goal_id)
    if goal.is_complete():
        logging.info("goal is finished")
        #for goal maker
        goal.goalStatus=2
        goal.save()
        user=goal.user
        user_openid=user.username
        nickname=goal.user.nickname
        template_id="nzA3m0pMBP9VNkyT16zuuEqt7ziX4OaxtCn6UA9dNBE"
        form_ids=cache.get(user_openid)
        if form_ids:
            form_id,num=form_ids[0]
        else:
            logging.error("user {} formId is ran out of".format(user_openid))
            return None
        supervises=goal.supervise.all().aggregate(sum_supMoney=Sum('supMoney'))
        data={
            "keyword1":
                {"value":goal.content},
            "keyword2":
                {"value":str(supervises['sum_supMoney'])}
        }
        logging.debug(data)
        with transaction.atomic():
            wallet=Wallet.objects.get(user=user)
            wallet.banlance+=goal.conMoney
            transactionrecord=TransactionRecord.objects.create(user=user,operateType='income',amount=goal.conMoney,
                                                     description=u'小信心金额返回',goal=goal,status='done')
            transactionrecord.save()
            wallet.banlance+=supervises['sum_supMoney']
            transactionrecord = TransactionRecord.objects.create(user=user, operateType='income', amount=supervises['sum_supMoney'],
                                                       description=u'目标完成奖励', goal=goal, status='done')
            transactionrecord.save()
            wallet.save()
        page="/pages/targeting/targeting?id="+str(goal_id)
        weixin.send_template_message(user_openid,template_id,form_id,data,page,emphasis_keyword="keyword2.DATA")

        num=num-1
        if num>0:
            form_ids[0]=(form_id,num)
            cache.set(user_openid,form_ids)
        else:
            form_ids.pop(0)
            cache.set(user_openid,form_ids)
        #for supervisor
        supervises=goal.supervise.all()
        for supervise in supervises:
            supervisor=supervise.supervisor
            logging.debug("info {}".format(supervisor))
            supervisor_openid=supervisor.username
            template_id="yQRz0IMFRvdsY1jIDW9n2mWD8OnQMuOluNdgvps6niE"
            supervisor_form_ids=cache.get(supervisor_openid)
            if supervisor_form_ids:
                supervisor_form_id,num=supervisor_form_ids[0]
            else:
                logging.error("user {} is ran out of".format(supervisor_openid))
                return None
            keyword1="{},{}已经完成目标".format(nickname,supervise.supervisor.nickname)
            keyword2=goal.content
            data={
                "keyword1":
                    {
                        "value":keyword1
                    },
                "keyword2":
                    {
                        "value":keyword2
                    }
            }
            page="/pages/targeting/targeting?id="+str(goal_id)
            weixin.send_template_message(supervisor_openid,template_id,supervisor_form_id,data,page)
            num=num-1
            if num>0:
                form_ids[0]=(supervisor_form_id,num)
                cache.set(supervisor_openid,form_ids)
            else:
                supervisor_form_ids.pop(0)
                cache.set(supervisor_openid,supervisor_form_ids)

@celery_app.task
def supervise_notification(supervise_id):
    logging.debug("supervise notification")
    supervise=Supervise.objects.get(pk=supervise_id)
    goal=supervise.goal
    openid=goal.user.username
    template_id="ERKpAOF8KhM7J9gv0o_BJGmEDXQmt8nUPNzUufQ6Uic"
    form_ids=cache.get(openid)
    if form_ids:
        form_id,num=form_ids[0]
    else:
        logging.error("user {} formId is ran out of".format(openid))
        return
    data={
        "keyword1":
            {"value":goal.content},
        "keyword2":
            {"value":supervise.supervisor.nickname},
        "keyword3":
            {"value":supervise.createdTime.strftime("%Y-%m-%d %H:%M:%S")}
    }
    #page="/pages/singleClock/singleClock?="+str(goal.id)
    page="/pages/index/index"
    weixin.send_template_message(openid, template_id, form_id, data, page)
    num = num - 1
    if num > 0:
        form_ids[0] = (form_id, num)
        cache.set(openid, form_ids)
    else:
        form_ids.pop(0)
        cache.set(openid, form_ids)

@celery_app.task
def acknowledge_notification(clock_id):
    logging.debug("clock ackownledge")
    clock=Clock.objects.get(pk=clock_id)
    goal=clock.goal
    supervises = goal.supervise.all()
    supervises_str=",".join(list(map(lambda supervise:supervise.supervisor.nickname,supervises)))
    for supervise in supervises:
        openid = supervise.supervisor.username
        form_ids = cache.get(openid)
        if form_ids:
            form_id, num = form_ids[0]
        else:
            logging.error("user {} formId is ran out of".format(openid))
            return
        template_id="TBUkZ-bMsNEQ63--dQ8m9sK0hu2qMiM7XXv1LF8xb2k"
        data={
            "keyword1":
                {"value":goal.content},
            "keyword2":
                {"value":goal.user.nickname},
            "keyword3":
                {"value":supervises_str}
        }
        page="/pages/singleClock/singleClock?id="+str(clock.id)
        weixin.send_template_message(openid, template_id, form_id, data, page)
        num = num - 1
        if num > 0:
            form_ids[0] = (form_id, num)
            cache.set(openid, form_ids)
        else:
            form_ids.pop(0)
            cache.set(openid, form_ids)

@celery_app.task
def notify_goal_maker(acknowledge_id):
    logging.debug("notify goal maker")
    acknowledgement=Acknowledgement.objects.get(pk=acknowledge_id)
    clock=acknowledgement.clock
    goal=clock.goal
    openid=goal.user.username
    template_id="kx90lIE5pHYnNzwC_rSrR1eOXH_I3l98zB1BXOk9Ac4"
    form_ids=cache.get(openid)
    if form_ids:
        form_id, num = form_ids[0]
    else:
        logging.error("user {} formId is ran out of".format(openid))
        return
    data={
        "keyword1":
            {"value":acknowledgement.supervisor.nickname},
        "keyword2":
            {"value":acknowledgement.acknowledgeTime.strftime("%Y-%m-%d %H:%M:%S")},
        "keyword3":
            {"value":goal.content}
    }
    page="/pages/singleClock/singleClock?id="+str(clock.id)
    weixin.send_template_message(openid, template_id, form_id, data, page)
    num = num - 1
    if num > 0:
        form_ids[0] = (form_id, num)
        cache.set(openid, form_ids)
    else:
        form_ids.pop(0)
        cache.set(openid, form_ids)


@periodic_task(run_every=crontab(minute=0,hour=3))
def clock_remind():
    logging.info("clock remind")
    goals=Goal.objects.filter(goalStatus=1)
    for goal in goals:
        openid=goal.user.username
        form_ids=cache.get(openid)
        if form_ids:
            form_id,num=form_ids[0]
        else:
            logging.error("user {} formId is ran out of".format(openid))
            continue
        template_id = "QPv0OUE8zkQggLawpxHDj6Tlr99qccMO4OiE1Qh8KKk"
        clock_num=goal.clock_num
        clocked_num=goal.clocks.all().count()
        progress="{}/{}".format(clocked_num,clock_num)
        data={
            "keyword1":
                {"value":goal.content},
            "keyword2":
                {"value":progress},
            "keyword3":
                {"value":"00:00-24:00"}
        }
        page="/pages/selectTarget/selectTarget"
        weixin.send_template_message(openid,template_id,form_id,data,page)
        num = num - 1
        if num > 0:
            form_ids[0] = (form_id, num)
            cache.set(openid, form_ids)
        else:
            form_ids.pop(0)
            cache.set(openid, form_ids)


@periodic_task(run_every=crontab(minute=1,hour=16))
def change_goal_stauts():
    today=datetime.date.today()
    goals=Goal.objects.filter(goalStatus=1,finishedTime__date__lte=today)
    for goal in goals:
        goal.goalStatus=-1
        goal.save()
