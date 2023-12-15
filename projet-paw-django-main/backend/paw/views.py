from django.views.generic.base import TemplateView

from .models import Task

from django import forms

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout

class AboutView( TemplateView):
    template_name = 'about.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['user'] = self.request.user
        return context

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','user']

class TasksView(TemplateView):
	template_name = 'list.html'
	def get_context_data(self,*args, **kwargs):
		context = super(TasksView, self).get_context_data(*args,**kwargs)
		context['tasks'] = Task.objects.all()
		return context
        
class TasksStat(TemplateView):
    template_name = 'account.html'
    def get_context_data(self, *args, **kwargs):
        context = super(TasksStat, self).get_context_data(*args, **kwargs)
        total_tasks = Task.objects.count()
        completed_tasks = Task.objects.filter(state=True).count()
        #deleted_tasks = Task.objects.filter(deleted=True).count()
        if total_tasks > 0:
            completion_percentage = (completed_tasks / total_tasks) * 100
        else:
            completion_percentage = 0
        print("here's yours completed tasks",  completed_tasks)
        context['completion_percentage'] = completion_percentage
        context['completed_tasks'] = completed_tasks
        #context['deleted_tasks'] = deleted_tasks
        return context
      
class IndexView(TemplateView):
	template_name = 'index.html'
     
class AccountView(TemplateView):
	template_name =  'account.html'
     
class CalendarView(TemplateView):
	template_name =  'calendar.html'

class MotivationView(TemplateView):
	template_name =  'motivation.html'



def auth_view(request):
    context = {'register_errors': None, 'login_errors': None}
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'register':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if User.objects.filter(username=username).exists():
                context['register_errors'] = 'Username already taken'
                return render(request, 'index.html', context)
            
            if password != password2:
                context['register_errors'] = 'passwords are not identicals'
                return render(request, 'index.html', context)

            user = User.objects.create_user(username, email, password)
            user.save()
            login(request, user)
            return redirect('about')  # Redirect after registration

        elif action == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('about')  # Redirect after login
            else:
                context['login_errors'] = 'Invalid username or password'
                return render(request, 'index.html', context)

    return render(request, 'index.html', context)

     
def user_logout(request):
    logout(request)  # Log out the user
    return redirect('auth_view') 

def completion_pourcentage(request):
    context = {'completion_percentage': request.completion_percentage}
    return render(request, 'account.html', context)

def supp(request):
    context = {'deleted_tasks': request.deleted_tasks}
    return render(request, 'account.html', context)

def complet(request):
    context = {'completed_taskse': request.completed_tasks}
    return render(request, 'account.html', context)
        



	
	

		
	
