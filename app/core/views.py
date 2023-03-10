# app/core/views.py

# Django modules
# from math import prod 
# from stripe import Review 
from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Avg 

# Locals
from app.core.models import Product, Category, Vendor, ProductReview
from taggit.models import Tag  

# Create your views here.

# Homepage
def index(request):
	# products = Product.objects.all().order_by('-id')
	products = Product.objects.filter(status_choice='published', featured=True)
	# print(products)
	context = {
		'products':products,
	}
	return render(request, 'app/core/index.html', context)


# Product List
def product_list_view(request):
	products = Product.objects.all()
	# print(products)
	context = {'products':products}
	return render(request, 'app/core/product_list.html', context)


# Product Detail
def product_detail_view(request, any):
	# Get product by pid
	product = Product.objects.get(pid=any)
	# product = get_object_or_404(Product, vid=vid) # this similar to the above
	# print(product)

	# # Related products - part 1
	# rel_products = Product.objects.filter(category=product.category)
	# print(rel_products)

	# Related products - part 2 
	rel_products = Product.objects.filter(category=product.category).exclude(pid=any)[:4]
	print(rel_products)

	# Get related products
	products = product.related_products.all()
	# print(products)

	# Getting all review of each product
	reviews = ProductReview.objects.filter(product=product).order_by('-created')

	# Getting average review
	average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))


	context = {
		'product':product, 
		'products':products,
		'rel_products':rel_products,
		'reviews':reviews,
		'average_rating':average_rating,
	}
	return render(request, 'app/core/product_detail.html', context)


# Category List
def category_list_view(request):
	categories = Category.objects.all()
	# print(categories)
	context = {'categories':categories}
	return render(request, 'app/core/category_list.html', context)


# Product By Category
def product_by_category_list_view(request, cat_id):
	category_based_id = Category.objects.get(cid=cat_id)
	products = Product.objects.filter(status_choice='published', category=category_based_id)
	context = {
		'category': category_based_id,
		'products': products,
	}
	return render(request, 'app/core/product_by_category_list.html', context)


# Vendor List
def vendor_list_view(request):
	vendors = Vendor.objects.all()
	# print(vendors)
	context = {
		'vendors':vendors
	}
	return render(request, 'app/core/vendor_list.html', context)


# Vendor Detail
def vendor_detail_view(request, vid):
	vendor = Vendor.objects.get(vid=vid)
	# print(vendor)
	products = Product.objects.filter(vendor=vendor, status_choice='published')
	# print(products)
	context = {
		'vendor':vendor,
		'products':products,
	}
	return render(request, 'app/core/vendor_detail.html', context)


def tag_list_view(request, tag_slug=None):
	products = Product.objects.filter(status_choice='published').order_by('-id')

	tag = None 
	if tag_slug:
		 # If there is slug in the Tags model
		 # then, slug is equal to what ever we passed in the tag_slug
		 # Example: http://127.0.0.1:8000/products/tag/lotion
		tag = get_object_or_404(Tag, slug=tag_slug)
		# print(tag)
		# Get all products from Product table which have tags in it and put it in products variable
		products = products.filter(tags__in=[tag])
		# print(products)

	context = {
		'tag':tag,
		'products':products,
	}

	return render(request, 'app/core/tag.html', context)