from django.shortcuts import render, redirect
# from .forms import AuthorForm
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from post.models import Post
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


def register(request):
    if request.method == 'POST':
        registerForm = forms.RegistrationForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            messages.success(request, 'Acount is created!! NICE!!')
            return redirect('register')

    else:
        registerForm = forms.RegistrationForm()
    return render(request, 'register.html', {'form': registerForm, 'type': 'Register'})


class UserLoginView(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('profile')

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Acount is logged In!! Ola Amigo!!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(
            self.request, 'Buddy!! Login information is not correct')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context


@login_required
def profile(request):
    data = Post.objects.filter(account=request.user)
    return render(request, 'profile.html', {'data': data})


@login_required
def editProfile(request):
    if request.method == 'POST':
        profileForm = forms.changeUserForm(request.POST, instance=request.user)
        if profileForm.is_valid():
            profileForm.save()
            messages.success(request, 'Profile is Updated!! NICE!!')
            return redirect('profile')

    else:
        profileForm = forms.changeUserForm(instance=request.user)
    return render(request, 'updateProfile.html', {'form': profileForm})


def passChange(request):
    if request.method == 'POST':
        Form = PasswordChangeForm(request.user, data=request.POST)
        if Form.is_valid():
            Form.save()
            messages.success(
                request, 'Password updated successfully!! be careful next time!')
            update_session_auth_hash(request, Form.user)
            return redirect('profile')

    else:
        Form = PasswordChangeForm(user=request.user)
    return render(request, 'passChange.html', {'form': Form})


def userLogout(request):
    logout(request)
    return redirect('userLogin')
