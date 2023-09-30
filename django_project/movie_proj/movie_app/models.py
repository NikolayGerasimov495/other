from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер {self.first_name} {self.last_name}'
        else:
            return f'Актриса {self.first_name} {self.last_name}'


class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = [
        ('EUR', 'Euro'),
        ('USD', 'Dollar'),
        ('RUB', 'Rubles')
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True, blank=True)  # blank отвечает, чтобы можно было сохранять пустоту в админке
    budget = models.IntegerField(default=1000000)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    slug = models.SlugField(default='', null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    director = models.ForeignKey(Director, on_delete=models.PROTECT,
                                 null=True)  # делаем связь между таблицами один ко многим.PROTECT не дает удалить данные тк у него есть дочерние записи
    # есть метод CASCADE (может удалить запись и дочернии записи) есть метод SET_NULL запись удалится и проставить нулл
    actors = models.ManyToManyField(Actor)

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    # def get_url(self):
    #     return reverse('movie-detail', args=[self.id])

    def __str__(self):
        return f'{self.name}-{self.rating}% {self.year}'
