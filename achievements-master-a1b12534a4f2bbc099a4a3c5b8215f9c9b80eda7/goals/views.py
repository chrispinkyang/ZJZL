from urllib.parse import urlencode
import requests
import logging
import time
from copy import deepcopy
from xml.etree import ElementTree
import os
import traceback

from django.conf import settings
from django.http import StreamingHttpResponse,JsonResponse
from django.shortcuts import get_object_or_404,render
from rest_framework import viewsets,response,generics,mixins
from rest_framework.decorators import api_view
from django_filters import rest_framework as filters
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import permission_classes,authentication_classes,action
from rest_framework import generics
from django.core.cache import cache
from django.db import transaction

from goals.models import *
from goals.serializers import *
from goals import utils
from goals import weixin

#TODO weixin pay interface

@permission_classes((AllowAny,))
def index(request):
    return render(request,'goals/index.html',{})

@permission_classes((AllowAny,))
def about(request):
    return render(request,'goals/about.html')

@permission_classes((AllowAny,))
def seachg(request):
    return render(request,'goals/seachg.html')

@permission_classes((AllowAny,))
def seachx(request):
    return render(request,'goals/seachx.html')

@permission_classes((AllowAny,))
def seachz(request):
    return render(request,'goals/seachz.html')


@permission_classes((AllowAny,))
def seach(request):
    return render(request,'goals/seach.html')

@permission_classes((AllowAny,))
def seachnull(request):
    return render(request,'goals/seachnull.html')

@permission_classes((AllowAny,))
def sell(request):
    return render(request,'goals/sell.html')

@permission_classes((AllowAny,))
def sign_in(request):
    return render(request,'goals/sign_in.html')

@permission_classes((AllowAny,))
def productg1(request):
    return render(request,'goals/product/productg1.html')

@permission_classes((AllowAny,))
def productg2(request):
    return render(request,'goals/product/productg2.html')

@permission_classes((AllowAny,))
def productg3(request):
    return render(request,'goals/product/productg3.html')

@permission_classes((AllowAny,))
def productg4(request):
    return render(request,'goals/product/productg4.html')

@permission_classes((AllowAny,))
def productg5(request):
    return render(request,'goals/product/productg5.html')

@permission_classes((AllowAny,))
def productg6(request):
    return render(request,'goals/product/productg6.html')

@permission_classes((AllowAny,))
def productg7(request):
    return render(request,'goals/product/productg7.html')

@permission_classes((AllowAny,))
def productx1(request):
    return render(request,'goals/product/productx1.html')

@permission_classes((AllowAny,))
def productx2(request):
    return render(request,'goals/product/productx2.html')

@permission_classes((AllowAny,))
def productx3(request):
    return render(request,'goals/product/productx3.html')

@permission_classes((AllowAny,))
def productx4(request):
    return render(request,'goals/product/productx4.html')

@permission_classes((AllowAny,))
def productx5(request):
    return render(request,'goals/product/productx5.html')

@permission_classes((AllowAny,))
def productx6(request):
    return render(request,'goals/product/productx6.html')

@permission_classes((AllowAny,))
def productz1(request):
    return render(request,'goals/product/productz1.html')

@permission_classes((AllowAny,))
def productz2(request):
    return render(request,'goals/product/productz2.html')

@permission_classes((AllowAny,))
def productz3(request):
    return render(request,'goals/product/productz3.html')

@permission_classes((AllowAny,))
def productz4(request):
    return render(request,'goals/product/productz4.html')

@permission_classes((AllowAny,))
def productz5(request):
    return render(request,'goals/product/productz5.html')

@permission_classes((AllowAny,))
def productz6(request):
    return render(request,'goals/product/productz6.html')

@permission_classes((AllowAny,))
def productz7(request):
    return render(request,'goals/product/productz7.html')




@permission_classes((AllowAny,))
def register(request):
    return render(request,'goals/register.html')

@permission_classes((AllowAny,))
def register2(request):
    return render(request,'goals/register2.html')

