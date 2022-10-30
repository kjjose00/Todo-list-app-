

from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.LoginView, name='login'),
    path('register/',views.RegisterView.as_view(), name='register'),
    path('logout/',views.logout_user,name='logout'),
    path('create/',views.create_todo,name='create'),
    path('del/<int:id>/',views.delete_todo,name='delete_todo'),
    path('edit/',views.save_edited,name='save_edited'),
    
]
