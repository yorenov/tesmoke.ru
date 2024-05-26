from django.db import models


class StatsData(models.Model):
    social_network = models.CharField(max_length=20, verbose_name='Социальная сеть')
    ip_address = models.CharField(max_length=60, verbose_name='Айпи адрес')
    city = models.CharField(max_length=1024, verbose_name='Город', blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    def __str__(self):
        return f"{self.social_network} {self.ip_address} {self.city if self.city else '-'} {self.created_at.strftime('%d/%m/%Y, %H:%M:%S')}"

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class ReferralLink(models.Model):
    refid = models.CharField(max_length=64, verbose_name='Реферальное айди', unique=True)
    visits = models.IntegerField(default=0, verbose_name='Посещения')
    stats = models.ManyToManyField(StatsData, 'referral_link', verbose_name='Записи')

    def __str__(self):
        return self.refid

    class Meta:
        verbose_name = 'Реферальная ссылка'
        verbose_name_plural = 'Реферальные ссылки'
