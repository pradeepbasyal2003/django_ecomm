from django.shortcuts import render
from django.views import View
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
        return render(request,'index.html',self.views)