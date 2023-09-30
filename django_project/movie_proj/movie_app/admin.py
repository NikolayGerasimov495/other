from django.contrib import admin
from .models import Movie, Director, Actor # импортируем название таблиц
from django.db.models import QuerySet

admin.site.register(Director)
admin.site.register(Actor)

class RaringFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 79', 'Высокий'),
            ('>=80', 'Высочайший'),
        ]

    def queryset(self, request, queryset):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        if self.value() == 'от 60 до 79':
            return queryset.filter(rating__gte=60).filter(rating__lt=80)
        if self.value() == '>=80':
            return queryset.filter(rating__gt=80)
        return queryset


@admin.register(Movie)  # навешиваем декоратор. Можно отсавить так - admin.site.register(Movie, MovieAdmin)
class MovieAdmin(
    admin.ModelAdmin):  # чтобы в админке отображались поля таблицы. Добавляем в admin.site.register(Movie, MovieAdmin)
    exclude = ['slug']  # при добавлении строки фильма исключает поле
    list_display = ['name', 'rating', 'year', 'budget', 'director',
                    'rating_status']  # - для отображения
    list_editable = ['rating', 'year', 'budget', 'director',]  # -для редактирования
    filter_horizontal = ['actors'] #добавляет виджет фильтр актеров
    ordering = ['rating']  # для сортировки можно поставить '-rating' - будет в обратном порядке
    list_per_page = 10  # погинация (отображения записей на странице)
    actions = ['set_dollars', 'set_euro']
    search_fields = ['name']
    list_filter = ['name', 'currency', RaringFilter]  # для фильтрации

    @admin.display(ordering='rating', description='Статус')  # для возможности сортировки rating_status по полю rating
    def rating_status(self,
                      mov: Movie):  # можно оставить просто mov(наследуем от класса Movie), а можно аннотировать как в записи(тогда pycharm увидит переменные)
        if mov.rating < 50:
            return "Зачем это смотреть"
        if mov.rating < 70:
            return "Разок можно глянуть"
        if mov.rating < 85:
            return "Зачет"
        return "Топчик"

    # admin.site.register(Movie, MovieAdmin)
    @admin.action(description='Установить валюту в доллар')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)  # метод update помогает обновить значения

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, qs: QuerySet):
        count_update = qs.update(currency=Movie.EUR)  # метод update помогает обновить значения
        self.message_user(request, f'Было обновлено {count_update} записей')
