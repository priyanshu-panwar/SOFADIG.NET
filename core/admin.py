from django.contrib import admin
from .models import Brand, Ingredient, Category, Product, ProductBrand, Region, Shop, Contact

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProductBrand)
admin.site.register(Region)
admin.site.register(Shop)
admin.site.register(Contact)

class IngredientInline(admin.TabularInline):
	model = Ingredient
	extra = 10

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'code', 'category', 'pbrand']
	list_filter = ['date', 'category']
	search_fields = ('name', 'code')
	inlines = [IngredientInline]

