from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('signout/', views.signout),

    path('<int:id>', views.take),

]
urlpatterns += staticfiles_urlpatterns()
