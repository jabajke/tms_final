from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default='Название статьи')
    anons = models.CharField('Анонс статьи', max_length=250, db_index=True)
    full_text = models.TextField('Текст статьи')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'