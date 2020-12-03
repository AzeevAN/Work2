from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Item


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = "new_item.html"
    fields = ("title", "price", "amount", 'date')

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Singleton pattern
        return super().form_valid(form)

#   PostDeleteView
# Create your views here.
class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = "list_items.html"
    context_object_name = "items"

class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = "detail_item.html"
    context_object_name = "item"

class ItemEditView(LoginRequiredMixin, UpdateView):
    model = Item
    template_name = "edit_item.html"
    fields = ("title", "amount", "price")
    context_object_name = "item"

class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = "delete_item.html"
    success_url = reverse_lazy("list_posts")