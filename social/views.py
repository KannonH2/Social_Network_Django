from multiprocessing import context
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.base import View
from django.shortcuts import render
from .models import SocialPost


class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        post = SocialPost.objects.get(pk=pk)

        context = {
            'post': post,
        }
        return render(request, 'pages/social/post_detail.html', context)

    def psot(self, request, pk, *args, **kwargs):
        post = SocialPost.objects.get(pk=pk)
        context = {
            'post': post,
        }
        return render(request, 'pages/social/post_detail.html', context)



class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = SocialPost
    fields = ['body']
    template_name = 'pages/social/post_edit.html'

    def get_success_url(self):
        return reverse_lazy('social:post_detail', kwargs={'pk': self.kwargs['pk']})
        

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=SocialPost
    template_name='pages/social/post_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
