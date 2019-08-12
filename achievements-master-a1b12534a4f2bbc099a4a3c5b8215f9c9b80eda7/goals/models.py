import os
import random
import logging
import datetime
import pytz

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,AbstractUser
from django.conf import settings
from django.core.exceptions import ValidationError
from goals.utils import Poster


GOALTYPE = (
    (0, u'阶段性目标'),
    (1, u'一次性目标'),
)

GOALSTATUS = (
    (-1, u'失败'),
    (0, u'待激活'),
    (1, u'进行中'),
    (2, u'完成')
)

OPERATETYPE = (
    ('refund', u'退款'),
    ('withdrawCash', u'提现'),
    ('pay','支付'),
    ('income','收入')
)

SEX = (
    ('F', u'女性'),
    ('M', u'男性'),
)

STATUS=(
    ('done',u'已完成'),
    ('ongoing',u'进行中')
)


class MyUserManager(BaseUserManager):
    #use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class MyUser(AbstractUser):
    #username = models.CharField(verbose_name=u'用户标识', max_length=150, unique=True)
    nickname = models.CharField(verbose_name=u'昵称', max_length=100,null=True,blank=True)
    avatar_url = models.URLField(verbose_name=u'用户图像URL', null=True, blank=True)
    phone_num = models.CharField(verbose_name=u'手机号码', max_length=25, null=True, blank=True, )
    city = models.CharField(verbose_name=u'城市', max_length=100, null=True, blank=True)
    province = models.CharField(verbose_name=u'省份', max_length=100, null=True, blank=True)
    country = models.CharField(verbose_name=u'国家', max_length=100, default='china')
    qq = models.CharField(verbose_name=u'QQ 号码', max_length=20, null=True, blank=True)
    wechat = models.CharField(verbose_name=u'微信号', max_length=50, null=True, blank=True)
    signature = models.CharField(max_length=4096, default='', blank=True)
    address = models.CharField(verbose_name=u'地址', max_length=100, null=True, blank=True)
    sex = models.CharField(verbose_name=u'性别', choices=SEX, max_length=1, null=True, blank=True)
    language = models.CharField(verbose_name=u'语言', default='zh-hans', max_length=50)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = verbose_name


class CarouselFigure(models.Model):
    img = models.ImageField(verbose_name=u'上传图片',upload_to='carousel/')
    description = models.CharField(verbose_name=u'图片说明', max_length=256, null=True, blank=True)
    link = models.CharField(verbose_name=u'链接', max_length=256, null=True, blank=True)
    is_published = models.BooleanField(verbose_name=u'是否显示', default=False)
    created_time = models.DateTimeField(verbose_name=u'添加时间', default=timezone.now)

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.description if self.description is not None else self.img.name


