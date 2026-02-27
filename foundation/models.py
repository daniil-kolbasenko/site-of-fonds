from django.db import models

class MenuItem(models.Model):
    title = models.CharField("Название", max_length=100)
    url = models.CharField("URL", max_length=200, default='/')
    order = models.IntegerField("Порядок", default=0)
    is_active = models.BooleanField("Активен", default=True)

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"
        ordering = ['order']

    def __str__(self):
        return self.title

class SiteSettings(models.Model):
    title = models.CharField("Название сайта", max_length=200, 
                           default="Благотворительный Фонд Ильинской больницы")
    phone = models.CharField("Телефон", max_length=20, default="+7 495 645 33 77")
    email = models.EmailField("Email", blank=True)
    logo = models.ImageField("Логотип", upload_to='logo/', blank=True, null=True)
    support_url = models.CharField("Ссылка на поддержку", max_length=200, 
                                   default='/support/')

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"

    def __str__(self):
        return self.title