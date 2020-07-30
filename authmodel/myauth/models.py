from django.db import models
from django.contrib.auth.models import AbstractBaseUser  , BaseUserManager
# Create your models here.
from rest_framework.authtoken.models import Token
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# create a user manager..


GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

TITLE = (
    ('Miss', 'Miss'),
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
)

class MyUserManager(BaseUserManager):
    def create_user(self , email ,password = None , **extra_fields):
        #cretae a normal user and save them

        # set super user to false
        extra_fields.setdefault('is_admin' , False)

        if not email:
            raise ValueError("Email must be available")
        email = self.normalize_email(email)
        user = self.model(email = email , **extra_fields)
        user.set_password(password)
        user.save(self._db)
        return user



             # create a super user and save it
    def create_superuser(self , email , password , **extra_fields):
        extra_fields.setdefault('is_admin' , True)
        extra_fields.setdefault('is_staff' , True)

        # check if not super user
        if extra_fields.get('is_admin') is not True:
            raise ValueError("You must be an admin")
        #
        # def has_module_perms(self):
        #     return True
        # then we create the user as superuser
        return self.create_user(email , password , **extra_fields)






#create the BaseUserManager

class myBaseUser(AbstractBaseUser):
    is_staff = models.BooleanField(default = False)
    is_admin = models.BooleanField(default = False)
    title = models.CharField(max_length = 255 , choices = TITLE , null = False , blank = False)
    name = models.CharField(max_length = 255 , blank = False , null= False)
    gender = models.CharField(max_length = 255 , choices = GENDER , null = False , blank = False)
    phone = models.CharField(max_length = 255 , blank = False , null= False)
    email = models.CharField(max_length=255 , unique = True , null = False)
    username = models.CharField(max_length = 255 , unique = False)


    objects = MyUserManager()

    USERNAME_FIELD = 'email'
