from django.urls import path
from .views import ItemEditView, ItemCreateView, ItemListView, ItemDeleteView, ItemDetailView

urlpatterns = [
    path("", ItemListView.as_view(), name="list_items"),
    path("new/", ItemCreateView.as_view(), name="new_item"),
    path("<int:pk>/edit/", ItemEditView.as_view(), name="edit_item"),
    path("<int:pk>/detail/", ItemDetailView.as_view(), name="detail_item"),
    path("<int:pk>/delete/", ItemDeleteView.as_view(), name="delete_item")
]