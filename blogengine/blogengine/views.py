from django.shortcuts import redirect, render, reverse
from django.views.generic import View
from django.contrib.auth import views
from django.contrib.auth.models import User


from .forms import *


def redirect_blog(request):
    return redirect('posts_list_url', permanent = True)


class Registration(View):
    def get(self, request):
        form = RegistrationForm
        return render(request, 'registration/signup.html', context={'form': form})


    def post(self, request):
        bound_form = RegistrationForm(request.POST)
        if bound_form.is_valid():
            user = bound_form.clean_all()
            new_user = User.objects.create_user(username = user['nickname'], email = user['email'], password = user['password'])
            new_user.first_name = user['first_name']
            new_user.last_name = user['last_name']
            new_user.save()
            return redirect(reverse('login'))
        return render(request, 'registration/signup.html', context={'form': form})
