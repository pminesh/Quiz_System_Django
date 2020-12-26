from django.shortcuts import render, redirect
from CWH.models import Contactus, Quiz_Quistion, QuizCourse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

# ************************Home


@login_required(login_url='')
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    courses = QuizCourse.objects.all()
    return render(request, "index.html", {'courses': courses})

# ************************Registration


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        if User.objects.filter(username=username).exists():
            messages.info(request, 'User Name is Already Taken..!!')
            return redirect('register')
        else:
            user_form = User.objects.create_user(
                username=username, password=password, first_name=firstname, last_name=lastname)
            user_form.save()
            messages.info(
                request, 'User Registration Successfuly Now You Can Login..!!')
            return render(request, 'login.html')
    return render(request, 'registration.html')

# ************************Login


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            courses = QuizCourse.objects.all()
            return render(request, 'index.html', {'courses': courses})
        else:
            messages.info(
                request, "Please enter valid password and username !")
            return render(request, 'login.html')
    return render(request, "login.html")

# *************************Quiz


@login_required(login_url='')
def take_quiz(request, id):
    courses = QuizCourse.objects.all()
    c_name = QuizCourse.objects.get(id=id)
    course_name = c_name.coursename
    qestion = Quiz_Quistion.objects.all()
    questions = []
    for i in qestion:
        if c_name.coursename == i.quiz_type.coursename:
            questions.append(i)
    context = {'id': id, 'courses': courses,
               'questions': questions, 'course_name': course_name}
    return render(request, "quiz.html", context)

# *************************Contact Us


@login_required(login_url='')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        phone = request.POST.get('phone')

        contact = Contactus(name=name, email=email, desc=desc,
                            address=address, city=city, state=state, phone_num=phone)
        contact.save()
        messages.success(request, "your message has been sent!")
        courses = QuizCourse.objects.all()
        return render(request, "contact.html", {'courses': courses})
    courses = QuizCourse.objects.all()
    return render(request, "contact.html", {'courses': courses})

# **************************Logout


@login_required
def logoutuser(request):
    logout(request)
    return render(request, "login.html")
