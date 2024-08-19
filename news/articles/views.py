from django.forms.models import BaseModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from . import models

class ArticleListView(LoginRequiredMixin, ListView):
    model=models.Article
    template_name='article_list.html'
    login_url='login'
class ArticleDetailView(LoginRequiredMixin, DetailView):
    model= models.Article
    template_name='article_detail.html'
    login_url='login'
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model= models.Article
    fields=['title', 'body', ]
    template_name='article_edit.html'
    login_url='login'
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model= models.Article
    success_url=reverse_lazy('article_list')
    template_name='article_delete.html'
    login_url='login'
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model=models.Article
    template_name='article_new.html'
    fields=['title', 'body']
    login_url='login'

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
class CommentCreateView(LoginRequiredMixin, CreateView):
    model=models.Comment
    template_name='comment_new.html'
    success_url=reverse_lazy('article_list')
    fields=['comment']
    login_url='login'

    def form_valid(self, form):
        form.instance.author=self.request.user
        article_id = self.kwargs.get('pk')
        article =models.Article.objects.get(id=article_id)
        
        # Устанавливаем статью для комментария
        form.instance.article = article
        
        return super().form_valid(form)
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model=models.Comment
    success_url=reverse_lazy('article_list')
    template_name='comment_delete.html'
    login_url='login'
