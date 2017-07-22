from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from joinus.models import student

def student_panel(request):
    if request.session.get('userid') != None:
        stu_id=request.session['userid']
        data=student.objects.get(id=stu_id)
        args={'user1':data}
        return render(request,'student/student_panel.html',args)
    else:
        return HttpResponseRedirect('/joinus/login/')

def edit_profile(request):
    if request.session.get('userid')!=None:
        if request.method=='POST':
            student.objects.filter(id=request.session['userid']).update(fname=request.POST.get('fname'),lname=request.POST.get('lname'),uname=request.POST.get('uname'),email=request.POST.get('email'),pic=request.FILES['file1'])
            data = student.objects.get(id=request.session['userid'])
            args = {'user1': data,'message':'success'}
            return render(request,'student/edit_profile.html',args)
        else:
            data = student.objects.get(id=request.session['userid'])
            args = {'user1': data}
            return render(request, 'student/edit_profile.html', args)
    else:
        return HttpResponseRedirect('/joinus/login/')

def change_password(request):
    if request.session.get('userid') != None:
        if request.method=='POST':
            data = student.objects.get(id=request.session['userid'])
            if request.POST.get('password')==data.password:
                if request.POST.get('newpassword')==request.POST.get('renewpassword'):
                    student.objects.filter(id=request.session['userid']).update(password=request.POST.get('newpassword'))
                    args = {'user1': data, 'message1': 'Password Change Successfully !!'}
                    return render(request, 'student/change_password.html', args)
                else:
                    args = {'user1': data,'message':'New and Retype Password are not same !!'}
                    return render(request,'student/change_password.html',args)
            else:
                args = {'user1': data, 'message': 'Current Password is wrong !!'}
                return render(request, 'student/change_password.html', args)
        else:
            data = student.objects.get(id=request.session['userid'])
            args = {'user1': data}
            return render(request, 'student/change_password.html', args)
    else:
        return HttpResponseRedirect('/joinus/login/')