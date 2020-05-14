from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, username=None, password = None, is_active =True, is_staff = False, is_admin = False):
        if not email:
            raise ValueError("User must have an Email address")
        if not password:
            raise ValueError("User must have a password")

        user_obj = self.model(
            email = self.normalize_email(email),
            username=username
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using = self._db)
        return user_obj
    def create_staffuser(self, email,username=None, password = None):
        user = self.create_user(
            email,
            username=username,
            password = password,
            is_staff = True
        )
        return user

    def create_superuser(self, email, username=None, password = None):
        user = self.create_user(
            email,
            username=username,
            password = password,
            is_staff = True,
            is_admin=True
        )
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=250, unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.username:
            return self.username
        return self.email

    def get_short_name(self):
        return self.username

    def has_perm(self,perm,obj = None):
        return True
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active


class GuestEmail(models.Model):
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
