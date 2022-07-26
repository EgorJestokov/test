from django.urls import path
from. import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name="logout"),
    path('registration/', views.register, name='registration'),
    path('manual/', views.manual, name='manual'),
    path('reports/', views.reports, name='reports'),

]