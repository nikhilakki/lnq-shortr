# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
from django.urls import path
from . import views

urlpatterns = [
    path("signin/", view=views.signin, name="SignIn Page"),
    path("", view=views.landing, name="Landing_Page"),
]
