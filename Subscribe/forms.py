from django import forms
from django.forms import ModelForm

from .models import MailDetail

"""
class MailForm(forms.Form):
    email = forms.CharField(label='Your Mail', max_length=100)

    def clean(self):
        cleaned_data = super().clean()
        mail = cleaned_data.get('email')

        with open("maillist.txt") as myFile:
            for line in myFile:
                line = line.rstrip()
                if mail == line:
                    raise forms.ValidationError(
                    "You have already Subscribed, Thanks"
                )

        myFile.close()
"""

class MailForm(ModelForm):
    class Meta:
        model = MailDetail
        fields = ('email',)

    def clean(self):
        cleaned_data = super().clean()
        mail = cleaned_data.get('email')
        is_given = MailDetail.objects.filter(email=mail)
        if is_given.count() != 0:
            raise forms.ValidationError(
                    "You have already Subscribed, Thanks"
                )
