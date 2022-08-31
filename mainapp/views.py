from os import path
from datetime import datetime

from news.parser_news import parser
from random import sample
from json import load

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from mainapp import models as mainapp_models


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
        context['news_qs'] = mainapp_models.News.objects.all()[:5]

        return context


class NewsPageDetailView(TemplateView):
    template_name = 'mainapp/news_detail.html'

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        context['news_object'] = get_object_or_404(mainapp_models.News, pk=pk)

        return context


class CoursesPageView(TemplateView):
    template_name = 'mainapp/courses_list.html'

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = mainapp_models.Courses.objects.all()[:7]

        return context


class CoursesDetailView(TemplateView):
    template_name = "mainapp/courses_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(mainapp_models.Courses, pk=pk)
        context["lessons"] = mainapp_models.Lesson.objects.filter(course=context["course_object"])
        context["teachers"] = mainapp_models.CourseTeachers.objects.filter(course=context["course_object"])

        return context


class ContactsPageView(TemplateView):
    template_name = 'mainapp/contacts.html'


class DocSitePageView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class LoginPageView(TemplateView):
    template_name = 'mainapp/login.html'
