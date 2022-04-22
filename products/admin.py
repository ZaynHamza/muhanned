from django.contrib import admin

from .models import Product, ProductImage, ProductVideo


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
    extra = 1


class ProductVideoAdmin(admin.StackedInline):
    model = ProductVideo
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'image', 'description']}),
        ('Date Info.', {'fields': ['pub_date']}),
    ]
    inlines = [ProductImageAdmin, ProductVideoAdmin]
    list_display = ('title', 'pub_date',)
    list_filter = ['pub_date']
    search_fields = ['question_text']

    class Meta:
        model = Product
