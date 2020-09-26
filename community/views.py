from django.shortcuts import render
from django.views.generic import ArchiveIndexView, DetailView, ListView, YearArchiveView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from rest_framework.viewsets import ModelViewSet

@method_decorator(login_required, name = 'dispatch')
class PostListView(ListView):
    model = Post
    paginate_by = 10

post_list = PostListView.as_view()

post_detail = DetailView.as_view(
    model = Post,
    queryset = Post.objects.filter(is_public=True)
)

class PostDetailView(DetailView):
    model = Post
    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'community/post_detail.html', {
        'post' : post,
    })

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.author = self.request.user
        messages.success(self.request, '포스팅을 저장했습니다.')
        return super().form_valid(form)

post_new = PostCreateView.as_view()

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        messages.success(self.request, '포스팅을 수정했습니다.')
        return super().form_valid(form)

post_edit = PostUpdateView.as_view()

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('community:post_list')

    def get_success_url(self):
        return reverse('community:post_list')

post_delete = PostDeleteView.as_view()