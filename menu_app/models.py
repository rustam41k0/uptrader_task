from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    url = models.SlugField(max_length=150, unique=True, verbose_name='URL')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menu"
