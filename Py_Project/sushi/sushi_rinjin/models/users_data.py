from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models.signals import post_save
from django.dispatch import receiver


class UsersDataProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #user_name = models.CharField(max_length=50, unique=True)
    tel = models.CharField(max_length=25, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         UsersDataProfile.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.usersdataprofile.save()

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            UsersDataProfile.objects.create(user=instance)
        instance.usersdataprofile.save()


# class UsersProfileForm(ModelForm):
#     class Meta:
#         model = UsersDataProfile
#         fields = ['tel', 'address']
#         #users = User.objects.all().select_related('UsersProfileForm')


class UserForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    tel = forms.CharField(max_length=25, required=True)
    address = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name',
                  'last_name', 'tel', 'address')
