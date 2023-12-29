from django.urls import path
from . import views
from .views import delete_view, detail_view, list_view, create_view, update_view, calculate_view

urlpatterns = [
    path('expenses/', list_view, name="list" ),
    path('expenses/create', create_view, name="create" ),
    path('expenses/calculate', calculate_view, name="calculate"),
    path('expenses/<id>', detail_view, name="detail" ),
    path('expenses/delete/<id>', delete_view, name="delete" ),
    path('expenses/update/<id>', update_view, name="update" ),
]