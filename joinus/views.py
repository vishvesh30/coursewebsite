from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from joinus import models
from joinus.models import student
from django.core.files.storage import FileSystemStorage



def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname=request.POST.get('lname')
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        password=request.POST.get('pass')
      #  pic=request.POST.get('file1')
        myfile = request.FILES['file1']
      #  fs = FileSystemStorage()
      #  filename = fs.save(myfile.name, myfile)
      #  uploaded_file_url = fs.url(filename)
        student_object=student(fname=fname,lname=lname,uname=uname,email=email,password=password,pic=myfile)
        student_object.save()
        return render(request,'joinus/register.html',{'message':'success'})
    else:
        return render(request,'joinus/register.html')

def login(request):
    if 'userid' in request.session:
        obj = student.objects.get(pk=request.session['userid'])
        args = {  # 'instructor': globals()['loggedin'],
            'user1': obj, }
        return HttpResponseRedirect('/home/',args)
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('pass')
            student_list = student.objects.all()
            for student_data in student_list:
                if password == student_data.password and email == student_data.email:
                    #  globals()['loggedin']=instructor_data
                    request.session['userid'] = student_data.pk
                    obj = student.objects.get(pk=request.session['userid'])
                    args = {'user1': obj}
                    return HttpResponseRedirect('/home/', args)
            return render(request, 'joinus/login.html')
        else:
            return render(request, 'joinus/login.html')

def demo(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')

        users = student.objects.all()
        for user in users:
            if password == user.password and email == user.email:
                args = {'user1': user}
        return render(request, 'home/home.html', args)
        #if not user.exists():
        #    return render(request, 'joinus/login.html')

def signout(request):
    del request.session['userid']
    return HttpResponseRedirect('/joinus/login/')
