from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView
from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
  path("get-details",UserDetailAPI.as_view()),
  path('register',RegisterUserAPIView.as_view()),

  path('admin', admin.site.urls),
  path('user', views.user, name = "user"),
  path('show', views.show, name = "show"),
  path('edit/', views.edit),
  path('update/', views.update),
  path('delete/', views.delete),
]