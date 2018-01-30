import requests
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
import json
from django.conf import settings
from .models import UserData


def index(request):
    if request.method == 'GET':
        return render(request, 'client/index.html')
    if request.method == 'POST':
        redirect_url = 'http://localhost:8080/web/authorize/?response_type=code&client_id=%s' \
                       '&redirect_uri=http://127.0.0.1:8070/client/hello&state=somestate' % \
                       settings.CLIENT_ID
        return redirect(redirect_url)


def hello(request):
    code = request.GET.get('code')
    auth_url = 'http://localhost:8080/api/v1/tokens/'
    arguments = {
        'grant_type': 'authorization_code',
        'client_id': settings.CLIENT_ID,
        'client_secret': settings.CLIENT_SECRET,
        'code': code,
    }
    response = requests.post(auth_url, data=arguments)
    json_data = json.loads(response.text)
    print(response.text)
    user = UserData(id=json_data['id'],
                    authorization_code=code,
                    access_token=json_data['access_token'],
                    refresh_token=json_data['refresh_token'],
                    expires_in=json_data['expires_in'],
                    token_type=json_data['token_type'],
                    info=json_data['scope'])
    user.save()

    context = {
        'id': json_data['id'],
        'result': json_data,
    }

    return render(request, 'client/hello.html', context)
