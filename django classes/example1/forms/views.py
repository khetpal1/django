from django.shortcuts import render, HttpResponse

# Create your views here.
from .forms import userregistration

def contact(request):
    return HttpResponse("hello")


def getuser(request):
    if request.method == 'POST':
        user = userregistration(request.POST)
        if user.is_valid():
            name = user.cleaned_data['name']
            email = user.cleaned_data['email']
            password=user.cleaned_data['password']
            rpassword=user.cleaned_data['rpassword']
            print(password)
            print(rpassword)

        # return render(request, 'message.html', {"name": name})
    else:
        user = userregistration()

    return render(request, 'form.html', {"user": user})
