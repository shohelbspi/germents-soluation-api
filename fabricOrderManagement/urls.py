from django.urls import path
from fabricOrderManagement import views


urlpatterns = [
        path('create/', views.FabricOrderCreateView.as_view(), name='fabric-order-create'),
        path('', views.FabricOrderListView.as_view(), name='fabric-order-index'),

]
