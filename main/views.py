import json
from urllib.request import urlopen

from django.http import JsonResponse, QueryDict, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_exempt
from .models import StatsData, ReferralLink
from .forms import ReferralLinkForm


def index(request):
    context = {}
    if request.GET.get('refid'):
        context = {'refid': request.GET.get('refid')}
    # print(context)
    return render(request, 'main/index.html', context=context)


def ref_index(request, refid):
    print('REFINDEX')
    return render(request, 'main/index.html', context={'refid': refid})


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


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# @csrf_exempt
def save_stats_data(request):
    # if request.method == 'POST':
    #     try:
    #         request_data = json.loads(request.body)
    #         social_network = request_data.get('social_network')
    #         ip_address = request_data.get('ip_address')
    #         StatsData.objects.create(social_network=social_network, ip_address=ip_address)
    #         return JsonResponse({'success': True})
    #     except json.JSONDecodeError:
    #         return JsonResponse({'success': False, 'error': 'Invalid JSON format'}, status=400)
    # return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)
    # return f'{social_network}, {refid}, {url}'
    # print()
    # try:
    #
    # g = GeoIP2()
    # print(g.city("5.101.18.87"))

    my_ip = get_client_ip(request)
    url = f'http://ipinfo.io/{my_ip}/json'
    response = urlopen(url)
    data = json.load(response)
    city = data['city'] if 'city' in data else None


    # request_data = json.loads(request.body)
    # social_network = request_data.get('social_network')
    # ip_address = request_data.get('ip_address')
    stats = StatsData.objects.create(social_network=request.GET.get('social_network', ''), ip_address=my_ip, city=city)
    # except json.JSONDecodeError:
    #     pass

    if 'refid' in request.GET:
        if ReferralLink.objects.filter(refid=request.GET.get('refid')).exists():
            referral: ReferralLink = ReferralLink.objects.get(refid=request.GET.get('refid'))
            referral.visits += 1
            referral.stats.add(stats)
            referral.save()

    return redirect(request.GET.get('url', ''))
