from django.db.models import Sum,aggregates
from django.db.models import Q
from rest_framework import serializers
from goals.models import Picture,Goal,Supervise,Wallet,TransactionRecord,Clock,Comment,Opinion,Acknowledgement,CarouselFigure
import datetime



class PictureSerializer(serializers.ModelSerializer):
    #image=serializers.ListSerializer(child=serializers.FileField(max_length=100000,allow_empty_file=False,use_url=False))
    class Meta:
        model=Picture
        fields='__all__'


class CarouseFigureSerializer(serializers.ModelSerializer):
    class Meta:
        model=CarouselFigure
        fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname',read_only=True)
    userImg = serializers.CharField(source='user.avatar_url',read_only=True)
    responseTo=serializers.SerializerMethodField()

    class Meta:
        model=Comment
        fields=('id','content','clock','nickname','userImg','responseTo','comment','flag')
    def get_responseTo(self,instance):
        if instance.comment:
            return instance.comment.user.nickname
        else:
            return None

class OpinionSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname',read_only=True)
    userImg = serializers.CharField(source='user.avatar_url',read_only=True)
    class Meta:
        model=Opinion
        fields=('id','nickname','userImg','clock','isLike','createTime')

class AcknowledgementSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='supervisor.nickname',read_only=True)
    userImg = serializers.CharField(source='supervisor.avatar_url',read_only=True)
    class Meta:
        model=Acknowledgement
        fields=('id','nickname','userImg','clock','is_acknowledge','acknowledgeTime')


class ClockSerializer(serializers.ModelSerializer):
    userName=serializers.CharField(source='user.nickname',read_only=True)
    userImg=serializers.CharField(source='user.avatar_url',read_only=True)
    opinions=OpinionSerializer(many=True,read_only=True)
    is_opinion=serializers.SerializerMethodField()
    acknowledgements=AcknowledgementSerializer(many=True,read_only=True)
    is_acknowledge=serializers.SerializerMethodField()
    comments=CommentSerializer(many=True,read_only=True)
    pictures=PictureSerializer(many=True,read_only=True)

    def get_is_opinion(self,instance):
        request=self.context['request']
        opinion=Opinion.objects.filter(user=request.user,clock=instance)
        if opinion:
            return opinion[0].isLike
        else:
            return False

    #def validate(self,data):
    #    if Clock.objects.filter(goal_id=data['goal'],clockTime__date__lte=datetime.date.today()).count()>1:
    #        raise serializers.ValidationError("one goal must be clock a day one time")
    #   return data

    def get_is_acknowledge(self,instance):
        request=self.context['request']
        acknowledgement=Acknowledgement.objects.filter(supervisor=request.user,clock=instance)
        if acknowledgement:
            return acknowledgement[0].is_acknowledge
        else:
            return False
    class Meta:
        model=Clock
        fields=('id','goal','userName','userImg','clockTime','content','pictures',
        'isConfirm','comments','opinions','is_opinion','acknowledgements','is_acknowledge')

class GoalSerializer(serializers.ModelSerializer):
    userImg=serializers.CharField(source='user.avatar_url')
    nickname=serializers.CharField(source='user.nickname')
    supervisors = serializers.SerializerMethodField()
    clocks=ClockSerializer(many=True,read_only=True)

    def get_supervisors(self,obj):
        return obj.supervise.all().values("supervisor__nickname","supervisor__avatar_url")

    class Meta:
        model=Goal
        fields=('id','userImg','nickname','content','conMoney','minSupMoney','goalType',
                'createdTime','finishedTime','poster_template','poster','goalStatus','supervisors',
                'clock_num','clocks','qrcode')

class SuperviseSerializer(serializers.ModelSerializer):
    nickname=serializers.CharField(source='goal.user.nickname')
    userImg=serializers.CharField(source='goal.user.avatar_url')
    content=serializers.CharField(source='goal.content')
    #supMoney=serializers.CharField(source='goal.supMoney')
    goalStatus=serializers.CharField(source='goal.goalStatus')
    finishedTime=serializers.DateTimeField(source='goal.finishedTime')
    supervisors=serializers.SerializerMethodField()

    class Meta:
        model=Supervise
        fields=('id','goal_id','nickname','userImg','createdTime','finishedTime','goalStatus','content','supMoney','supervisors')

    def get_supervisors(self,obj):
        return obj.goal.supervise.all().exclude(id=obj.id).values("supervisor__nickname","supervisor__avatar_url")

class WalletSerializer(serializers.ModelSerializer):
    freeze=serializers.SerializerMethodField()
    class Meta:
        model=Wallet
        fields=('banlance','freeze')
    def get_freeze(self,obj):
        freeze=TransactionRecord.objects.filter(Q(user=obj.user,operateType='pay',goal_id__isnull=True)
                                                |Q(user=obj.user,operateType='pay',goal__goalStatus=1)|Q(user=obj.user,operateType='pay',goal__goalStatus=0)).aggregate(freeze=Sum('amount'))['freeze']
        if freeze:
            return freeze
        else:
            return 0


class TransactionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=TransactionRecord
        fields='__all__'











