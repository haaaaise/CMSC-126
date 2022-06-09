from django.shortcuts import redirect, render, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# IMPORTING THE MODELS FOR VIEWING
from .models import Feedback
from .models import Member
from .models import ShareMessage

# IMPORTING THE FORMS FOR SAVING
from .forms import ContactForm
from .forms import sMessageForm

# Create your views here.
# request -> response
# request handler
# action

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def basepage(request):
    return render(request, 'hello.html')

def sharemessage(request):
    if request.method == 'POST':    
        sName = request.POST.get('sName')
        sMessage = request.POST.get('sMessage')
        date = request.POST.get('date')
        sharemessage = sMessageForm(request.POST) #name=name, email=email, message=message,date=date)
        sharemessage.save()   
    return render(request, 'sMessage.html')

def helpdesk(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        concern = request.POST.get('concern')
        message = request.POST.get('message')
        date = request.POST.get('date')
        form = ContactForm(request.POST) #name=name, email=email, message=message,date=date)
        form.save()   
    return render(request, 'helpdesk.html')

def updates(request):
    return render(request, 'l_updates.html')

# Deprecated code
# def sharespace(request):
#     context = {
#         'feedbacks': Feedback.objects.all()
#     }
#     return render(request, 'sharespace.html', context)

def sharespaces(request):
    context = {
        'share_message': ShareMessage.objects.all()
    }
    return render(request, 's_sharespace.html', context)

def index(request):
    return render(request, 'index.html')

def a_test(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'a.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'login.html', context)
#    return render(request, 'a.html')

def login_home(request):
    return render(request, 'a.html')

def home_page(request):
    return render(request, 'home_page.html')

def register(request):
    if request.method == 'POST':
#       firstname = request.POST.get('firstname')
#        lastname = request.POST.get('lastname')
#        username = request.POST.get('username')
#        password = request.POST.get('password')
#        member = Member(request.POST)
        member = Member(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'register.html')
    
   

#    return redirect('/')
#    return render(request, 'register.html')
 
def login(request):
    return render(request, 'login.html')

def index_redirect(request):
    return redirect('')

