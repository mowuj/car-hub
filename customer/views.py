from django.shortcuts import render,redirect
from .import forms
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import logout,update_session_auth_hash
from django.urls import reverse_lazy
from car.models import Car
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form=forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,"Account Created Successfully")
            return redirect ('user_login')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html',{'form':register_form,'type':'Register'})


class UserLoginView(LoginView):
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, 'Logged in Invalid')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context


@login_required
def profile(request):
    data = Car.objects.filter(user=request.user)
    return render(request,'profile.html',{'data':data})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form=forms.ChangeUserData(request.POST,instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Profile updated Successfully')
            return redirect('profile')
    else:
        profile_form = forms.ChangeUserData(instance=request.user)
    return render(request,'update_profile.html',{'form':profile_form})

def change_pass(request):
    if request.method == 'POST':
        form=PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password changed Successfully')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'change_pass.html',{'form':form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')
