from django.contrib import admin

from .models import Beauty, BeautyImage, BeautyVideo


class BeautyImageAdmin(admin.StackedInline):
    model = BeautyImage
    extra = 1


class BeautyVideoAdmin(admin.StackedInline):
    model = BeautyVideo
    extra = 1


@admin.register(Beauty)
class BeautyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'image', 'description']}),
        ('Date Info.', {'fields': ['pub_date']}),
    ]
    inlines = [BeautyImageAdmin, BeautyVideoAdmin]
    list_display = ('title', 'pub_date',)
    list_filter = ['pub_date']
    search_fields = ['question_text']

    class Meta:
        model = Beauty