@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    """
    Endpoint for xiaochengxu user login,and then return the token assotiate with user,
    if the user is a new user,create it use the openid and then return the token.
    :method:POST
    :param request:
    {
    "code":"abedefjf"
    }
    :return:
    {
    "token":"abedefg"
    }
    """
    data=request.data
    print(data)
    try:
        js_code=data['code']
        userImg=data.get('userImg',None)
        nickname=data.get('userName',None)
    except KeyError as e:
        return utils.render_exceptions(e.args,1)
    base_url=settings.WEIXIN_AUTHORIZATION_URL
    appid=settings.WEIXIN_APPID
    secret=settings.WEIXIN_SECRET
    grant_type = 'authorization_code'
    params=urlencode({'appid':appid,'secret':secret,'js_code':js_code,'grant_type':grant_type})
    req_url='?'.join([base_url,params])
    print(req_url)
    try:
        response=requests.get(req_url)
        if response.status_code==200:
            try:
                openid=response.json()['openid']
                user=MyUser.objects.filter(username=openid)
                if user:
                    update_num=MyUser.objects.filter(username=openid).update(avatar_url=userImg,nickname=nickname)
                    token,created=Token.objects.get_or_create(user=user[0])
                    response_data={"openid":openid,"token":token.key}
                    return utils.render_response(response_data)
                else:
                    user=MyUser.objects.create_user(username=openid,password=openid,avatar_url=userImg,nickname=nickname)
                    token=Token.objects.create(user=user)
                    response_data={"openid":openid,"token":token.key}
                    return utils.render_response(response_data)
            except KeyError as e:
                return utils.render_exceptions(response, 1)
        else:
            return utils.render_exceptions("http request error",1)
    except Exception as e:
        return utils.render_exceptions(e.args,1)


