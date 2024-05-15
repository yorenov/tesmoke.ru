from django.db import models


class ReferralLink(models.Model):
    text = models.TextField(verbose_name='Текст')
    visits = models.IntegerField(default=0, verbose_name='Посещения')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Реферальная ссылка'
        verbose_name_plural = 'Реферальные ссылки'


class StatsData(models.Model):
    social_network = models.CharField(max_length=20, verbose_name='Социальная сеть')
    ip_address = models.CharField(max_length=60, verbose_name='Айпи адрес')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    def __str__(self):
        return f"{self.social_network} - {self.ip_address}"

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
