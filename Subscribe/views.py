from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .forms import MailForm

def get_mail(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            with open("maillist.txt", "a") as myfile:
                myfile.write(form.cleaned_data['email']+"\n")
            myfile.close()
            return HttpResponseRedirect('/thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MailForm()

    return render(request, 'mail.html', {'form': form})

def thanks(request):
	return HttpResponse("<html><head><title>Thanks</title></head><body><h3><center>Thanks</center></h3></body></html>")
