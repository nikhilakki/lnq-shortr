# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
from django.urls import path
from . import views

urlpatterns = [
    path("tos", view=views.tos, name="TOS Page"),
    path("privacy", view=views.privacy, name="Privacy Page"),
    path("signin", view=views.signin, name="SignIn Page"),
    path("", view=views.landing, name="Home"),
]
