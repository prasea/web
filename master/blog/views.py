from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# posts = [
#     {
#         'title' : 'Post 1',
#         'author' : 'Jack',
#         'date_posted' : 'Jan 6, 2020',
#         'content' : 'We will we will Rock You'
#     },
#      {
#         'title' : 'Post 2',
#         'author' : 'John Doe',
#         'date_posted' : 'Jan 7, 2020',
#         'content' : 'We will we will Make You'
#     }
# ]
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
                              
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
def home(request):
    # context_dictionary = {'postss': posts}
    context_dictionary = {'postss': Post.objects.all()}

    return render(request, 'blog/home.html', context_dictionary)
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'postss'
    ordering = ['-date_posted']
class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    fields = ['title', 'content']
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})