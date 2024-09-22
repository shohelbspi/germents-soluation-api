from django.urls import path
from masterdata import views

urlpatterns = [
    # using function base api view
    path('buyers/',views.buyer_list_create,name='buyer_list_create'),
    path('buyer/<int:id>/',views.buyer_show_edit_delete,name='buyer_show_edit_delete'),

    # using class base api view
    path('machine-types/',views.MachineTypeListCreateView.as_view(),name='machine_list_create'),
    path('machine-type/<int:id>/',views.MachineTypeShowEditDeleteView.as_view(),name='machinetype_show_edit_delete')
]
