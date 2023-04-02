from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager

import os
from uuid import uuid4

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()


class Application(models.Model):
    applicant_name = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    approval = models.BooleanField(default=False)

    def __str__(self):
        return self.applicant_name

class School(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid4().hex}.{ext}"
    return os.path.join('uploads', filename)

class Document(models.Model):
    document_name = models.CharField(max_length=100)
    uploaded_by = models.CharField(max_length=100)
    uploaded_date = models.DateField()
    document_file = models.FileField(upload_to=get_file_path)
    approval = models.BooleanField(default=False)

    def __str__(self):
        return self.document_name

class DocumentFile(models.Model):
    name = models.CharField(max_length=40)
    document_image = models.ImageField(upload_to='image/',null=True,blank=True)
    description=models.CharField(max_length=40)
    def __str__(self):
        return self.name