from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    studentname = models.CharField(max_length=100)
    age = models.IntegerField()


class Course(models.Model):
    coursename = models.CharField(max_length=100)
    description = models.TextField()


class ProductList(models.Model):
    productname = models.CharField(max_length=100)
    producttype = models.CharField(max_length=100)


"""
from django.db import models


class Myuser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)


class Student(models.Model):
    studentname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=False, blank=False)


class Course(models.Model):
    coursename = models.CharField(max_length=100)
    description = models.TextField()


class Registration(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)


class ProductList(models.Model):
    productname = models.CharField(max_length=100)
    producttype = models.TextField(max_length=100)
"""
