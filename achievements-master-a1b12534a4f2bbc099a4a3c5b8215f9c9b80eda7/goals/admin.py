from django.contrib import admin

from goals.models import A,B
from goals.models import Picture,Goal,MyUser,Supervise,TransactionRecord,Wallet,Clock,Acknowledgement,Comment,Opinion,CarouselFigure
# Register your models here.
admin.site.register(MyUser)
admin.site.register(CarouselFigure)
admin.site.register(Picture)
admin.site.register(Goal)
admin.site.register(Supervise)
admin.site.register(Wallet)
admin.site.register(Clock)
admin.site.register(Acknowledgement)
admin.site.register(Comment)
admin.site.register(Opinion)

class TransactionRecordAdmin(admin.ModelAdmin):
    list_display = ('id','user','operateType','amount','description','goal','trade_no','status','createdTime','finishedTime')

#class AAdmin(admin.ModelAdmin):
#    list_display = ('id','username','login_time','login_ip')
#    list_per_page = 10

#class BAdmin(admin.ModelAdmin):
#    list_display = ('id','word','created_time','creator')
#    list_per_page = 10

#admin.site.register(A,AAdmin)
#admin.site.register(B,BAdmin)
admin.site.register(TransactionRecord,TransactionRecordAdmin)
