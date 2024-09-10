from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    model = User
    success_url = reverse_lazy('login')

class LoginUserView(LoginView):
    template_name = 'registration/login.html'

class LogoutUserView(LogoutView):
    template_name = 'registration/logout.html'
    success_url = reverse_lazy('register')

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST , instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = ProfileForm(instance=request.user)
        return render(request, 'registration/profile.html', {'form': form})
    
class BlogView(LoginRequiredMixin, TemplateView):
    template_name = 'blog.html'



    

