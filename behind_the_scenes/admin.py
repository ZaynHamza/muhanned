from django.contrib import admin

from .models import BehindTheScenes, BehindTheScenesImage, BehindTheScenesVideo


class BehindTheScenesImageAdmin(admin.StackedInline):
    model = BehindTheScenesImage
    extra = 1


class BehindTheScenesVideoAdmin(admin.StackedInline):
    model = BehindTheScenesVideo
    extra = 1


@admin.register(BehindTheScenes)
class BehindTheScenesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'image', 'description']}),
        ('Date Info.', {'fields': ['pub_date']}),
    ]
    inlines = [BehindTheScenesImageAdmin, BehindTheScenesVideoAdmin]
    list_display = ('title', 'pub_date',)
    list_filter = ['pub_date']
    search_fields = ['question_text']

    class Meta:
        model = BehindTheScenes
