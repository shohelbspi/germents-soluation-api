from django.urls import path
from masterdata import views

urlpatterns = [
    # using function base api view
    path('buyers/',views.buyer_list_create,name='buyer_list_create'),
    path('buyer/<int:id>/',views.buyer_show_edit_delete,name='buyer_show_edit_delete'),

    # using class base api view
    path('machine-types/',views.MachineTypeListCreateView.as_view(),name='machine_list_create'),
    path('machine-type/<int:id>/',views.MachineTypeShowEditDeleteView.as_view(),name='machinetype_show_edit_delete'),

    # using genric api view and model mixin
    path('units/',views.UnitListCreateView.as_view(),name='unit_list_create'),
    path('unit/<int:pk>/',views.UnitShowEditDeleteView.as_view(),name='unit_show_edit_delete'),

    path('yarn-counts/',views.YarnCountListView.as_view(),name='yarn_count_list'),
    path('yarn-count/create/',views.YarnCountCreateView.as_view(),name='yarn_count_create'),
    path('yarn-count/<int:pk>/show/',views.YarnCountShowView.as_view(),name="yarn_count_show"),
    path('yarn-count/<int:pk>/update/',views.YarnCountUpdateView.as_view(),name="yarn_count_update"),
    path('yarn-count/<int:pk>/delete/',views.YarnCountDeleteView.as_view(),name="yarn_count_delete"),

    path('yarn-types/',views.YarnTypeListCreateView.as_view(),name='yarntype_list_create'),
    path('yarn-type/<int:pk>/',views.YarnTypeShowUpdateDeleteView.as_view(),name='yarntype_show_edit_delete'),

]
