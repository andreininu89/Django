from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm


def get_form_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            print("VALIDATION SUCCESSFUL")
            print("NAME:", form.cleaned_data["name"])
            print("EMAIL:", form.cleaned_data["email"])
            print("VEMAIL:", form.cleaned_data["verify_email"])
            print("text:", form.cleaned_data["text"])
            # redirect to a new URL:
            return HttpResponseRedirect("/form_page/")
        else:
            print("VALIDATION FAILED")
            return render(request, "basicapp/form_page.html", {"form": form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "basicapp/form_page.html", {"form": form})


def index(request):
    return render(request, "basicapp/index.html")
