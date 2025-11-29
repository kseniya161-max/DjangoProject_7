from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from products.forms import CategoryForm
from products.models import Category


class CategoryListView(ListView):
    model = Category
    template_name ='category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return super().get_queryset()


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_create.html'
    context_object_name = 'category_add'
    success_url = reverse_lazy('categories_list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_update.html'
    context_object_name = 'category_update'
    success_url = reverse_lazy('categories_list')


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category_detail'



class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_delete.html'
    context_object_name = 'category_delete'
    success_url = reverse_lazy('categories_list')










