from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        user = authenticate(username=request.POST.get('username'), 
                            password=request.POST.get('password'))
        if user is None:
            return redirect('login')            ## using name of url
        login(request, user)
        return redirect('/')

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('/')                ## using name of url