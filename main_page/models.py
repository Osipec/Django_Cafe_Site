from django.db import models
from django.core.validators import RegexValidator


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    def __iter__(self):
        for item in self.dishes.all():
            yield item

    class Meta:
        ordering = ('position',)


class Dish(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    ingredients = models.CharField(max_length=255)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='dishes/%Y_%m_%d', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('category', 'position',)


class Events(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    description = models.TextField(max_length=500, blank=True)
    date_time = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='events/%Y_%m_%d', blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)


class Gallery(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)


class Photo(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='GalleryPhoto/%Y_%m_%d', blank=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position', 'gallery')


class TableReserv(models.Model):
    phone_validator = RegexValidator(regex=r'^\+?3?8?0\d{2}[- ]?(\d[ -]?){7}$', message="Wrong number")
    user_name = models.CharField(max_length=50, db_index=True)
    user_email = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=20, validators=[phone_validator])
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    number_of_people = models.SmallIntegerField()
    message = models.CharField(blank=True, max_length=255)
    processed = models.BooleanField(default=False)
    date_of_reserv = models.DateField(auto_now_add=True)
    date_processed = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.date} ({self.time}): {self.user_name}'

    class Meta:
        ordering = ('-date', 'time')


class OurTeam(models.Model):
    name = models.CharField(max_length=50, db_index=True, unique=True)
    position = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to='Workers/', blank=True)
    twitter = models.URLField(help_text='Twitter account')
    facebook = models.URLField(help_text='Facebook account')
    instagram = models.URLField(help_text='Instagram account')
    linkedin = models.URLField(help_text='LinkedIn account')
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}: {self.position}'
