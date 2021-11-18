from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .models import CustomUser
from .forms import CustomUserForm
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse

from rest_framework import generics
from .serializers import *
from .permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.
def all_users(request):
    context = {'users_list': CustomUser.objects.all()}
    return render(request, 'users_list.html', context)


def get_by_id(request, id):
    user = CustomUser.get_by_id(id)
    context = {'user': user}
    return render(request, 'user.html', context)


# def delete_user(request, id):
#     user = CustomUser.objects.get(pk=id)
#     user.delete()
#     return redirect('users_list')

def delete_all_users(request):
    users = CustomUser.objects.all()
    users.delete()
    return redirect('homepage')


class UserCreate(View):
    def get(self, request):
        form = CustomUserForm
        return render(request, 'user_create.html', context={'form': form})

    def post(self, request):
        post_form = CustomUserForm(request.POST)
        if post_form.is_valid():
            new_user = post_form.save()
            return redirect(new_user)
        return render(request, 'user_create.html', context={'form': post_form})


def register(request):
    """Rigister a new user"""
    if request.method != 'POST':
        form = CustomUserForm()
    else:
        form = CustomUserForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(first_name=new_user.first_name,
                                              password=request.POST['password'])
            authenticated_user = form.save()
            login(request, authenticated_user, backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponseRedirect(reverse('users_list'))
    context = {'form': form}
    return render(request, "register.html", context)


def delete_user_by_id(request, id):
    context = {}
    obj = get_object_or_404(CustomUser, pk=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(reverse("users_list"))
    return render(request, "delete_user_by_id.html", context)


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer


class UsersListView(generics.ListAPIView):
    serializer_class = UsersListSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)