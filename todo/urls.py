from django.urls.conf import path
from todo.views import todo_list

app_name='todos'

urlpatterns = [
    path('',todo_list),
]
