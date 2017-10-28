from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from sushi_rinjin.models.users_data import UserForm


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # load the profile instance created by the signal
            user.refresh_from_db()
            user.usersdataprofile.tel = form.cleaned_data.get('tel')
            user.usersdataprofile.address = form.cleaned_data.get('address')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/sushi_rinjin/')
        else:
            messages.error(request, 'Form not valid',
                           extra_tags='valid_error')
            return render(request, 'sushi_rinjin/registration/sign_up.html',
                  {'form': form})
    else:
        form = UserForm()
    return render(request, 'sushi_rinjin/registration/sign_up.html',
                  {'form': form})
