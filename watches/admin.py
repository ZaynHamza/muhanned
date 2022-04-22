from django.contrib import admin

from .models import Watch, WatchImage, WatchVideo


class WatchImageAdmin(admin.StackedInline):
    model = WatchImage
    extra = 1


class WatchVideoAdmin(admin.StackedInline):
    model = WatchVideo
    extra = 1


@admin.register(Watch)
class WatchesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'image', 'description']}),
        ('Date Info.', {'fields': ['pub_date']}),
    ]
    inlines = [WatchImageAdmin, WatchVideoAdmin]
    list_display = ('title', 'pub_date',)
    list_filter = ['pub_date']
    search_fields = ['question_text']

    class Meta:
        model = Watch
