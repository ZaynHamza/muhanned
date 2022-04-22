from django.contrib import admin

from .models import Food, FoodImage, FoodVideo


class FoodImageAdmin(admin.StackedInline):
    model = FoodImage
    extra = 1


class FoodVideoAdmin(admin.StackedInline):
    model = FoodVideo
    extra = 1


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'image', 'description']}),
        ('Date Info.', {'fields': ['pub_date']}),
    ]
    inlines = [FoodImageAdmin, FoodVideoAdmin]
    list_display = ('title', 'pub_date',)
    list_filter = ['pub_date']
    search_fields = ['question_text']

    class Meta:
        model = Food