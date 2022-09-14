import os.path

from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.views.generic.list import ListView
from django.conf import settings
from .models import FileAdmin
from .registration import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Task


# Create your views here.
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return ("main:home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})

class TaskList(ListView):
	model = Task
	context_object_name = 'tasks'


def home(request):
    context={'file':FileAdmin.objects.all()}
    return render(request,'wesite/home.html',context)


def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(),content_type="application/adminupload")
            response['content-Dispositon']='inline;filename='+os.path.basename(file_path)
            return response

    raise Http404