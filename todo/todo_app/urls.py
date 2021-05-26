from django.urls import path,include
from .views import test
from .views import todo_detail,todo_list
urlpatterns = [
    path('', todo_list, name="create_retrive"),
    path('<int:pk>/', todo_detail, name="put_del_get")
]

