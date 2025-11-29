from django.urls import path

from products.views import CategoryCreateView, CategoryListView, CategoryUpdateView, CategoryDetailView

app_name = "products"

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_add'),
    path('category/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_edit'),
    path('category/<int:pk>/detail/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]