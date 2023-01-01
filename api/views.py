from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics 
from django.shortcuts import redirect, render
from .models import User
from .forms import UserForm

# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer


def user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass

    else: 
            form = UserForm()
    return render(request, 'index.html', {'form': form})

def show(request):
    user1 = User.objects.all()
    return render(request, 'show.html', {'user1': user1})

def edit(request, id):
    user2 = User.objects.get(id = id) 
    return render(request, 'edit.html', {'user2': user2})

def update(request, id):
    user3 = User.objects.get(id = id)
    form = UserForm(request.POST, instance = user3)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html', {'user3':user3})  
    
def delete(request, id):
    user4 = User.objects.get(id = id)
    user4.delete()
    return redirect('/show')