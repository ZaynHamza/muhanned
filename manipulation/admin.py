from django.contrib import admin

from .models import Manipulation, ManipulationImage, ManipulationVideo


class ManipulationImageAdmin(admin.StackedInline):
    model = ManipulationImage
    extra = 1


class ManipulationVideoAdmin(admin.StackedInline):
    model = ManipulationVideo
    extra = 1


@admin.register(Manipulation)
class ManipulationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'image', 'description']}),
        ('Date Info.', {'fields': ['pub_date']}),
    ]
    inlines = [ManipulationImageAdmin, ManipulationVideoAdmin]
    list_display = ('title', 'pub_date',)
    list_filter = ['pub_date']
    search_fields = ['question_text']

    class Meta:
        model = Manipulation
