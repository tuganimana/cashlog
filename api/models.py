from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    telephone = models.CharField(_('phone'), unique=True,max_length=255)
    isverified = models.CharField(default='No',max_length=255)
    fullname =  models.CharField(max_length=255) 
    email =  models.CharField(max_length=255) 
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    accounttype =models.CharField(default='admin',max_length=255)
    created_at= models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = ['password']

    objects = CustomUserManager()

    def __str__(self):
        return self.telephone