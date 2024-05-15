from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('adminka', views.add_referral_link, name='add_referral_link'),
    path('save_stats_data/', views.save_stats_data, name='save_stats_data'),
]