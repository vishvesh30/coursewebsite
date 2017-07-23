from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import post
# Create your views here.
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        data=request.POST.get('data')
        date=request.POST.get('date')
        post_object = post(title=title,data=data,date=date)
        post_object.save()
        return render(request, 'form.html', {'message': 'success'})
    else:
        return render(request, 'form.html')