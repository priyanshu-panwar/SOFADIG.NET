from django.db import models
from PIL import Image
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail 
from django.conf import settings


class User(AbstractUser):
	is_client = models.BooleanField(default=True)
	is_commercial = models.BooleanField(default=False)
	is_marketing = models.BooleanField(default=False)



class Utility(models.Model):
	TopHeading = models.CharField(max_length=500, default='')
	TopSubHeading = models.CharField(max_length=500, default='')
	TopParagraph = models.CharField(max_length=500, default='')
	PresentationHeading = models.CharField(max_length=500, default='')
	PresentationPara1 = models.CharField(max_length=500, default='')
	PresentationPara2 = models.CharField(max_length=500, default='')
	PresentationPara3 = models.CharField(max_length=500, default='')
	IMG1 = models.ImageField(upload_to='HomePage/', default='default.jpg')
	IMG2 = models.ImageField(upload_to='HomePage/', default='default.jpg')
	IMG3 = models.ImageField(upload_to='HomePage/', default='default.jpg')
	Lundi = models.CharField(max_length=100, default='8:00 – 12:00 / 14:00 – 17:00')
	Mardi = models.CharField(max_length=100, default='8:00 – 12:00 / 14:00 – 17:00')
	Mercredi = models.CharField(max_length=100, default='8:00 – 12:00')
	Jeudi = models.CharField(max_length=100, default='8:00 – 12:00 / 14:00 – 17:00')
	Vendredi = models.CharField(max_length=100, default='8:00 – 12:00 / 14:00 – 17:00')
	Samedi = models.CharField(max_length=100, default='Fermé')
	Dimanche = models.CharField(max_length=100, default='Fermé')
	Adresse = models.CharField(max_length=200, default='Impasse Georges Claude, Z.I. Jarry, 97122 Baie-Mahault, Guadeloupe')
	Telephone = models.CharField(max_length=100, default='+590 (0) 590 26 73 20')
	Fax = models.CharField(max_length=100, default='+590 (0) 590 26 73 21')
	Email = models.CharField(max_length=100, default='info@sofadig.net')
	contact_subject = models.CharField(max_length=200, default='')
	contact_mail = models.CharField(max_length=500, default='')
	info_subject = models.CharField(max_length=200, default='')
	info_mail = models.CharField(max_length=500, default='')
	success_message = models.CharField(max_length=500, default='')

	class Meta:
		verbose_name_plural = "-----  RENSEIGNEMENTS ----"

	def __str__(self):
		return "DEFAULT"

class HomePage(models.Model):
	TYPE = models.CharField(max_length=200, default='')
	PRODUIT = models.CharField(max_length=200, default='')
	PARTICULARITE = models.CharField(max_length=200, default='')
	IMAGE = models.ImageField(upload_to='HomePage/', default='default.jpg')
	date = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "----- DIAPORAMA -----"
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
	image = models.ImageField(upload_to='brands/', default='default_brand.jpg')
	date = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "6. MARQUES"
		ordering = ['-date',]

	def __str__(self):
		return self.title


class Category(models.Model):
	cat_id = models.CharField(max_length=100, default='')
	cat_name = models.CharField(max_length=100, default='')
	cat_short_name = models.CharField(max_length=100, default='')
	level = models.CharField(max_length=1, default=1)
	date = models.DateField(auto_now_add=True)

	def save(self, *args, **kwargs):
		print(len(self.cat_id))
		if (len(self.cat_id) == 3):
			self.level = '1'
		elif (len(self.cat_id) == 5):
			self.level = '2'
		else:
			self.level = '3'
		super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = "5. CATEGORIES"
		ordering = ['cat_name',]

	def __str__(self):
		return f'{self.cat_id} | {self.cat_name}'

class SubCategory(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "10. SUB CATEGORIES"

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
	CATEGORIE = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
	# SUBCATEGORY = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
	PCB = models.CharField(max_length=5, default='0')
	SIZE = models.CharField(max_length=100, default='')
	GENCODE = models.CharField(max_length=100, default='')
	IMAGE = models.ImageField(upload_to='Products/', default='default.jpg')
	date = models.DateField(auto_now_add=True)
	REQUEST_INFO = models.BooleanField(default=False)
	slug = models.SlugField(unique=True)
	count = models.IntegerField(default=0)
	INGREDIENTS = models.ForeignKey('IngredientList', on_delete=models.CASCADE, null=True, blank=True)

	def save(self, *args, **kwargs):
		# self.slug = slugify(self.DESIGNATION)
		a = self.CODE
		b = self.BRAND.title
		c = self.DESIGNATION
		a = a.replace(' ', '-').lower()
		b = b.replace(' ', '-').lower()
		c = c.replace(' ', '-').lower()
		self.slug = f'{a}-{b}-{c}'
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
		verbose_name_plural = "8. REGIONS"
		ordering = ['-date',]

	def __str__(self):
		return self.title


class Shop(models.Model):
	name = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
	latitude = models.CharField(max_length=7, default='00')
	longitude = models.CharField(max_length=7, default='00')
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



class PDFRequest(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	phone = models.CharField(max_length=13)
	product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		recipient_list = [settings.EMAIL_HOST_USER, ]
		message = f'Hello, {self.name} ({self.email}) has asked for information request for product - {self.product.DESIGNATION}. \n PHone - {self.phone}.'
		send_mail("New INFORMATION REQUEST", message, settings.EMAIL_HOST_USER, recipient_list)
		super(PDFRequest, self).save(*args, **kwargs)

	class Meta:
		ordering = ['-date',]

	def __str__(self):
		return self.email