class CarouselFigureList(generics.ListAPIView):
    """
    API endpoint for add,get,delete,retrieve pictures.
    """
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class=CarouseFigureSerializer

    def get_queryset(self):
        return CarouselFigure.objects.filter(is_published=True)[0:3]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        print(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return utils.render_response(serializer.data)


class GoalViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
    API endpoint for add,get,delete,retrieve goals
    """
    #authentication_classes = (TokenAuthentication,SessionAuthentication)
    #permission_classes = (IsAuthenticated,)
    #queryset=Goal.objects.all()
    serializer_class = GoalSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('user_id','id')
    def get_queryset(self):
        user=self.request.user
        return Goal.objects.filter(user=user)

    def get_object(self):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """

        queryset = self.filter_queryset(Goal.objects.all())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj


    @authentication_classes((TokenAuthentication, SessionAuthentication))
    @permission_classes((IsAuthenticated,))
    def list(self, request, *args, **kwargs):
        print("filter")
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return utils.render_response(serializer.data)


    @permission_classes((AllowAny,))
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return utils.render_response(serializer.data)

    @authentication_classes((TokenAuthentication,SessionAuthentication))
    @permission_classes((IsAuthenticated,))
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return utils.render_response("delete success")

    @authentication_classes((TokenAuthentication,SessionAuthentication))
    @permission_classes((IsAuthenticated,))
    def create(self, request, *args, **kwargs):
        try:
            data=request.data
            logging.info(data)
            if 'trade_no' not in data:
                return utils.render_exceptions("trade_no must be provided",1)
            trade_no=data.pop('trade_no')
            data['user'] = request.user
            goal=Goal.objects.create(**data)
            transaction=TransactionRecord.objects.get(trade_no=trade_no)
            transaction.goal=goal
            transaction.status='done'
            transaction.save()
            serializer=GoalSerializer(goal)
            return utils.render_response(serializer.data)
        except Exception as e:
            return utils.render_exceptions(e.args,1)

    @action(methods=['post'],detail=True,permission_classes=[IsAuthenticated,])
    def generate_poster(self,request,*args,**kwargs):
        #def file_iterator(file_name, chunk_size=512):
        #   with open(file_name,'rb') as f:
        #        while True:
        #           c = f.read(chunk_size)
        #            if c:
        #                yield c
        #            else:
        #                break
        goal = self.get_object()
        data=request.data
        if 'type' in data:
            poster_type=data['type']
            if poster_type=='create':
                poster_url=goal.poster
                if poster_url:
                    logging.info("poster_url:{}".format(poster_url))
                    return JsonResponse({"poster_url": poster_url.name})
                else:
                    logging.info("generate poster")
                    poster_path=goal.generate_poster()
                    filename=os.path.split(poster_path)[-1]
                    poster_url=os.path.join('poster',filename)
                    goal.poster=poster_url
                    logging.debug("poster_url:{}".format(poster_url))
                    goal.save()
                    #response = StreamingHttpResponse(file_iterator(poster_path))
                    #response['Content-Type'] = 'application/octet-stream'
                    #response['Content-Disposition'] = 'attachment;filename="{0}"'.format(poster_path)
                    return JsonResponse({"poster_url":poster_url})
            elif poster_type=='result':
                poster_url=goal.poster_result
                if poster_url:
                    logging.info("poster_url:{}".format(poster_url))
                    return JsonResponse({"poster_url": poster_url.name})
                else:
                    logging.info("generate poster")
                    if goal.goalStatus==1 or goal.goalStatus==0:
                        return utils.render_exceptions("goal does not finished",1)
                    else:
                        poster=utils.Poster(goal)
                        if goal.goalStatus==2:
                            poster_path=poster.make_result_poster(1)
                        else:
                            poster_path=poster.make_result_poster(0)
                        filename = os.path.split(poster_path)[-1]
                        poster_url=os.path.join('poster',filename)
                        goal.poster_result=poster_url
                        logging.debug("poster_url:{}".format(poster_url))
                        goal.save()
                        #response = StreamingHttpResponse(file_iterator(poster_path))
                        #response['Content-Type'] = 'application/octet-stream'
                        #response['Content-Disposition'] = 'attachment;filename="{0}"'.format(poster_path)
                        return JsonResponse({"poster_url":poster_url})
            else:
                return utils.render_exceptions("poster type is not provided",1)




class SuperviseViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    #queryset = Supervise.objects.all()
    serializer_class = SuperviseSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields=('goal_id','supervisor_id')

    def get_queryset(self):
        user=self.request.user
        return Supervise.objects.filter(supervisor=user)

    def create(self, request, *args, **kwargs):
        try:
            req_data=request.data
            print(req_data)
            try:
                goal_id=req_data.pop('goal_id')
                goal=Goal.objects.get(pk=goal_id)
            except Exception as e:
                return utils.render_exceptions(e.args,1)
            if goal.goalStatus==2:
                return utils.render_exceptions("goal has been finished",1)
            supMoney = float(req_data['supMoney'])
            req_data['supMoney']=supMoney
            if 'trade_no' not in req_data:
                if supMoney>0.0:
                    return utils.render_exceptions("trade_no must be provided",1)
            else:
                trade_no=req_data.pop('trade_no')
            user=request.user
            if goal.user == user:
                return utils.render_exceptions("you can't supervise yourself",1)
            req_data['supervisor']=request.user
            req_data['goal']=goal
            try:
                supervise=Supervise(**req_data)
                supervise.save()
            except Exception as e:
                if "Duplicate entry" in e.args:
                    return utils.render_exceptions("goal has been supervised", 1)
                return utils.render_exceptions(e.args,1)
            if supMoney>0.0:
                transaction=TransactionRecord.objects.get(trade_no=trade_no)
                transaction.goal=goal
                transaction.status='done'
                transaction.save()
            serializer = self.get_serializer(supervise)
        #serializer.is_valid(raise_exception=True)
        #self.perform_create(serializer)
        #headers = self.get_success_headers(serializer.data)
            return utils.render_response(serializer.data)
        except Exception as e:
            return utils.render_exceptions(e.args,1)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return utils.render_response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return utils.render_response("delete success")

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return utils.render_response(serializer.data)
        except Exception as e:
            logging.exception(traceback.format_exc())
            return utils.render_exceptions(e.args,1)

class WalletRetrieve(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    permission_classes(IsAuthenticated,)
    #queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user)


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return utils.render_response(serializer.data)



class TransactionRecordViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    permission_classes=(IsAuthenticated,)
    serializer_class = TransactionRecordSerializer
    def get_queryset(self):
        return TransactionRecord.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return utils.render_response(serializer.data)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return utils.render_response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return utils.render_response("delete success")
    def create(self, request, *args, **kwargs):
        data=request.data
        #print(data)
        #print("user:",request.auth)
        print(self.request.user)
        #user=Token.objects.get(key=request.auth).user
        data['user']=request.user
        if "goal_id" not in data:
            return utils.render_exceptions("create transaction failure",1)
        try:
            record=TransactionRecord.objects.create(**data)
        except Exception as e:
            return utils.render_exceptions(e.args,1)
        serializer=TransactionRecordSerializer(record)
        return utils.render_response(serializer.data)

    def update(self, request, *args, **kwargs):
        try:
            data=request.data
            if 'goal_id' not in data:
                return utils.render_exceptions("goal_id is must be provided",1)
            instance = self.get_object()
            if instance.goal is None:
                return utils.render_exceptions("illegae operate,has been info administrator",1)
            goal=Goal.objects.get(pk=data['goal_id'])
            instance.goal=goal
            instance.save()
            return utils.render_response("update success",1)
        except Exception as e:
            return utils.render_exceptions(e.args,1)


class ClockViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    permission_classes=(IsAuthenticated,)
    serializer_class = ClockSerializer
    queryset = Clock.objects.all()

    #def get_queryset(self):
    #    return Clock.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return utils.render_response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return utils.render_response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return utils.render_response("delete success")

    def create(self, request, *args, **kwargs):
        """
        :method : POST
        :body:
        {
	          "content": "test for clock",
              "goal": 11,
              "img":"sdsdsd"
        }
        :remarks:img fields is a choicable field
        :return:

        {
            "msg": "succeed",
            "status": 0,
            "result": {
                 "id": 1,
                 "clockTime": "2018-05-22 03:40:13",
                 "content": "test for clock",
                 "img": null,
                "isConfirm": false,
                "goal": 11,
                "user": 3
                }
        }
        """
        #try:
        print(request.data)
        data=request.data
            #pictures=data.pop('pictures')
        user=request.user
        goal=Goal.objects.get(pk=data['goal'])
        if Clock.objects.filter(goal=goal, clockTime__date__lte=datetime.date.today()).count() > 1:
            raise serializers.ValidationError("one goal must be clock a day one time")
        content=data['content']
        clock=Clock.objects.create(user=user,goal=goal,content=content)
        serializer=self.get_serializer(clock)
            #for picture in pictures:
            #    p=Picture.objects.create(clock=clock,image=picture)
            #    p.save()
        return utils.render_response(serializer.data)
        #except Exception as e:
         #   return utils.render_exceptions(e.args, 1)

        def destroy(self, request, *args, **kwargs):
            instance = self.get_object()
            self.perform_destroy(instance)
            return utils.render_response("delete success")

class AcknowledgementViewSet(mixins.CreateModelMixin,
                             mixins.DestroyModelMixin,
                             viewsets.GenericViewSet):
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    permission_classes=(IsAuthenticated,)
    serializer_class = AcknowledgementSerializer

    #query user clock id   url:/api/goals/acknowledgement/{clock_id}
    lookup_field = 'clock_id'
    lookup_value_regex = '[0-9]+'

    def get_queryset(self):
        return Acknowledgement.objects.filter(supervisor=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            data=request.data
            clock=data['clock']
            clock_obj=Clock.objects.get(pk=clock)
            supervisors=clock_obj.goal.supervise.all().filter(supervisor__id=request.user.id)
            if not supervisors:
                return utils.render_exceptions("you are not a supervisor",1)
            serializer = self.get_serializer(data=request.data)
            # try:
            #    clock = Clock.objects.create(**data)
            # except Exception as e:
            #    return utils.render_exceptions(e.args, 1)
            # serializer = self.serializer_class(clock)
            # return utils.render_response(serializer.data)
            serializer.is_valid()
            #self.perform_create(serializer)
            serializer.save(supervisor=request.user)
            return utils.render_response(serializer.data)
        except Exception as e:
            return utils.render_exceptions(e.args, 1)


    #def update(self, request, *args, **kwargs):
    #    try:
    #        partial = kwargs.pop('partial', False)
     #       instance = self.get_object()
     #       serializer = self.get_serializer(instance, data=request.data, partial=partial)
     #       serializer.is_valid(raise_exception=True)
     #       serializer.save(supervisor=request.user)
    #
    #        if getattr(instance, '_prefetched_objects_cache', None):
    #        # If 'prefetch_related' has been applied to a queryset, we need to
    #        # forcibly invalidate the prefetch cache on the instance.
    #            instance._prefetched_objects_cache = {}
    #
    #        return utils.render_response(serializer.data)
    #    except Exception as e:
    #        utils.render_exceptions(e.args, 1)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return utils.render_response("delete success")

class OpinionViewSet(viewsets.GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = OpinionSerializer
    #queryset = Opinion.objects.all()
    lookup_field = 'clock_id'
    lookup_value_regex = '[0-9]+'

    def get_queryset(self):
        return Opinion.objects.filter(user=self.request.user)



    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            # try:
            #    clock = Clock.objects.create(**data)
            # except Exception as e:
            #    return utils.render_exceptions(e.args, 1)
            # serializer = self.serializer_class(clock)
            # return utils.render_response(serializer.data)
            serializer.is_valid()
            #self.perform_create(serializer)
            serializer.save(user=request.user)
            return utils.render_response(serializer.data)
        except Exception as e:
            return utils.render_exceptions(e.args, 1)

    #def update(self, request, *args, **kwargs):
    #   try:
    #        partial = kwargs.pop('partial', False)
    #        instance = self.get_object()
    #        serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #        serializer.is_valid(raise_exception=True)
     #       serializer.save()
    #
     #       if getattr(instance, '_prefetched_objects_cache', None):
     #       # If 'prefetch_related' has been applied to a queryset, we need to
    #        # forcibly invalidate the prefetch cache on the instance.
     #           instance._prefetched_objects_cache = {}
    #
     #       return utils.render_response(serializer.data)
     #   except Exception as e:
     #       return utils.render_exceptions(e.args, 1)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return utils.render_response("delete success")

class CommentViewSet(mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    authentication_classes = (SessionAuthentication,TokenAuthentication)
    permission_classes=(IsAuthenticated,)
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def create(self, request, *args, **kwargs):
        #data = dict(request.data)
        # user=Token.objects.get(key=request.auth).user
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid()
            serializer.save(user=request.user)
            return utils.render_response(serializer.data)
        except Exception as e:
            return utils.render_exceptions(e.args, 1)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return utils.render_response("delete success")


class PictureViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = PictureSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return utils.render_response(serializer.data)
        except Exception as e:
            return utils.render_exceptions(e.args, 1)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,SessionAuthentication))
@permission_classes((IsAuthenticated,))
def withdrawCash(request):
    """
    :param request:
    json {"desc":desc,"amount":amount}
    :return:
    """
    try:
        data=request.data
        print(data)
        logging.debug(data)
        user=request.user
        openid=user.username
        desc=data["desc"]
        amount=data["amount"]
        wallet=Wallet.objects.get(user=user)
        if amount>wallet.banlance*100:
            return utils.render_exceptions("amount must be little than banlance",1)
        appid = settings.WEIXIN_APPID
        mch_id = settings.WEIXIN_MCH_ID
        key = settings.WEIXIN_KEY
        client = weixin.WeixinPay(appid, mch_id, key, notify_url="https://qdting.com/api/withdraw_cash/")
        pay_info=client.generate_pay_info(openid,"withdraw",amount)
        nonce_str = weixin.generate_nonce_str()
        print("pay_info:{}".format(pay_info))
        param = deepcopy(client.__dict__)
        param.pop('appid')
        param.pop('mch_id')
        param.pop('trade_type')
        param.pop('sign_type')
        param.pop('notify_url')
        param.update({'mch_appid': appid,'mchid':mch_id})
        param.update(pay_info)
        param.update({'nonce_str': nonce_str})
        key = param.pop('key')
        param = {k: v for k, v in param.items() if v}
        sign = client.generate_sign(param, key)
        param.update({'sign': sign})
        print("param:{}".format(param))
        tree=client.make_request("https://api.mch.weixin.qq.com/mmpaymkttransfers/promotion/transfers",param,user_cert=True)
        if tree is None:
            return utils.render_exceptions("https request error",1)
        else:
            return_code = tree.findtext("return_code")
            if return_code=='SUCCESS':
                result_code=tree.findtext('result_code')
                if result_code=='SUCCESS':
                    with transaction.atomic():
                        transactionrecord=TransactionRecord.objects.create(user=user,operateType='withdrawCash',amount=-amount/100.0,description=u'提现',
                                                             trade_no=pay_info['partner_trade_no'],status="done")
                        transactionrecord.save()
                        wallet=Wallet.objects.get(user=user)
                        wallet.banlance-=amount/100.0
                        wallet.save()
                    return utils.render_response("withdraw success")
                else:
                    return_msg=tree.findtext('return_msg')
                    print(ElementTree.tostring(tree))
                    return utils.render_exceptions(return_msg, 1)
            else:
                return_msg = tree.findtext("return_msg")
                print(ElementTree.tostring(tree))
                return utils.render_exceptions(return_msg, 1)
    except Exception as e:
        return utils.render_exceptions(e.args,1)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,SessionAuthentication))
@permission_classes((IsAuthenticated,))
def unifiedorder(request):
    """
    :payload:
    {
        "body":订单描述,
        "total_fee":订单金额,
        "goal_id":goal_id
    }
    :return:
    """
    try:
        data=request.data
        print(data)
        logging.debug(data)
        user=request.user
        openid=user.username
        body=data["body"]
        total_fee=data["total_fee"]
        appid=settings.WEIXIN_APPID
        mch_id=settings.WEIXIN_MCH_ID
        key=settings.WEIXIN_KEY
        client=weixin.WeixinPay(appid,mch_id,key,notify_url="https://qdting.com/api/unifiedorder/")
        pay_info=client.generate_order_info(openid,body,total_fee)
        nonce_str=weixin.generate_nonce_str()
        print("pay_info:{}".format(pay_info))
        param=deepcopy(client.__dict__)
        param.update(pay_info)
        param.update({'nonce_str':nonce_str})
        key=param.pop('key')
        param={k:v for k,v in param.items()if v}
        sign=client.generate_sign(param,key)
        param.update({'sign':sign})
        print("param:{}".format(param))
        tree=client.make_request("https://api.mch.weixin.qq.com/pay/unifiedorder",param)
        if tree is None:
            return utils.render_exceptions("https request error",1)
        else:
            return_code = tree.findtext("return_code")
            if return_code=='SUCCESS':
                result_code = tree.findtext('result_code')
                if result_code == 'SUCCESS':
                    #with transaction.atomic():
                    if not 'goal_id' in data:
                        transactionrecord=TransactionRecord.objects.create(user=user,amount=total_fee/100.0,description=u'制定目标',trade_no=
                                                             pay_info['out_trade_no'],status='ongoing')
                    else:
                        transactionrecord = TransactionRecord.objects.create(user=user, amount=total_fee/100.0, description=u'监督目标',
                                                                   trade_no=pay_info['out_trade_no'], status='ongoing')
                        #wallet=Wallet.objects.get(user=user)
                        #wallet.banlance-=total_fee/100.0
                        #wallet.save()
                    prepay_id = tree.findtext("prepay_id")
                    timestamp=str(int(time.time()))
                    nonce_str=weixin.generate_nonce_str()
                    sign_type=client.sign_type
                    package="prepay_id={}".format(prepay_id)
                    param={"appId":appid,"timeStamp":timestamp,"nonceStr":nonce_str,"package":package,"signType":sign_type}
                    sign=weixin.generate_sign(param,key,sign_type)
                    param.update({"paySign":sign})
                    param.update({'trade_no':pay_info['out_trade_no']})
                    logging.debug("return:{}".format(param))
                    return utils.render_response(param)
                else:
                    return_msg = tree.findtext("return_msg")
                    print(ElementTree.tostring(tree))
                    return utils.render_exceptions(return_msg, 1)
            else:
                return_msg=tree.findtext("return_msg")
                print(ElementTree.tostring(tree))
                return utils.render_exceptions(return_msg,1)
    except Exception as e:
        logging.exception(e)
        return utils.render_exceptions(e.args,1)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,SessionAuthentication))
