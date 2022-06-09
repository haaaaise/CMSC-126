from django.contrib import admin
# MODEL IMPORT
from .models import Feedback
from .models import Member
from .models import ShareMessage

class FeedbackAdmin(admin.ModelAdmin):
	list_display=('name','concern','message','date')
	list_filter=('name','date')
	search_fields = ('name','date')

	class Meta:
		model = Feedback

class MemberAdmin(admin.ModelAdmin):
	list_display=('username','password','firstname','lastname')
	list_filter=('username','password','firstname','lastname')
	search_fields = ('username','password','firstname','lastname')
	
	class Meta:
		model = Member

class ShareMessageAdmin(admin.ModelAdmin):
	list_display= ('sName', 'sMessage', 'date')
	list_filter= ('sName', 'sMessage', 'date')
	search_fields = ('sName', 'sMessage', 'date')
	
	class Meta:
		model = ShareMessage

# MODEL REGISTRATION TO ADMIN DATABASE
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(ShareMessage, ShareMessageAdmin)

