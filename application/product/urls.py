from django.urls import path

from application.product.views import ProductListView

urlpatterns = [
    path('product-list/', ProductListView.as_view())
]
