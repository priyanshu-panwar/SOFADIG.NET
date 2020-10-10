from django.shortcuts import render, get_object_or_404
from .models import ProductBrand, Category, Product, Region, Shop, Contact
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
	brands = ProductBrand.objects.all()
	regions = Region.objects.all()
	context = {
		'brands' : brands,
		'regions' : regions,
	}
	return render(request, 'core/x_home.html', context)


def catalog(request):
	products = Product.objects.all()
	products = products[::-1]
	count = len(products)

	categories = Category.objects.all()
	categories = categories[::-1]

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
	}
	return render(request, 'core/x_catalogue.html', context)


def detail(request, pk):
	object = get_object_or_404(Product, pk=pk)
	regions = Region.objects.all()
	context = {
		'product' : object,
		'regions' : regions,
	}
	return render(request, 'core/x_product_details.html', context)


def ingredients(request, pk):
	object = get_object_or_404(Product, pk=pk)
	regions = Region.objects.all()
	context = {
		'product' : object,
		'regions' :regions,
	}
	return render(request, 'core/x_product_ingredients.html', context)


def category_details(request, pk):
	products = Product.objects.filter(category__id=pk)
	products = products[::-1]
	count = len(products)

	categories = Category.objects.all()
	categories = categories[::-1]

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
	}
	return render(request, 'core/x_catalogue.html', context)


def pos(request, pk):
	regions = Region.objects.all()
	object = get_object_or_404(Region, pk=pk)
	shops = Shop.objects.filter(region__id=pk).order_by('name')
	shops = shops[::-1]

	context = {
		'regions' : regions,
		'shops' : shops,
		'region' : object,
	}

	return render(request, 'core/x_points-de-vente.html', context)


def is_valid_queryparam(param):
	return param != '' and param is not None


def contact(request):
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
	
	if is_valid_queryparam(name) and is_valid_queryparam(email) and is_valid_queryparam(message):
		c = Contact(name=name, email=email, telephone=phone, subject=subject, message=message)
		c.save()
		return render(request, 'core/thankyou.html')

	context = {
		'regions' : regions,
	}
	return render(request, 'core/x_contact.html', context)