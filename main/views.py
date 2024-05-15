import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_exempt
from .models import StatsData, ReferralLink
from .forms import ReferralLinkForm

def index(request):
    return render(request, 'main/index.html')

def is_admin(user):
    return user.is_superuser

def dynamic_page(request, text):
    return render(request, 'main/index.html', {'referral': text})

@user_passes_test(is_admin)
def add_referral_link(request):
    referral_links = ReferralLink.objects.all()
    if request.method == 'POST':
        form = ReferralLinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_referral_link')
    else:
        form = ReferralLinkForm()
    return render(request, 'main/admin.html', {'form': form, 'referral_links': referral_links})

@csrf_exempt
def save_stats_data(request):
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
            social_network = request_data.get('social_network')
            ip_address = request_data.get('ip_address')
            StatsData.objects.create(social_network=social_network, ip_address=ip_address)
            return JsonResponse({'success': True})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON format'}, status=400)
    return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)