from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, UpdateView, DeleteView,  CreateView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib import messages
from .models import Task, TaskImage
from .forms import TaskForm

# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = Task.objects.all() 

        # Filtering by priority
        filter_priority = self.request.GET.get('filter_priority')
        if filter_priority:
            queryset = queryset.filter(priority=filter_priority)

        # Filtering by completion
        filter_completed = self.request.GET.get('filter_completed')
        if filter_completed:
            queryset = queryset.filter(completed=(filter_completed == 'true'))

        # Searching by title
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(Q(title__icontains=search))

        return queryset


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = '/'  

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

# Update Task View
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm  
    template_name = 'task_update.html'
    success_url = reverse_lazy('home')  

# Task Deletion Confirmation View
class TaskDeleteConfirmView(DetailView):
    model = Task
    template_name = 'task_delete_confirm.html'

# Task Deletion View
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete_confirm.html'
    success_url = reverse_lazy('home')

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_create.html'
    success_url = '/' 

    def form_valid(self, form):
        form.instance.user = self.request.user
        task = form.save()

        images = self.request.FILES.getlist('images')
        for image in images:
            TaskImage.objects.create(task=task, image=image)

        messages.success(self.request, 'Task created successfully.')
        return super().form_valid(form)
    

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

# Password Reset Done View
class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

# Password Reset Confirm View
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

# Password Reset Complete View
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'    


