from django.contrib import admin
from .models import Category, Dish, TableReserv, Gallery, Photo, Events, OurTeam


class DishAdmin(admin.TabularInline):
    model = Dish
    raw_id_fields = ['category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [DishAdmin]
    list_display = ['title', 'position', 'is_visible']
    list_editable = ['position', 'is_visible']


@admin.register(Dish)
class DishAllAdmin(admin.ModelAdmin):
    model = Dish
    list_display = ['title', 'position', 'is_visible', 'ingredients', 'desc', 'price', 'photo', 'category',
                    'is_special']
    list_editable = ['position', 'is_visible', 'price']
    list_filter = ['category', 'is_special']


@admin.register(TableReserv)
class TableReservAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_phone', 'date', 'time', 'number_of_people', 'message', 'processed', 'date_of_reserv']
    list_editable = ['date', 'time', 'number_of_people', 'message', 'processed']
    list_filter = ['date', 'time']


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'description', 'date_time', 'price', 'photo', 'is_visible']
    list_editable = ['date_time', 'price', 'is_visible']


@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'description', 'photo', 'twitter', 'facebook', 'instagram', 'linkedin',
                    'is_visible']
    list_editable = ['position', 'is_visible']


class PhotoAdmin(admin.TabularInline):
    model = Photo
    raw_id_fields = ('gallery', )


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = [PhotoAdmin]
    list_display = ['title', 'position', 'is_visible']
    list_editable = ['position', 'is_visible']


@admin.register(Photo)
class PhotoAllAdmin(admin.ModelAdmin):
    model = Photo
    list_display = ['title', 'position', 'is_visible', 'photo', 'gallery']
    list_editable = ['is_visible', 'gallery']
    list_filter = ['gallery', 'position']
