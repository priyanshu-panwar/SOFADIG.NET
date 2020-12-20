from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Region, Shop, Contact, Brand, HomePage, PDFRequest, GROUPES
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponse

import xlrd
import csv

def load_data_stores(request):
	with open('C:\\stores.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			s = Shop()
			s.name = row[0]
			s.city = row[1]
			s.region, created = Region.objects.get_or_create(
				title = row[2]
			)
			s.url = row[3]
			s.latitude = row[4]
			s.longitude = row[5]
			s.save()
			print(f"{row[0]} is saved in DB.")
	return HttpResponse("done")


def load_data_from_excel(request):
	# url = staticfiles_storage.url('products.xlsx')
	with open('C:\\products.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			p = Product.objects.filter(CODE=row[3]).first()
			p.CODE = row[3]
			p.BRAND, created = Brand.objects.get_or_create(
				title = f'{row[4]}'
			)
			if p.DESIGNATION != row[5]:
				p.DESIGNATION = row[5]
			if p.DESCRIPTION != row[6]:
				p.DESCRIPTION = row[6]
			p.CATEGORIE, created = Category.objects.get_or_create(
				cat_id = f'{row[7]}'
			)
			p.PCB = f'{row[8]}'
			p.GENCODE = row[9]
			p.SIZE = row[10]
			if row[11].strip() == "x":
				p.REQUEST_INFO = True
			p.GROUPE_PRODUIT, created = GROUPES.objects.get_or_create(
				title = f'{row[12]}'
			)
			c = row[3] + ".jpg"
			p.IMAGE = c
			p.save()
			print(f'{row[5]} is saved in DB.')
	return HttpResponse("hell")

from django.conf import settings
from .models import Utility

from django.contrib import messages
def request_info(request, pk):
	util = Utility.objects.all()
	util = util[::-1]
	util = util[0]
	
	p = get_object_or_404(Product, pk=pk)
	if request.method == 'POST':
		
		name = request.POST['pdf-name']
		email = request.POST['pdf-email']
		phone = request.POST['pdf-phone']
		if is_valid_queryparam(email):
			# fun = PDFRequest(name=name, email=email, phone=phone, product=p)
			# fun.save()
			recipient_list = ["sofadig@wanadoo.fr", ]
			message = f'{ util.info_mail }\n{ p.BRAND }\n{ p.DESIGNATION }\n{ p.GENCODE }    \n\n  { util.contact_mail }\n{name} ({email}) \n \n Phone - {phone}.'
			send_mail(f"{ util.info_subject }", message, "site@sofadig.net", recipient_list);messages.success(request, f'{util.success_message}');
			return redirect('detail', pk=p.slug)
	else:
		return redirect('detail', pk=p.slug)


def logout(request):
	auth_logout(request)
	return redirect('home')

def login(request):
	if request.method == 'POST':
		username_ = request.POST['username']
		pass_ = request.POST['password']
		print(username_)
		print(pass_)
		user = authenticate(request, username=username_, password=pass_)
		if user is not None:
			auth_login(request, user)
			return redirect('home')
		else:
			return redirect('home')
	else:
		return redirect('home')

def home(request):
	util = Utility.objects.all()
	util = util[::-1]
	if (len(util) > 0):
		util = util[0]
	slides = HomePage.objects.all()
	br = Brand.objects.all()
	brands = []
	for b in br:
		if b.image != "default_brand.jpg":
			brands.append(b)
	regions = Region.objects.all()
	"""
	username_ = request.GET.get('username')
	password_ = request.GET.get('password')
	print(username_)
	print(password_)
	if is_valid_queryparam(username_) and is_valid_queryparam(password_):
		print("POST")
		user = authenticate(request, username=username_, password=password_)
		print("user = ", user)
		if user is not None:
			login(request, user)
			print("logging")
			return redirect('home')
	"""
	context = {
		'brands' : brands,
		'regions' : regions,
		'slides' : slides,
		'util' : util,
	}
	return render(request, 'core/x_home2.html', context)


def catalog(request):
	util = Utility.objects.all()
	util = util[::-1]
	util = util[0]
	products = Product.objects.all()
	products = products[::-1]
	count = len(products)

	url = 1
	fun = 0
	level1 = 1

	categories_ = Category.objects.all()
	# categories_ = categories_[::-1]

	categories = []
	v = []

	for i in products:
		x = i.CATEGORIE.cat_id[0:3]
		c = Category.objects.filter(cat_id__iexact=x)
		if c:
			c = c[0]
			if x not in v:
				v.append(x)
				y = []
				y.append(x)
				y.append(c.cat_name)
				categories.append(y)

	regions = Region.objects.all()

	page = request.GET.get('page', 1)
	paginator = Paginator(products, 12)

	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	context = {
		'products' : products,
		'categories' : categories,
		'regions' : regions,
		'count' : count,
		'url' : url,
		'util' : util,
		'level1' : level1,
	}
	return render(request, 'core/x_catalogue.html', context)


def detail(request, pk):
	util = Utility.objects.all()
	util = util[::-1]
	util = util[0]
	object = get_object_or_404(Product, slug=pk)
	object.count += 1
	object.save()
	hi = object.CATEGORIE.cat_id
	bread2 = Category.objects.filter(cat_id__iexact=hi[0:5])
	if bread2:
		bread2 = bread2[0]

	bread1 = Category.objects.filter(cat_id__iexact=hi[0:3])
	if bread1:
		bread1 = bread1[0]
	regions = Region.objects.all()
	yo = object.CATEGORIE.cat_id[:3]
	print("yo = ", yo)
	context = {
		'product' : object,
		'regions' : regions,
		'util' : util,
		'yo' : yo,
		'bread1' : bread1,
		'bread2' : bread2,
	}
	return render(request, 'core/x_product_details.html', context)


def ingredients(request, pk):
	util = Utility.objects.all()
	util = util[::-1]
	util = util[0]
	object = get_object_or_404(Product, slug=pk)
	regions = Region.objects.all()
	context = {
		'product' : object,
		'regions' :regions,
		'util' : util,
	}
	return render(request, 'core/x_product_ingredients.html', context)


def category_1_details(request, pk):
	util = Utility.objects.all()
	util = util[::-1]
	util = util[0]
	products = Product.objects.filter(CATEGORIE__cat_id__startswith=pk)
	products = products[::-1]
	count = len(products)

	bread1 = Category.objects.filter(cat_id__iexact=pk)
	if bread1:
		bread1 = bread1[0]

	categories_ = Category.objects.filter(cat_id__startswith=pk)
	# categories_ = categories_[::-1]

	url = 2
	fun = 0
	level2 = 1

	categories = []
	v = []

	for i in categories_:
		x = i.cat_id
		if len(x) == 5 and x not in v:
			v.append(x)
			y = []
			y.append(x)
			y.append(i.cat_name)
			categories.append(y)


	regions = Region.objects.all()

	page = request.GET.get('page', 1)
	paginator = Paginator(products, 12)

	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	context = {
		'products' : products,
		'regions' : regions,
		'categories' : categories,
		'count' : count,
		'url' : url,
		'bread1' : bread1,
		'util' : util,
		'level2' : level2,
	}
	return render(request, 'core/x_catalogue.html', context)

def category_2_details(request, pk):
	util = Utility.objects.all()
	util = util[::-1]
	util = util[0]
	products = Product.objects.filter(CATEGORIE__cat_id__startswith=pk)
	products = products[::-1]
	count = len(products)

	categories_ = Category.objects.filter(cat_id__startswith=pk)
	# categories_ = categories_[::-1]

	bread2 = Category.objects.filter(cat_id__iexact=pk)
	if bread2:
		bread2 = bread2[0]

	bread1 = Category.objects.filter(cat_id__iexact=pk[0:3])
	if bread1:
		bread1 = bread1[0]

	categories = []
	v = []

	for i in categories_:
		x = i.cat_id
		if len(x) == 7 and x not in v:
			v.append(x)
			y = []
			y.append(x)
			y.append(i.cat_name)
			categories.append(y)

	regions = Region.objects.all()

	url = 3
	fun = 2

	page = request.GET.get('page', 1)
	paginator = Paginator(products, 12)

	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	context = {
		'products' : products,
		'regions' : regions,
		'categories' : categories,
		'count' : count,
		'url' : url,
		'util' : util,
		'bread1' : bread1,
		'bread2' : bread2,
	}
	return render(request, 'core/x_catalogue.html', context)

def pos(request, pk):
	util = Utility.objects.all()
	util = util[::-1]
	util = util[0]
	regions = Region.objects.all()
	object = get_object_or_404(Region, pk=pk)
	shops = Shop.objects.filter(region__id=pk).order_by('name')
	shops = shops[::-1]

	context = {
		'regions' : regions,
		'shops' : shops,
		'region' : object,
		'util' : util,
	}

	return render(request, 'core/x_points-de-vente.html', context)


def is_valid_queryparam(param):
	return param != '' and param is not None


from django.core.mail import send_mail
from sofadig.settings import EMAIL_HOST_USER

def contact(request):
	util = Utility.objects.all()
	util = util[::-1]
	util = util[0]
	regions = Region.objects.all()

	name = request.GET.get('contact-name')
	email = request.GET.get('contact-email')
	phone = request.GET.get('contact-phone')
	subject = request.GET.get('contact-subject')
	message = request.GET.get('contact-message')
	print(name)
	print(email)
	print(phone)
	print(subject)
	print(message)
	context = {
		'regions' : regions,
		'util' : util,
	}
	if is_valid_queryparam(name) and is_valid_queryparam(email) and is_valid_queryparam(message):
		c = Contact(name=name, email=email, telephone=phone, subject=subject, message=message)
		c.save()
		"""send_mail(
			f'{ util.contact_subject }',
			f"{ util.contact_mail }",
			EMAIL_HOST_USER,
			[email, ],
			fail_silently=True,
		)"""
		send_mail(
			f'{ util.contact_subject }',
			f'{ util.contact_mail }\n{ name }\n{ email }\n{ email }\nMessage: { message }',
			EMAIL_HOST_USER,
			['accueil.sofadig@orange.fr', ],
			fail_silently=True,
		)
		return render(request, 'core/thankyou.html', context)

	
	return render(request, 'core/x_contact.html', context)


def politiq(request):
	util = Utility.objects.all()
	util = util[::-1]
	util = util[0]
	context = {
		'util' : util,
	}
	return render(request, 'core/condition.html', context)


def condition(request):
	util = Utility.objects.all()
	util = util[::-1]
	util = util[0]
	context = {
		'util' : util,
	}
	return render(request, 'core/politiq.html', context)
