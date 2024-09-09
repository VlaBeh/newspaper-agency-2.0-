from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.forms import RedactorCreationForm, NewsForm, NewspaperSearchForm
from catalog.models import Newspaper, Redactor, Topic


@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_newspapers = Newspaper.objects.count()
    num_redactors = Redactor.objects.count()
    num_topics = Topic.objects.count()
    context = {
        "num_newspapers": num_newspapers,
        "num_redactors": num_redactors,
        "num_topics": num_topics,
    }
    return render(request, "catalog/index.html", context=context)


class TopicFormatListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    template_name = "catalog/topic_list.html"
    context_object_name = "topic_list"
    paginate_by = 10


class TopicFormatCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("catalog:topic-list")
    template_name = "catalog/topic_form.html"


class TopicFormatUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("catalog:topic-list")
    template_name = "catalog/topic_form.html"


class TopicFormatDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Topic
    template_name = "catalog/topic_form_config_delete.html"
    success_url = reverse_lazy("catalog:topic-list")


class NewspaperFormatListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    template_name = "catalog/newspaper_list.html"
    context_object_name = "newspaper_list"
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspaperFormatListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = NewspaperSearchForm(
            initial={"title": title}
        )
        return context

    def get_queryset(self):
        queryset = Newspaper.objects.select_related("topics")
        title = self.request.GET.get("title")
        if title:
            return queryset.filter(title__icontains=title)
        return queryset


class NewspaperFormatDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class NewspaperFormatCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Newspaper
    form_class = NewsForm
    success_url = reverse_lazy("catalog:newspaper-list")
    template_name = "catalog/newspaper_form.html"


class NewspaperFormatUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Newspaper
    form_class = NewsForm
    success_url = reverse_lazy("catalog:newspaper-list")
    template_name = "catalog/newspaper_form.html"


class NewspaperFormatDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Newspaper
    template_name = "catalog/news_form_config_delete.html"
    success_url = reverse_lazy("catalog:newspaper-list")


class RedactorFormatListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    template_name = "catalog/redactor_list.html"
    context_object_name = "redactor_list"
    paginate_by = 3


class RedactorFormatDetailView(generic.DetailView):
    model = Redactor
    template_name = 'catalog/redactor_detail.html'


class RedactorFormatCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Redactor
    form_class = RedactorCreationForm
    success_url = reverse_lazy("catalog:redactor-list")


class RedactorFormatDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Redactor
    template_name = "catalog/redactor_form_config_delete.html"
    success_url = reverse_lazy("catalog:redactor-list")
