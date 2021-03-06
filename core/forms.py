from django import forms

# Django: Importing User Model
from django.contrib.auth.models import User

# Models
from .models import UserProfile, Post

from allauth.account.forms import SignupForm

from .validators import username_validator


class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=30, validators=[username_validator])

    class Meta:
        model = User
        fields = ("first_name", "last_name")
        help_texts = {
            "username": "Use your IGN",
            "first_name": "If you want to use your first name you can place it here.",
            "last_name": "If you use your first name, you should also put your last name, so its easier to know what your name really is.",
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name")
        help_texts = {
            "first_name": "If you want to use your first name you can place it here.",
            "last_name": "If you use your first name, you should also put your last name, so its easier to know what your name really is.",
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("avatar", "bio", "platform", "status")
        help_texts = {
            "avatar": "Only images in JPG and PNG are allowed.",
            "bio": "Use this space for text, you have a limit of 140 characters.",
            "platform": "Select the platform on which you play.",
            "status": "If you want to make transactions faster in the Market, you must change your status to Online or In-Game.",
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("text", "image", "video")
        help_texts = {
            "text": "Use this space for text, you have a limit of 280 characters.",
            "image": "Only images in JPG and PNG are allowed.",
            "video": "Copy and paste an URL from the following sites: YouTube.com, Twitch.tv, Vimeo.com or Giphy.com.",
        }