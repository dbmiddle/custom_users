from django.shortcuts import render
from custom_users.models import MyUser
from django.shortcuts import reverse
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from utm_custom_users import settings
from custom_users.forms import SignupForm
from custom_users.forms import LoginForm

# Create your views here.


@login_required
def index(request):
    data = request.user.display_name
    usermodel = settings.AUTH_USER_MODEL
    return render(request, 'index.html', {'data': data, 'usermodel': usermodel})


def signup(request):
    html = 'signup_form.html'

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            newuser_ = MyUser.objects.create_user(
                data['username'], data['password1']
            )
            login(request, newuser_)
            return HttpResponseRedirect(reverse('homepage'))

    form = SignupForm()
    return render(request, html, {'form': form})


def loginview(request):
    html = 'login_form.html'

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                    )

    form = LoginForm()

    return render(request, html, {'form': form})


def logoutview(request):
    if request.method == 'GET':
        logout(request)

    return HttpResponseRedirect(reverse('login'))
