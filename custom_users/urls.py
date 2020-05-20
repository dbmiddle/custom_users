from django.urls import path

from custom_users import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('signup/', views.signup),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview)
]
