from django import forms

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
