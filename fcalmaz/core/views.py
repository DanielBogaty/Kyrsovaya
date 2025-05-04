from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404

from .utils import DataMixin
from .models import News


class HomePage(DataMixin, ListView):
    template_name = 'core/home.html'
    title_page = 'Главная страница'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)


class ShowNews(DataMixin, DetailView):
    template_name = 'core/news.html'
    context_object_name = 'news'
    slug_url_kwarg = 'news_slug'

    def get_object(self, queryset = None):
        return get_object_or_404(News.objects.all(), slug=self.kwargs[self.slug_url_kwarg])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['news'].title)
    

class AboutClub(DataMixin, TemplateView):
    template_name = 'core/about.html'
    title_page = 'История клуба'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)
    

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")