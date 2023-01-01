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
  path('edit/<int:id>', views.edit),
  path('update/<int:id>', views.update),
  path('delete/<int:id>', views.delete),
]