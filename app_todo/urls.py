from django.urls import path
from . import views

app_name = "app_todo"

urlpatterns =[
    path('',views.home,name='home'),
    path('create/', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('del/<int:id>', views.delete, name='del'),
]
