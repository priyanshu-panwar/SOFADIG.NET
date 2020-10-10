from django.db import models
from PIL import Image
from django.utils.translation import gettext as _


class Brand(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='brands/')
	date = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name_plural = _("Brands")
		ordering = ['-date',]

	def __str__(self):
		return self.title


class Category(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Categories"
		ordering = ['-date',]

	def __str__(self):
		return self.title


class ProductBrand(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='pbrands/', null=True, blank=True)
	date = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Produit Marques"
		ordering = ['-date',]

	def __str__(self):
		return self.title


class Product(models.Model):
	name = models.CharField(max_length=100)
	pbrand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, null=True)
	code = models.CharField(max_length=20)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	size = models.CharField(max_length=100)
	description = models.TextField()
	image = models.ImageField(upload_to='Products/', default='default.jpg')
	date = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Produit"
		ordering = ['-date',]

	def __str__(self):
		return self.name


class Ingredient(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	amt = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Region(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Régions"
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
		verbose_name_plural = "Magasins"
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
		verbose_name_plural = "Contacts"
		ordering = ['-date',]

	def __str__(self):
		return self.email

