from django.urls import path
from . import views

urlpatterns = [
    path('' , views.all_chai , name= "all_home"),
    path('order/' , views.order , name= "order"),
    path('<int:chai_id>/', views.chai_detail, name='chai_details'), # yeha pe hamne chai_id ko url me pass kiya hai taki ham usko views me access kar sakein
    path('chai_stores/', views.chai_store_view, name='chai_stores')
]