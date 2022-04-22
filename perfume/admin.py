from django.contrib import admin

from .models import Perfume, PerfumeImage, PerfumeVideo


class PerfumeImageAdmin(admin.StackedInline):
    model = PerfumeImage
    extra = 1


class PerfumeVideoAdmin(admin.StackedInline):
    model = PerfumeVideo
    extra = 1


@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'image', 'description']}),
        ('Date Info.', {'fields': ['pub_date']}),
    ]
    inlines = [PerfumeImageAdmin, PerfumeVideoAdmin]
    list_display = ('title', 'pub_date',)
    list_filter = ['pub_date']
    search_fields = ['question_text']

    class Meta:
        model = Perfume
