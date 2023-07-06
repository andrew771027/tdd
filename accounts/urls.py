from django.urls import path
from accounts import views

urlpatterns = [
    path('login', views.personal_login, name='personal_login'),
    path('logout', views.logout, {'next_page': '/'}, name='logout'),
]
