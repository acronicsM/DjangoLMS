from os import path
from datetime import datetime
from news.parser_news import parser
from random import sample
from json import load

from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'mainapp/index.html'


class NewsPageView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):

        def get_news():

            name_file = f'news/json_news/news{datetime.today():%Y%m%d}.json'
            list_news = []

            if not path.exists(name_file):
                parser()

            with open(name_file) as json_file:
                news = load(json_file)['articles']
                for i in sample(range(len(news)), 5):
                    list_news.append(news[i - 1])

            return list_news

        context = super().get_context_data(**kwargs)
        # context['news_title'] = 'Заголовок новости'
        # context['news_preview'] = 'Предварителньое описание новости'
        # context['range'] = range(5)
        # context['data_obj'] = datetime.now
        context['list_news'] = get_news()

        return context


class NewsWithPaginatorView(NewsPageView):

    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context['page_num'] = page

        return context


class CoursesPageView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class ContactsPageView(TemplateView):
    template_name = 'mainapp/contacts.html'


class DocSitePageView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class LoginPageView(TemplateView):
    template_name = 'mainapp/login.html'