class Goal(models.Model):
    user = models.ForeignKey(MyUser, verbose_name=u'USER', on_delete=models.CASCADE)
    content = models.CharField(verbose_name=u'目标内容', max_length=256)
    conMoney = models.FloatField(verbose_name=u'小信心金额')
    minSupMoney = models.FloatField(verbose_name=u'最小支持金额',default=0.0)
    goalType = models.PositiveSmallIntegerField(verbose_name=u'目标类型', choices=GOALTYPE, default='onetime',
                                                help_text=u"0:阶段性目标,1:一次性目标")
    clock_num=models.PositiveSmallIntegerField(verbose_name=u'打卡次数',default=1)
    createdTime = models.DateTimeField(verbose_name=u'创建时间', default=timezone.now)
    finishedTime = models.DateTimeField(verbose_name=u'完成时间')
    poster_template=models.ImageField(verbose_name=u'目标海报模板',null=True,blank=True)
    poster=models.ImageField(verbose_name=u'目标海报',null=True,blank=True)
    poster_result=models.ImageField(verbose_name=u'结果海报',null=True,blank=True)
    qrcode=models.ImageField(verbose_name=u'二维码',null=True,blank=True)
    goalStatus = models.SmallIntegerField(verbose_name=u'目标状态', choices=GOALSTATUS, default=0,
                                                  help_text=u"-1:失败,0:待激活,1:进行中,2:完成")

    def is_complete(self):
        local=pytz.timezone("Asia/Shanghai")
        finishedTime=self.finishedTime.astimezone(local)
        print(finishedTime)
        today = datetime.date.today()
        print(today)
        if finishedTime.date() != today:
            return False
        if self.goalType == 'onetime':
            if self.clocks.all()[0].isConfirm:
                return True
            else:
                return False
        else:
            print("clocks:{}".format(self.clocks.all()))
            if self.clock_num <= self.clocks.all().filter(isConfirm=True).count():
                return True
            else:
                return False

    def save(self,*args,**kwargs):
        BASE_DIR=settings.BASE_DIR
        templates_path=os.path.join(BASE_DIR,'media/template')
        logging.debug(templates_path)
        #templates=[template for template in os.listdir(templates_path) if template.startswith('t')]
        #self.poster_template=os.path.join('template',random.choice(templates))
        self.poster_template=os.path.join('template','background.png')
        logging.debug(self.poster_template)
        super().save(*args, **kwargs)

    def generate_poster(self):
        poster=Poster(self)
        poster_path=poster.make_goal_poster()
        return poster_path

    def get_date(self):
        return self.finishedTime.date()

    class Meta:
        verbose_name = u'目标'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class Supervise(models.Model):
    supervisor = models.ForeignKey(MyUser, verbose_name=u'USER', on_delete=models.CASCADE)
    supMoney=models.FloatField(verbose_name=u'支持金额',default=0.0)
    goal = models.ForeignKey(Goal, verbose_name=u'目标', on_delete=models.CASCADE,related_name='supervise')
    createdTime = models.DateTimeField(verbose_name=u'开始监督时间', default=timezone.now)

    def save(self, *args,**kwargs):
        if not isinstance(self.supMoney,float):
            raise TypeError("supMoney must a float field")
        if self.supMoney>self.goal.conMoney:
            raise ValidationError("supMoney amount must be litter than conMoney")
        super().save(*args, **kwargs)


    class Meta:
        verbose_name=u"目标监督"
        verbose_name_plural=verbose_name
        unique_together=(('supervisor','goal'))


class Wallet(models.Model):
    user = models.OneToOneField(MyUser, verbose_name=u'USER', on_delete=models.CASCADE)
    banlance = models.FloatField(verbose_name=u'账户余额',default=0)
    createdTime = models.DateTimeField(verbose_name=u'钱包创建时间',default=timezone.now)

    class Meta:
        verbose_name = u'钱包'
        verbose_name_plural = verbose_name


class TransactionRecord(models.Model):
    user = models.ForeignKey(MyUser, verbose_name=u'USER', on_delete=models.CASCADE)
    operateType = models.CharField(verbose_name=u'操作类型', choices=OPERATETYPE,max_length=15,
                                   default='pay',help_text="'pay':u'支付','withdrawCash': u'提现','refund':u'退款','income':u'收入'")
    amount = models.FloatField(verbose_name=u'操作金额')
    description=models.CharField(verbose_name=u'交易描述',max_length=4096,null=True,blank=True)
    goal=models.ForeignKey(Goal,verbose_name=u'目标',null=True,blank=True,on_delete=models.SET_NULL)
    trade_no=models.CharField(verbose_name=u'订单号',max_length=64,null=True,blank=True)
    status=models.CharField(verbose_name=u'交易状态',choices=STATUS,default='done',max_length=10)
    createdTime = models.DateTimeField(verbose_name=u'交易创建时间',default=timezone.now)
    finishedTime=models.DateTimeField(verbose_name=u'交易完成时间',null=True,blank=True)

    def save(self, *args,**kwargs):
        if self.pk is None:
            self.finishedTime=self.createdTime
            super().save(*args,**kwargs)
        else:
            self.finishedTime=timezone.now()
            super().save(*args, **kwargs)

    class Meta:
        verbose_name = u'交易记录'
        verbose_name_plural = verbose_name

