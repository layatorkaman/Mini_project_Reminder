from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils.timesince import timeuntil

from .models import Task, CategoryTask
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from .forms import TaskForm, CategoryTaskForm


# Create your views here.


class TaskListView(ListView):
    model = Task
    template_name = 'tasklist.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        try:
            context["exp_task"] = Task.objects.expire_task()
        except Task.DoesNotExist:
            context["exp_task"] = None
        return context


class TaskDetailView(DetailView):
    model = Task
    template_name = 'taskdetail.html'


class CategoriView(ListView):
    model = Task
    template_name = 'Category.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super(CategoriView, self).get_context_data(**kwargs)
        try:
            context["emp_cat"] = CategoryTask.objects.empty_cat()
            context['full_cat']= CategoryTask.objects.Full_cat()
        except Task.DoesNotExist:
            context["emp_cat"] = None

        return context






class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_new.html'
    fields = ['title', 'description', 'pority', 'category', 'expire_date']


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'task_new.html', {'form': form})
    else:
        form = TaskForm()

    return render(request, 'task_new.html', {'form': form})


def create_category(request):
    if request.method == 'POST':
        form = CategoryTaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo/')
        else:
            return render(request, 'Category.html', {'form': form})
    else:
        form = CategoryTaskForm()

    return render(request, 'Category.html', {'form': form})
