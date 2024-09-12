from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView, DeleteView , ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ProfileForm, PostForm
from .models import Post

class BlogView(TemplateView):
    template_name = 'blog/blog.html'

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'blog/register.html'
    model = User
    success_url = reverse_lazy('login')
    context_object_name = 'form'

class LoginUserView(LoginView):
    template_name = 'blog/login.html'

class LogoutUserView(LogoutView):
    template_name = 'blog/logout.html'

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST , instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = ProfileForm(instance=request.user)
        return render(request, 'blog/profile.html', {'form': form})

# CRUD OPERATIONS 
# Create Posts
class PostCreateView( LoginRequiredMixin ,CreateView):
    form_class = PostForm
    model = Post
    template_name = 'blog/create.html'
    success_url = reverse_lazy('post_list')


# Read Posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

# Update a Post
class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/update.html'
    success_url = reverse_lazy('post_list')

    def test_func(self) -> bool | None:
        return self.request.user.is_active

# Delete a Post
class PostDeleteview(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'blog/delete.html'
    context_object_name = 'post'

    def test_func(self) -> bool | None:
        return self.request.user.is_active






    

