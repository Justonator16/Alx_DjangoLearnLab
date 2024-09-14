from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView, DeleteView , ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ProfileForm, PostForm, CommentForm
from .models import Post, Comment
from django.db.models import Q

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
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')


# class LogoutUserView(LogoutView):
#     template_name = 'blog/logout.html'
#     next_page = reverse_lazy('login')

#     def get_template_names(self) -> list[str]:
#         return super().get_template_names()

def LogoutUserView(request):
    auth.logout(request)
    return redirect('login')

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

# CRUD OPERATIONS Posts
# Create Posts
class PostCreateView( LoginRequiredMixin ,CreateView):
    form_class = PostForm
    model = Post
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('post_list')


# Read Posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# Update a Post
class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('post_list')

    def test_func(self) -> bool | None:
        return self.request.user.is_active

# Delete a Post
class PostDeleteview(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'blog/post_delete.html'
    context_object_name = 'post'

    def test_func(self) -> bool | None:
        return self.request.user.is_active

# CRUD OPERATIONS FOR Comment Model
# Create
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'blog/comment_create.html'
    form_class = CommentForm
    context_object_name = 'forms'
    success_url = reverse_lazy('comment_list')

# Read
class CommentListView(ListView):
    model = Comment
    template_name = 'blog/comment_list.html'
    context_object_name = 'comments'

# Update
class CommentUpdateView(UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_update.html'
    context_object_name = 'comment'
    success_url = reverse_lazy('comment_list')

    def test_func(self) -> bool | None:
        return self.request.user.is_authenticated

class CommentDetailView(DetailView):
    model = Comment
    template_name = 'blog/comment_detail.html'
    context_object_name = 'comment'

# Delete
class CommentDeleteView(UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_delete.html'
    context_object_name = 'comment'
    success_url = reverse_lazy('comment_list')

    def test_func(self) -> bool | None:
        return self.request.user.is_authenticated
    
def post_search(request):
    query = request.GET.get('q')
    results = Post.objects.filter(
        Q(title__icontains=query) | 
        Q(content__icontains=query) | 
        Q(tags__name__icontains=query)
    ).distinct()
    return render(request, 'blog/search_results.html', {'posts': results, 'query': query})

def posts_by_tag(request, tag_name):
    posts = Post.objects.filter(tags__name=tag_name)
    return render(request, 'blog/posts_by_tag.html', {'posts': posts, 'tag_name': tag_name})



    






    

