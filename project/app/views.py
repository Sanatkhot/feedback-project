from django.shortcuts import render,HttpResponse,redirect
from .forms import Signupform
from .forms import Feedback_form
from django.contrib.auth.forms import AuthenticationForm   # for signin view
from django.contrib.auth import authenticate, login, logout # for sign in
from django.contrib import messages
from .models import Feedback
from .models import Contact
def index(request):
    return render(request,'index.html')

def AboutUs(request):
    return render(request,'aboutus.html')

def ContactUs(request):
    if request.method =="POST":
        email = request.POST.get('email')
        text = request.POST.get('text')
        contact = Contact(email=email, text=text)
        contact.save()
        # messages.success(request, "Your Massage has been sent :)")
    return render(request, 'contactus.html')

def feedback(request):
    if request.method=='POST':
        cb=Feedback_form(request.POST)
        if cb.is_valid():
            cb.save()
        #redirect With url patch
        return redirect('feedback')    
    else:
        cb=Feedback_form()  
    show=Feedback.objects.all()    
    return render(request,"Feedback.html",{'feedback':cb,'show':show})

def showfeed(request):
    show=Feedback.objects.all()
    return render(request,'showfeed.html',{'show':show})

def course(request):
    return render(request,'course.html')


def signup(request):
    if request.method == "POST":
        fm = Signupform(request.POST)
        if fm.is_valid():
            fm.save()
            # messages.success(request, 'You have register successfully.')
            return redirect("signin")
    else:    
        fm=Signupform()
    return render(request,'Signup.html',{'fm':fm})

def signin(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return render(request, 'index.html', {'user': user,})
    else:
        fm = AuthenticationForm()
    return render(request, "signin.html", {'user_data': fm})


def signout(request):
    logout(request)
    return redirect('/')