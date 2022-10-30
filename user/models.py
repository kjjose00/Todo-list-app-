from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

class Todos(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=False,null=False)
    text=models.TextField()