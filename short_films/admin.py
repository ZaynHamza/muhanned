from django.contrib import admin

from .models import ShortFilms, ShortFilmsImage, ShortFilmsVideo


class ShortFilmsImageAdmin(admin.StackedInline):
    model = ShortFilmsImage
    extra = 1


class ShortFilmsVideoAdmin(admin.StackedInline):
    model = ShortFilmsVideo
    extra = 1


@admin.register(ShortFilms)
class ShortFilmsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'image', 'description']}),
        ('Date Info.', {'fields': ['pub_date']}),
    ]
    inlines = [ShortFilmsImageAdmin, ShortFilmsVideoAdmin]
    list_display = ('title', 'pub_date',)
    list_filter = ['pub_date']
    search_fields = ['question_text']

    class Meta:
        model = ShortFilms
