from django.contrib import admin

from main.models import ReferralLink, StatsData


# Register your models here.
class ReferralLinkAdmin(admin.ModelAdmin):
    list_display = ['refid', 'visits']
    fields = ['refid', 'visits', 'stats']
    # filter_horizontal = ['stats']
    readonly_fields = ['stats']


class CityFilter(admin.SimpleListFilter):
    title = 'Город'

    parameter_name = 'city'

    def lookups(self, request, model_admin):
        cities = list(StatsData.objects.order_by().values_list('city', flat=True).distinct())
        current_lookups = ()
        for city in cities:
            if city:
                current_lookups += ((city, city),)
        return current_lookups

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(city=self.value())


class ReferralLinkFilter(admin.SimpleListFilter):
    title = 'Реферальная ссылка'

    parameter_name = 'referral_link'

    def lookups(self, request, model_admin):
        ref_links = ReferralLink.objects.all()
        current_lookups = ()
        for ref_link in ref_links:
            if ref_link.refid:
                current_lookups += ((ref_link.id, ref_link.refid),)
        return current_lookups

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(referral_link=self.value())


class StatsDataAdmin(admin.ModelAdmin):
    list_display = ['social_network', 'ip_address', 'city', 'created_at']
    fields = ['social_network', 'ip_address', 'city', 'created_at']
    readonly_fields = ['social_network', 'ip_address', 'created_at', 'city']
    list_filter = [CityFilter, ReferralLinkFilter]


admin.site.register(ReferralLink, ReferralLinkAdmin)
admin.site.register(StatsData, StatsDataAdmin)
