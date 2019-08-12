from django.dispatch import receiver
from django.db.models.signals import post_save
from goals.models import MyUser,Wallet,Supervise,Acknowledgement,Comment,Clock,Goal,TransactionRecord
from goals.tasks import check_and_perferm,supervise_notification,acknowledge_notification,notify_goal_maker
import logging

from goals import weixin

@receiver(post_save,sender=MyUser)
def create_wallet(sender,instance,*args,**kwargs):
    if not Wallet.objects.filter(user=instance):
        try:
            wallet=Wallet(user=instance)
            wallet.save()
        except Exception as e:
            logging.error(e)

@receiver(post_save,sender=Supervise)
def after_supervise(sender,instance,*args,**kwargs):
    logging.debug("change the goal's status")
    goal=instance.goal
    goalStatus=goal.goalStatus
    if goalStatus==1:
        supervise_notification.delay(instance.id)
    if goalStatus==0:
        goal.goalStatus=1
        goal.save()
        supervise_notification.delay(instance.id)
    #transaction=TransactionRecord.objects.get(user=instance.supervisor,goal=instance.goal,status='ongoing')
    #if transaction:
    #    transaction.status='done'
    #    transaction.save()



@receiver(post_save,sender=Acknowledgement)
def is_confirm(sender,instance,*args,**kwargs):
    supervisor=instance.supervisor
    nickname=supervisor.nickname
    clock=instance.clock
    if clock.isConfirm:
        return
    goal=clock.goal
    goal_id=goal.id
    supervises=goal.supervise.all()
    supervisor_count=supervises.count()
    acknowledgement_count=Acknowledgement.objects.filter(clock=clock).count()

    if acknowledgement_count*2>=supervisor_count:
        clock.isConfirm=True
        clock.save()
        if goal.goalStatus==2 :
            notify_goal_maker.delay(instance.id)
            return
        else:
            notify_goal_maker.delay(instance.id)
            check_and_perferm.delay(goal_id)
    else:
        notify_goal_maker.delay(instance.id)




@receiver(post_save,sender=Comment)
def add_flag(sender,instance,*args,**kwargs):
    flag=instance.flag
    comment=instance.comment
    if not flag:
        if not comment:
            instance.flag=str(instance.pk)
            instance.save()
        else:
            last_flag=comment.flag
            instance.flag='_'.join([last_flag,str(instance.pk)])
            instance.save()

@receiver(post_save,sender=Clock)
def after_clock(sender,instance,*args,**kwargs):
    #goal=instance.goal
    acknowledge_notification.delay(instance.id)


@receiver(post_save,sender=Goal)
def generate_qrcode(sender,instance,*args,**kwargs):
    print("generate qrcode")
    if not instance.qrcode:
        qrcode_path=weixin.generate_qrcode(instance.user.username,instance.id)
        instance.qrcode=qrcode_path
        instance.save()


