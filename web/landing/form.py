# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from django import forms
from .models import URL


class ShortenURL(forms.ModelForm):
    class Meta:
        model = URL
        fields = ("long_url",)

    long_url = forms.CharField()
