from django.contrib import admin

from .models import Fashion, FashionImage, FashionVideo


class FashionImageAdmin(admin.StackedInline):
    model = FashionImage
    extra = 1


class FashionVideoAdmin(admin.StackedInline):
    model = FashionVideo
    extra = 1


@admin.register(Fashion)
class FashionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'image', 'description']}),
        ('Date Info.', {'fields': ['pub_date']}),
    ]
    inlines = [FashionImageAdmin, FashionVideoAdmin]
    list_display = ('title', 'pub_date',)
    list_filter = ['pub_date']
    search_fields = ['question_text']

    class Meta:
        model = Fashion
