from django.urls import path
from .views import TaskListView, IndexTemplateView, CategoriView, TaskDetailView, create_task, create_category
from django.views.generic import TemplateView

app_name = "todo"
urlpatterns = [
    path('newtask/', create_task, name='task_new'),
    path('tasklist/', TaskListView.as_view(), name='tasklist'),
    path('category/', CategoriView.as_view(), name='category'),
    path('newcategory/',create_category, name='new_category'),
    path('<slug:pk>/', TaskDetailView.as_view(), name='taskdetail'),

]
