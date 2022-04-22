from django.contrib import admin

from .models import Monument, MonumentImage, MonumentVideo


class MonumentImageAdmin(admin.StackedInline):
    model = MonumentImage
    extra = 1


class MonumentVideoAdmin(admin.StackedInline):
    model = MonumentVideo
    extra = 1


@admin.register(Monument)
class MonumentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'image', 'description']}),
        ('Date Info.', {'fields': ['pub_date']}),
    ]
    inlines = [MonumentImageAdmin, MonumentVideoAdmin]
    list_display = ('title', 'pub_date',)
    list_filter = ['pub_date']
    search_fields = ['question_text']

    class Meta:
        model = Monument
