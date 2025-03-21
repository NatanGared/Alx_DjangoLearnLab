from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

class HomeView():
    template_name = 'base.html'

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('post-list')  # Redirect to post list after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post-list')
        else:
            return render(request, 'blog/login.html', {'error': 'Invalid credentials'})
    return render(request, 'blog/login.html')

def user_logout(request):
    logout(request)
    return redirect('post-list')

@login_required
def profile(request):
    if request.method == 'POST':
        request.user.email = request.POST['email']
        request.user.save()
        return redirect('profile')  # Redirect to the profile page after update
    return render(request, 'blog/profile.html')

# blog/views.py
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm

# List all blog posts
class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

# Show details of a single blog post
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# Create a new blog post
class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)

# Update an existing blog post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only the author can edit the post

# Delete a blog post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/posts/'  # Redirect to the list view after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only the author can delete the post
    

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView
from .models import Post, Comment
from .forms import CommentForm
from django.urls import reverse_lazy

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=post.pk)

        return self.render_to_response(self.get_context_data(comment_form=comment_form))

class CommentCreateView(CreateView):
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    success_url = reverse_lazy('post-detail')  # Redirect after creating a comment

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        return super().form_valid(form)

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    success_url = reverse_lazy('post-detail')  # Redirect after updating a comment

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentDeleteView(View):
    @login_required
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)

        if request.user == comment.author:
            post_pk = comment.post.pk
            comment.delete()
            return redirect('post-detail', pk=post_pk)

        return redirect('post-detail', pk=comment.post.pk)