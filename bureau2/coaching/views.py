from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .models import Detail, Profile , time
from django.contrib.auth.forms import UserCreationForm
from .form import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

import random
from django.conf import settings

import http.client
from django.shortcuts import render
from django.core.files import File
import csv
import datetime




context = {
           'amt': 0,
           'tot': 0,
           'std': '',
           'sub': '',
            'cour': '',
           }



def timeT(request):
        times = time.get_all_times()
        print(times)
        return render(request, 'schedule.html',  {'times': times} )

def index(request):

    print('you 1 are=', request.session.get('email'))

    return render(request, 'index.html')

def ul(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "login successfully!!")
                    request.session['user_id'] = user.id
                    request.session['email'] = user.email
                    print('you 2 are=', request.session.get('email'))
                    print('you 2 are=', request.session.get('user_id'))
                    return HttpResponseRedirect('/user_profile/')
            else:
                messages.error(request, "Invalid Login")
                return redirect('/ul')
        else:
            fm = AuthenticationForm()
            return render(request, 'ul.html', {'form': fm})
    else:
        return HttpResponseRedirect('/user_profile/')

def user_profile(request):

    if request.user.is_authenticated:
        if request.method == 'POST':
            sname = request.user.first_name
            board = request.POST["board"]
            school = request.POST["school"]
            stand = request.POST["stand"]
            subject = request.POST["subject"]
            course = request.POST["course"]
            address = request.POST["address"]
            phone = request.POST["phone"]
            cno = request.POST['cno']


            if stand == '6' or stand == '7' or stand == '8':
                if course == "Monthly":
                    amount = 780
                elif course == "Term":
                    amount = 4290
                elif course == "Yearly":
                    amount = 8580
            elif stand == '9' or stand == '10':
                if course == "Monthly":
                    amount = 880
                elif course == "Term":
                    amount = 4840
                elif course == "Yearly":
                    amount = 9680
            elif stand == '11' or stand == '12':
                if course == "Monthly":
                    amount = 1000
                elif course == "Term":
                    amount = 5500
                elif course == "Yearly":
                    amount = 11000

            context['amt'] = amount
            context['tot'] = context['tot'] + amount
            amount = context['tot']
            po = Detail(sname=sname, board=board, school=school, stand=stand, subject=subject, course=course,  amount=amount,
                        address=address, phone=phone)
            po.save()
            context['std'] = stand
            context['sub'] = context['sub'] +','+ subject
            context['cour'] = course
            messages.success(request, "Message has been sent")
            print(cno)

            return redirect("/user_profile/")
        else:
                return render(request, 'profile.html', {'name': request.user})
        # context

    else:
        return HttpResponseRedirect('/ul/')

def profile2(request):

    return render(request, "profile2.html", context )

def payment(request):
    return render(request, "payment.html", context)

def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        #fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Account  has been created successfully!!")
    else:
        fm = SignUpForm()
        #fm = UserCreationForm()
    return render(request, 'sign_up.html', {'form': fm})


def user_logout(request):
    logout(request)
    messages.success(request, "You are logged out")
    return redirect('/')


def about(request):
    return render(request, 'about.html')


def send_otp(mobile, otp):
    conn = http.client.HTTPSConnection("api.msg91.com")
    headers = {'content-type': "application/json"}
    authkey = settings.authkey
    url = "http://control.msg91.com/api/sendotp.php?otp"+otp+'&sender=ABCmessage='+'&Your otp is=' +otp+'&mobile='+mobile+'&authkey='+authkey+'&country='+91
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()
    return None

def otp(request):
    mobile = request.session['mobile']
    context = {'mobile':'mobile'}
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = Profile.objects.filter(mobile=mobile).first()
        if otp == profile.otp:
            return redirect('payment')
        else:
            context = {'message': 'wrong otp', 'mobile':'mobile' }

        return render(request, 'otp.html', context)

def register(request):
    if request.method == 'POST':
        email = request.POST["email"]
        name = request.POST["name"]
        mobile = request.POST["mobile"]

        check_user = User.objects.filter(email=email).first()
        check_profile = Profile.objects.filter(mobile=mobile).first()

        print(check_user)
        if check_user or check_profile:
            context = {'message':'User already exist'}
            return render(request, 'register.html', context)
        else:
            user = User(email=email, first_name=name)
            user.save()

            otp = str(random.randint(1000, 9999))

            profile = Profile(user=user, mobile=mobile, otp=otp)
            profile.save()
            send_otp(mobile, otp)
            request.session["mobile"] = mobile
        return redirect('otp')

    return render(request, 'register.html')



def song1(request):

	return render(request, 'fun.html')


