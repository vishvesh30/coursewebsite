# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from instructor.models import course, coursecontent
from joinus.models import student,instructor
def login(request):
    # if globals()['loggedin'] != "":
    if 'instructorid' in request.session:
        obj = instructor.objects.get(pk=request.session['instructorid'])
        args = {  # 'instructor': globals()['loggedin'],
            'instructor': obj, }
        return render(request, 'instructor/instructor_panel.html', args)
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('pass')
            instructors = instructor.objects.all()
            for instructor_data in instructors:
                if password == instructor_data.password and email == instructor_data.email:
                    #  globals()['loggedin']=instructor_data
                    request.session['instructorid'] = instructor_data.pk
                    obj = instructor.objects.get(pk=request.session['instructorid'])
                    args = {'instructor': obj}
                    return HttpResponseRedirect('/instructor/panel/', args)
            return render(request, 'instructor/instructor_login.html')
        else:
            return render(request, 'instructor/instructor_login.html')

def logout(request):
    del request.session['instructorid']
    return HttpResponseRedirect('/instructor/login/')

def managecourse(request):
    if request.session.get('instructorid') != None:
        obj = instructor.objects.get(pk=request.session['instructorid'])
        args = {
            #'instructor': globals()['loggedin'],
            'instructor': obj, }
        return render(request,'instructor/manage_course.html',args)
    else:
        return HttpResponseRedirect('/instructor/login/')

def instructor_panel(request):
    # if globals()['loggedin']=="":
    if request.session.get('instructorid') != None:
        obj = instructor.objects.get(pk=request.session['instructorid'])
        args = {'user1': obj}
        return render(request, 'instructor/instructor_panel.html', args)
    else:
        return HttpResponseRedirect('/instructor/login/')
def edit_course(request,course_id):
    if request.session.get('instructorid') != None:
        if request.method == 'POST':
            data=course.objects.get(pk=course_id)
            data.cname = request.POST.get('coursename')
            data.taughtby = request.POST.get('taughtby')
            data.prerequisite = request.POST.get('prerequisites')
            data.courselanguage = request.POST.get('courselanguage')
            data.duration = request.POST.get('duration')
            data.fee = request.POST.get('fee')
            data.startdate = request.POST.get('startdate')
            data.save()
            obj = instructor.objects.get(pk=request.session['instructorid'])
            args1 = {
               # 'instructor': request.session['instructorid'],
                'instructor':obj,
                'course': data,
                'message':'success'
            }
            return render(request, 'instructor/edit_course.html', args1)
        else:
            data=course.objects.get(pk=course_id)
            obj = instructor.objects.get(pk=request.session['instructorid'])
            args2={
               # 'instructor': request.session['instructorid'],
                'instructor': obj,
                'course':data,
            }
            return render(request,'instructor/edit_course.html',args2)
    else:
        return HttpResponseRedirect('/instructor/login/')
def create_course(request):
    if request.session.get('instructorid') != None:
        if request.method == 'POST':
            cname=request.POST.get('coursename')
            taughtby=request.POST.get('taughtby')
            prerequisite=request.POST.get('prerequisites')
            courselanguage=request.POST.get('courselanguage')
            duration=request.POST.get('duration')
            fee=request.POST.get('fee')
            startdate=request.POST.get('startdate')
            pic=request.FILES['course_pic']
            data=instructor.objects.get(pk=request.session['instructorid'])
            createdby=data
            courseobject=course(cname=cname,creatorid=createdby,taughtby=taughtby,prerequisite=prerequisite,course_language=courselanguage,duration=duration,fee=fee,start_date=startdate,course_pic=pic)
            courseobject.save()
            course_content=coursecontent.objects.all()
            args = {'instructor': request.session['instructorid'],
                    'message': 'success', 'course_id':courseobject.id, 'course_content':course_content}
            return render(request,'instructor/create_course1.html',args)
        else:
            args = {'instructor': request.session['instructorid']}
            return render(request,'instructor/create_course.html',args)
    else:
        return HttpResponseRedirect('/instructor/login/')
def create_course1(request):
    if request.session.get('instructorid') != None:
        if request.method == 'POST':

            courseid=request.POST.get('course_id')
            data=course.objects.get(pk=courseid)
            type='video'
            seq_no=0
            file='null'
            topic1=request.POST.get('maintopicname')
            if topic1 is not None:
                name=request.POST.get('maintopicname')
                desc=request.POST.get('maintopicdesc')
        #       file='null'
                subid=0
            else:
                name=request.POST.get('subtopicname')
                desc=request.POST.get('subtopicdesc')
                file=request.FILES['content_file']
                subid=request.POST.get('maintopicname1')
                #subid=coursecontent.objects.get(pk=subid1)
            createdby=request.session['instructorid']
            contentobject=coursecontent(course_id=data,content_sub_id=subid,content_name=name,content_description=desc,content_type=type,content_url=file,content_sequence_no=seq_no)
            contentobject.save()
            data=instructor.objects.get(pk=request.session['instructorid'])
            args = {'instructor': request.session['instructorid'],
                    'user1':data,
                    'message': 'success'}
            return render(request,'instructor/instructor_panel.html',args)
        else:
            course_content1=coursecontent.objects.filter(course_id=5,content_sub_id=0)
            course_content=coursecontent.objects.all()
            args = {'instructor': request.session['instructorid'],'course_id':5, 'course_content':course_content1}
            return render(request,'instructor/create_course1.html',args)
    else:
        return HttpResponseRedirect('/instructor/login/')