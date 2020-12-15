from django.contrib import admin
from .models import Brand, Utility, Ingredient, SubCategory, HomePage, IngredientList, Category, Product, Region, Shop, Contact, GROUPES
from django.contrib import admin
from .models import User, PDFRequest
from django.contrib.auth.models import Group
from django.contrib import messages

admin.site.register(PDFRequest)

admin.site.register(User)
admin.site.register(Utility)

admin.site.unregister(Group)
# admin.site.unregister(User)

# admin.site.register(SubCategory)
# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('cat_id', 'cat_name', 'cat_short_name', 'level')

	def get_form(self, request, obj=None, **kwargs):
		self.exclude = ("level",)
		form = super(CategoryAdmin, self).get_form(request, obj, **kwargs)
		return form



admin.site.register(GROUPES)
admin.site.register(Shop)
admin.site.register(Region)
# admin.site.register(Contact)
# admin.site.register(Product)
# admin.site.register(Ingredient)
admin.site.register(Brand)
# admin.site.register(IngredientList)
admin.site.register(HomePage)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'email')
	list_filter = ('date',)
	def save_model(self, request, obj, form, change):
		if 'name' in form.changed_data:
			messages.add_message(request, messages.INFO, 'new contact')
		super(ContactAdmin, self).save_model(request, obj, form, changerequest, obj, form, change)


class ProductAdmin(admin.ModelAdmin):
	# prepopulated_fields = {"slug": ("DESIGNATION",)}
	search_fields = ('DESIGNATION', 'GENCODE', 'CODE')
	list_filter = ('date',)
	list_display = ('DESIGNATION', 'CODE', 'GENCODE', 'HYP', 'SUP', 'MINI')
	def get_form(self, request, obj=None, **kwargs):
		self.exclude = ("slug", "count")
		form = super(ProductAdmin, self).get_form(request, obj, **kwargs)
		return form

admin.site.register(Product, ProductAdmin)

class IngredientInline(admin.TabularInline):
	model = Ingredient
	extra = 8

class IngredientListAdmin(admin.ModelAdmin):
	list_display = ('TITLE',)
	inlines = [IngredientInline]

admin.site.register(IngredientList, IngredientListAdmin)