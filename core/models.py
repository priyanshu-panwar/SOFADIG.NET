from django.db import models
from PIL import Image
from django.utils.text import slugify

class HomePage(models.Model):
	TYPE = models.CharField(max_length=200, default='')
	PRODUIT = models.CharField(max_length=200, default='')
	PARTICULARITE = models.CharField(max_length=200, default='')
	IMAGE = models.ImageField(upload_to='HomePage/', default='default.jpg')
	date = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "8. YOUR HOME SCREEN"
		ordering = ['-date',]

	def __str__(self):
		return self.PRODUIT

class IngredientList(models.Model):
	TITLE = models.CharField(max_length=100, default='')

	class Meta:
		verbose_name_plural = "7. INGREDIENTS LIST"

	def __str__(self):
		return self.TITLE

class Brand(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='brands/')
	date = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "6. MARQUES"
		ordering = ['-date',]

	def __str__(self):
		return self.title


class Category(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "5. CATEGORIES"
		ordering = ['-date',]

	def __str__(self):
		return self.title


class GROUPES(models.Model):
	title = models.CharField(max_length=100, default='')

	class Meta:
		verbose_name_plural = "4. GROUPES"

	def __str__(self):
		return self.title


class Product(models.Model):
	HYP = models.BooleanField(default=False)
	SUP = models.BooleanField(default=False)
	MINI = models.BooleanField(default=False)
	CODE = models.CharField(max_length=200, default='')
	GROUPE_PRODUIT = models.ForeignKey(GROUPES, on_delete=models.CASCADE)
	BRAND = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
	DESIGNATION = models.CharField(max_length=200, default='')
	DESCRIPTION = models.TextField(default='')
	CATEGORIE = models.ForeignKey(Category, on_delete=models.CASCADE)
	PCB = models.IntegerField(default=0)
	SIZE = models.CharField(max_length=100, default='')
	GENCODE = models.CharField(max_length=100, default='')
	IMAGE = models.ImageField(upload_to='Products/', default='default.jpg')
	date = models.DateField(auto_now_add=True)
	slug = models.SlugField(unique=True)
	INGREDIENTS = models.ForeignKey('IngredientList', on_delete=models.CASCADE, null=True, blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.DESIGNATION)
		super(Product, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = "1. PRODUITS"
		ordering = ['DESIGNATION',]

	def __str__(self):
		return self.DESIGNATION


class Ingredient(models.Model):
	NAME = models.CharField(max_length=100, null=True, blank=True)
	AMT = models.CharField(max_length=100, null=True, blank=True)
	ING_LIST = models.ForeignKey(IngredientList, on_delete=models.CASCADE, null=True, blank=True)

	class Meta:
		verbose_name_plural = "9. INGREDIENTS"

	def __str__(self):
		return self.NAME


class Region(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "8. Régions"
		ordering = ['-date',]

	def __str__(self):
		return self.title


class Shop(models.Model):
	name = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
	url = models.URLField(null=True, blank=True)
	date = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "2. MAGASINS"
		ordering = ['-date',]

	def __str__(self):
		return self.name


class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	telephone = models.CharField(max_length=15)
	subject = models.CharField(max_length=200)
	message = models.TextField()
	date = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "3. CONTACTS"
		ordering = ['-date',]

	def __str__(self):
		return self.email

