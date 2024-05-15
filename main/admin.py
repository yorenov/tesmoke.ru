from django.contrib import admin

from main.models import ReferralLink, StatsData


# Register your models here.
class ReferralLinkAdmin(admin.ModelAdmin):
    list_display = ['text', 'visits']
    fields = ['text', 'visits']


class StatsDataAdmin(admin.ModelAdmin):
    list_display = ['social_network', 'ip_address', 'created_at']
    fields = ['social_network', 'ip_address', 'created_at']
    readonly_fields = ['created_at']


admin.site.register(ReferralLink, ReferralLinkAdmin)
admin.site.register(StatsData, StatsDataAdmin)