@permission_classes((IsAuthenticated,))
def refund(request):
    """
    :param request:
    json{"trade_no":trade_no}
    :return:
    """
    try:
        data=request.data
        logging.debug(data)
        if "trade_no" in data:
            trade_no=data.pop('trade_no')
        else:
            return utils.render_exceptions("trade_no is must be provided")
        appid = settings.WEIXIN_APPID
        mch_id = settings.WEIXIN_MCH_ID
        key = settings.WEIXIN_KEY
        query_client = weixin.WeixinPay(appid, mch_id, key, notify_url="https://qdting.com/api/refund/")
        orderquery_info=query_client.generate_orderquery_info({"out_trade_no":trade_no})
        nonce_str = weixin.generate_nonce_str()
        query_param = deepcopy(query_client.__dict__)
        query_param.update(orderquery_info)
        query_param.update({'nonce_str': nonce_str})
        key = query_param.pop('key')
        query_param = {k: v for k, v in query_param.items() if v}
        sign = query_client.generate_sign(query_param, key)
        query_param.update({'sign': sign})
        print("param:{}".format(query_param))
        tree = query_client.make_request("https://api.mch.weixin.qq.com/pay/orderquery", query_param)
        if tree is None:
            return utils.render_exceptions("https request error", 1)
        else:
            return_code = tree.findtext("return_code")
            if return_code == 'SUCCESS':
                result_code=tree.findtext("result_code")
                if result_code=='SUCCESS':
                    trade_state=tree.findtext("trade_state")
                    if trade_state!="SUCCESS":
                        return utils.render_exceptions("非法操作,已通知管理员",1)
                else:
                    return_msg = tree.findtext("return_msg")
                    ElementTree.tostring(tree)
                    return utils.render_exceptions(return_msg, 1)
            else:
                return_msg = tree.findtext("return_msg")
                ElementTree.tostring(tree)
                return utils.render_exceptions(return_msg, 1)
        transactionrecord = TransactionRecord.objects.get(trade_no=trade_no)
        data['out_trade_no'] = trade_no
        amount = transactionrecord.amount
        data['total_fee'] = amount
        data['refund_fee'] = amount
        user=request.user
        openid = user.username
        appid = settings.WEIXIN_APPID
        mch_id = settings.WEIXIN_MCH_ID
        key = settings.WEIXIN_KEY
        client=weixin.WeixinPay(appid,mch_id,key,notify_url="https://qdting.com/api/refund/")
        refund_info=client.generate_refund_info(data)
        nonce_str = weixin.generate_nonce_str()
        param = deepcopy(client.__dict__)
        param.update(refund_info)
        param.update({'nonce_str': nonce_str})
        key = param.pop('key')
        param = {k: v for k, v in param.items() if v}
        sign = client.generate_sign(param, key)
        param.update({'sign': sign})
        print("param:{}".format(param))
        tree = client.make_request("https://api.mch.weixin.qq.com/pay/refundquery", param,user_cert=True)
        if tree is None:
            return utils.render_exceptions("https request error", 1)
        else:
            return_code = tree.findtext("return_code")
            if return_code == 'SUCCESS':
                result_code=tree.findtext('result_code')
                if result_code=='SUCCESS':
                    with transaction.atomic():
                        goal=transactionrecord.goal
                        #supervisor refund
                        if goal.user!=request.user:
                            refund_transaction=TransactionRecord.objects.create(user=user,operateType="refund",amount=-amount/100.0,
                                                                        description=u"创建监督失败",
                                                                        trade_no=refund_info['out_refund_no'],goal=transactionrecord.goal,
                                                                        )
                        #goal_maker refund
                        else:
                            refund_transaction=TransactionRecord.objects.create(user=user,operateType="refund",amount=-amount/100.0,
                                                                        description="创建目标失败",
                                                                        trade_no=refund_info['out_refund_no'],goal=transactionrecord.goal)
                    return utils.render_response("refund success")
                else:
                    return_msg = tree.findtext("return_msg")
                    #ElementTree.tostring(tree)
                    return utils.render_exceptions(return_msg, 1)
            else:
                return_msg = tree.findtext("return_msg")
                # ElementTree.tostring(tree)
                return utils.render_exceptions(return_msg, 1)
    except Exception as e:
        return utils.render_exceptions(e.args, 1)



@api_view(["POST",])
@authentication_classes((SessionAuthentication,TokenAuthentication))
@permission_classes((IsAuthenticated,))
def get_form_id(request):
    """
    url:/api/form_ids/
    request param:
    {
        "form_id":
        "prepay_id":
    }
    """
    try:
        logging.debug(request.data)
        print(request.data)
        data=request.data
        user=request.user
        openid=user.username
        print(openid)
        form_ids=cache.get(openid)
        if form_ids is None:
            form_ids=[]
        if "form_id" in data:
            form_id=data['form_id']
            form_ids.append((form_id,1))
        if "prepay_id" in data:
            form_id=data['prepay_id']
            form_ids.append((form_id,3))
        cache.set(openid,form_ids)
        return utils.render_response({"update formId success!"})
    except Exception as e:
        logging.debug(e)
        return utils.render_exceptions(e.args,1)











