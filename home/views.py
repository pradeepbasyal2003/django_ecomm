from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import View
# Create your views here.
from .models import *
class Base(View):
    views = {}
class HomeView(Base):

    def get(self,request):
        self.views['categories'] = Category.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['reviews'] = CustumerReview.objects.all()
        self.views['hots'] = Product.objects.filter(labels = 'hot')
        self.views['news'] = Product.objects.filter(labels = 'new')

        return render(request,'index.html',self.views)


class CategoryView(Base):

    def get(self,request,slug):
        cat_id = Category.objects.get(slug = slug).id
        self.views['cat_products'] = Product.objects.filter(category_id = cat_id)
        self.views['brands'] = Brand.objects.all()
        self.views['sales'] = Product.objects.filter(labels = 'sale')
        return render(request , 'category.html' ,self.views)

class BrandView(Base):


    def get(self,request,slug):
        brand_id = Brand.objects.get(slug = slug).id
        self.views['brand_products'] = Product.objects.filter(brand_id = brand_id)
        self.views['categories'] = Category.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['sales'] = Product.objects.filter(labels='sale')

        return render(request , 'brand.html' ,self.views)


class ProductDetail(Base):

    def get(self,request,slug):
        self.views['product_detail'] = Product.objects.filter(slug = slug)
        product_category = Product.objects.get(slug=slug).category_id
        self.views['related_products'] = Product.objects.filter(category_id = product_category)
        return render(request,'product-detail.html',self.views)

class SearchView(Base):

    def get(self, request):
        if request.method == "GET":
            query = request.GET['query']
            if query != "":
                self.views['search_products'] = Product.objects.filter(name__icontains = query)
            else:
                redirect('/')

        self.views['categories'] = Product.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['sales'] = Product.objects.filter(labels='sale')

        return render(request, 'search.html', self.views)


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.error(request , "the username is already taken")
                return redirect("/signup")
            elif User.objects.filter(email = email).exists():
                messages.error(request , "the email is already in use.")
                return redirect('/signup')
            else:
                data = User.objects.create_user(
                    first_name = fname,
                    last_name = lname,
                    email = email,
                    username = username,
                    password= password,
                )
                data.save()
        else:
            messages.error(request , " the passwords do no match.")
            return redirect('/signup')
    return render(request,'signup.html')