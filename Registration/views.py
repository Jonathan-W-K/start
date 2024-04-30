from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import UserRegistrationForm
from .models import User, Student
from .serializers import ProductSerializer
from .models import ProductList


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = ProductList.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


def product_list_view(request):
    products = ProductList.objects.all() # retrieve all instances of products from database
    context = {'products': products}
    return render(request, 'product_list.html', context)


def create_course(request):
    if request.method == 'POST':
        # Process the form data
        course_name = request.POST.get('course_name')
        # Your processing logic goes here

        # Redirect to the course list page
        return redirect('course_list')
    else:
        # If it's a GET request, render the empty form
        return render(request, 'create_course.html')


def registration(request):
    return render(request, 'register.html')


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
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data into the database
            return redirect('dashboard')  # Redirect back to the dashboard

    else:
        form = UserRegistrationForm()
    context = {'form': form}
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


@csrf_exempt
def adduser(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create a new User object and save it to the database
        User.objects.create(username=name, email=email, password=password)

        return redirect('dashboard')  # Redirect to the dashboard after successfully adding user
    else:
        return render(request, 'login.html')


def editstudent(request, id):
    data = Student.objects.get(id=id)
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
        return redirect(request, 'confirm_delete')


def student_list(request, id):
    data = Student.objects.all()
    context = {'data': data}
    return render(request, 'product_table.html', context)


def edituser(request):
    data = Student.objects.get()
    context = {'data': data}
    return render(request, 'dashboard.html')


def add_user(request):
    if request.method == 'POST':
        # Process the form data
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Assuming you have a dashboard view
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'register.html', context)
