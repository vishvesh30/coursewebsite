from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from joinus.models import student
import os


def home(request):

        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('pass')
            users = student.objects.all()
            for user in users:
                if password == user.password and email == user.email:
                    request.session['userid']=user.pk
                    args={'user1':user}
                    return render(request, 'home/home.html',args)
        else:
            if request.session.get('userid') != None:
                user=student.objects.get(id=request.session['userid'])
                args = {'user1': user}
                return render(request, 'home/home.html', args)
        #if not user.exists():
        #    return render(request, 'joinus/login.html')
            else:
                return HttpResponseRedirect('/joinus/login/')