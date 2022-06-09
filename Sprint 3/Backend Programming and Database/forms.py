# Based from Django documentation
# https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/

from django.forms import ModelForm

# IMPORTING MODELS FOR MAPPING OF DATA
from .models import Feedback
from .models import ShareMessage

class ContactForm(ModelForm):
	class Meta:
		model = Feedback
		fields = ['name','concern','message']

class sMessageForm(ModelForm):
	class Meta:
		model = ShareMessage
		fields = ['sName', 'sMessage']