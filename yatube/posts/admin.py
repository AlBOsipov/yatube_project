from django.contrib import admin
from .models import Post, Group

class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = (
        'pk', 
        'text', 
        'pub_date', 
        'author',
        'group',
    ) 
    # Содержимое поля груп можно ред в админке
    list_editable = ('group',)
    # Доступен поиск по полю текста
    search_fields = ('text',)
    # Доступна фильтрация по полю даты
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'

# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Post, PostAdmin) 
admin.site.register(Group)
