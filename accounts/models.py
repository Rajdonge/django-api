from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
import uuid


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)
    

class User(AbstractUser):
    username = None
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    verification_otp = models.CharField(max_length=10)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class SocialMedia(models.Model):
    facebook = models.CharField(max_length=255)
    github = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Social Media Links - {self.created_at}"

class Banner(models.Model):
    banner = models.ImageField(upload_to='banner/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Banner Image - {self.created_at}"


class CV(models.Model):
    cv = models.FileField(upload_to='cv/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CV - {self.created_at}"


class Logo(models.Model):
    logo_image = models.ImageField(upload_to='logo/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Logo {self.id}"

class Project(models.Model):
    project_title = models.CharField(max_length=100)
    project_image = models.ImageField(upload_to='project_image/')
    project_description = models.TextField()

class Enquiry(models.Model):
    visitor_name = models.CharField(max_length=255)
    visitor_email = models.CharField(max_length=255)
    visitor_message = models.TextField()