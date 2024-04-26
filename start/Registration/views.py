from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from .models import Myuser, Student


# from .forms import CourseForm  # Assuming you have a CourseForm defined in forms.py
# from .models import Course  # Assuming you have a Course model defined in models.py


def create_course(request):
    if request.method == 'POST':
        # Process the form data
        course_name = request.POST.get('course_name')  # Assuming 'course_name' is the name of the input field
        # You can retrieve other form fields similarly

        # Here you can perform any additional processing or validation before saving

        # Save the course data (You should replace this with your actual save logic)
        # For example, you might save it to a database model
        # Example: Course.objects.create(course_name=course_name)

        # After saving, you can redirect to a success page or another view
        return redirect('course_list')  # Redirect to the URL name for your course list view
    else:
        # If it's a GET request, render the empty form
        return render(request, 'create_course.html')


def registration(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())


def mypage(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def courses(request):
    template = loader.get_template('courses.html')
    return HttpResponse(template.render())


def login(request):
    if request.method == 'POST':
        # Assuming you have a form with 'username' and 'password' fields
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Here you would validate the username and password, and authenticate the user
        # For simplicity, let's assume the user is authenticated

        # Redirect the user to the dashboard page after successful login
        return redirect('dashboard')

    return render(request, 'login.html')


def dashboard(request):
    data = Student.objects.all();
    context = {'data': data}
    return render(request, 'dashboard.html', context)


def coursedash(request, template):
    template = loader.get_template('coursedash.html')
    return HttpResponse(template.render())


def success(request):
    # Your view logic goes here
    return render(request, 'success.html')


def dashbase(request):
    template = loader.get_template('dashbase.html')
    return HttpResponse(template.render())


# @csrf_protect

@csrf_exempt
def adduser(request):
    template = loader.get_template('login.html')
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mydata = {'name': name, 'email': email, 'password': password}
        print(mydata)
        query = Myuser(username=name, email=email, password=password)
        query.save()
    return HttpResponse(template.render())


def addstudent(request):
    if request.method == 'POST':
        name = request.POST.get('studname')
        email = request.POST.get('studmail')
        password = request.POST.get('password')
        age = request.POST.get('studage')
        obj1 = Student(studentname=name, email=email, password=password, age=age)
        obj1.save()

    # fetch the student data to be displayed
    data = Student.objects.all();
    context = {'data': data}
    return render(request, 'dashboard.html', context)


def editstudent(request, id):
    data = Student.objects.get(id=id);
    context = {'data': data}
    return render(request, 'updatestudent.html', context)


def updatestudent(request, id):
    if request.method == 'POST':
        name = request.POST.get('studname')
        email = request.POST.get('studmail')
        password = request.POST.get('password')
        age = request.POST.get('studage')


def delstudent(request, id):
    if request.method == 'POST':
        data = Student.objects.get(id=id)
        data.delete()
        return redirect('')
