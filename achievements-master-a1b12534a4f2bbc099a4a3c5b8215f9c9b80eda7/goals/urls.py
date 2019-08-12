from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import *

router=DefaultRouter()
router.register(r'goals',GoalViewSet,'goals')
router.register(r'supervises',SuperviseViewSet,'supervises')
router.register(r'transaction_records',TransactionRecordViewSet,'transaction_records')
router.register(r'clocks',ClockViewSet,'clocks')
router.register(r'acknowledgements',AcknowledgementViewSet,'acknowledgements')
router.register(r'opinions',OpinionViewSet,'opinions')
router.register(r'comments',CommentViewSet,'comments')
router.register(r'pictures',PictureViewSet,'pictures')

urlpatterns=[
    path(r'carousel_figure/',CarouselFigureList.as_view()),
    path(r'wallet/',WalletRetrieve.as_view()),
    path(r'login/',login,name='login'),
    path(r'unifiedorder/',unifiedorder),
    path(r'withdraw_cash/',withdrawCash),
    path(r'refund/',refund),
    path(r'form_ids/',get_form_id)
    ]+router.urls
