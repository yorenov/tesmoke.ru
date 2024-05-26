from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('<str:refid>', views.ref_index, name='refindex'),
    # path('referral_index', views.referral_index, name='referral_index'),
    path('adminka', views.add_referral_link, name='add_referral_link'),
    # path('save_stats_data/<str:social_network>/<str:refid>/<str:url>', views.save_stats_data, name='save_stats_data'),
    path('save_stats_data', views.save_stats_data, name='save_stats_data'),
]
