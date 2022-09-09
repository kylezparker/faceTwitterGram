from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Share



# Create your views here.

class ShareListView(ListView):
    template_name = "friends/list.html"
    model= Share

class ShareDetailView(DetailView):
    template_name = "friends/detail.html"
    model= Share

class ShareCreateView(CreateView):
    template_name = "friends/new.html"
    model= Share
    fields = ["title", "subtitle", "body", "author"]

class ShareUpdateView(UpdateView):
    template_name = "friends/edit.html"
    model= Share
    fields = ["title", "subtitle", "body"]

class ShareDeleteView(DeleteView):
    template_name = "friends/delete.html"
    model= Share
    success_url = reverse_lazy("post_list")