class Clock(models.Model):
    goal=models.ForeignKey(Goal,verbose_name='目标',on_delete=models.CASCADE,related_name='clocks')
    user = models.ForeignKey(MyUser, verbose_name=u'USER', on_delete=models.CASCADE)
    clockTime=models.DateTimeField(verbose_name=u'打卡时间',default=datetime.datetime.today)
    content=models.CharField(verbose_name=u'内容',max_length=256)
    #img=models.ImageField(verbose_name=u'图片',null=True,blank=True)
    isConfirm=models.BooleanField(verbose_name=u'打卡是否确认',default=False)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name=u'打卡记录'
        verbose_name_plural=verbose_name

class Picture(models.Model):
    clock=models.ForeignKey(Clock,verbose_name='打卡记录',related_name='pictures',on_delete=models.CASCADE)
    image=models.ImageField(verbose_name="图片",upload_to="upload/")
    uploadTime=models.DateTimeField(verbose_name=u'上传时间',default=timezone.now)

    class Meta:
        verbose_name=u'图片'
        verbose_name_plural=verbose_name

class Acknowledgement(models.Model):
    supervisor=models.ForeignKey(MyUser,verbose_name=u'监督者',on_delete=models.CASCADE)
    clock=models.ForeignKey(Clock,verbose_name=u'打卡内容',on_delete=models.CASCADE,related_name='acknowledgements')
    is_acknowledge=models.BooleanField(verbose_name=u"是否支持",default=True)
    acknowledgeTime=models.DateTimeField(verbose_name=u'确认时间',default=timezone.now)

    class Meta:
        verbose_name=u'打卡确认'
        verbose_name_plural=verbose_name
        unique_together=(('supervisor','clock'))

class Comment(models.Model):
    clock=models.ForeignKey(Clock,verbose_name=u'打卡内容',on_delete=models.CASCADE,null=True,blank=True,related_name="comments")
    user=models.ForeignKey(MyUser,verbose_name=u'评论者',on_delete=models.CASCADE)
    comment=models.ForeignKey('Comment',verbose_name=u'上级评论',related_name="childs",null=True,blank=True,on_delete=models.CASCADE)
    content=models.CharField(verbose_name=u'评论内容',max_length=4096)
    commentTime=models.DateTimeField(verbose_name=u'评论时间',default=timezone.now)
    #level=models.PositiveSmallIntegerField(verbose_name=u'层级',default=1)
    flag=models.CharField(verbose_name=u'层级标签',max_length=256,null=True,blank=True)


    def __str__(self):
        return self.content

    class Meta:
        verbose_name=u'评论'
        verbose_name_plural=verbose_name

class Opinion(models.Model):
    user=models.ForeignKey(MyUser,verbose_name=u'用户',on_delete=models.CASCADE)
    clock=models.ForeignKey(Clock,verbose_name=u'打卡',on_delete=models.CASCADE,related_name='opinions')
    isLike=models.BooleanField(verbose_name=u'赞与否',default=True)
    createTime=models.DateTimeField(verbose_name=u'创建时间',default=timezone.now)

    #TODO:Validatetin on user opinion
    class Meta:
        verbose_name="点赞"
        verbose_name_plural=verbose_name
        unique_together=(('user','clock'))


class A(models.Model):
    username=models.CharField(verbose_name=u'用户姓名',max_length=32)
    login_time=models.DateTimeField(verbose_name=u'登录时间',null=True,blank=True)
    login_ip=models.GenericIPAddressField(verbose_name=u'登录IP')

    #def save(self, force_insert=False, force_update=False, using=None,
     #        update_fields=None):
     #   self.login_time=timezone.now()
    #    super().save(force_insert=False, force_update=False, using=None,
     #        update_fields=None)

    class Meta:
        verbose_name="用户登录信息"
        verbose_name_plural=verbose_name


class B(models.Model):
    word=models.CharField(verbose_name=u'敏感词',max_length=32)
    created_time=models.DateTimeField(verbose_name=u'创建时间',auto_now_add=True)
    creator=models.CharField(verbose_name=u'创建者',max_length=32)

    class Meta:
        verbose_name=u'敏感词过滤'
        verbose_name_plural=verbose_name






