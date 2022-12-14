import imp
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from .forms import ReviewForm
from .forms import Review
#from .models import Review
# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
    
        return render(request, "reviews/review.html",{
        "form" : form
    })

    def post(self, request):
        form = ReviewForm(request.POST)

        if  form.is_valid():

            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews/review.html",{
        "form" : form
          })

class ThankYouView(TemplateView):          
    template_name = "reviews/thank_you.html"
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context

class ReviewsListView(TemplateView):
    template_name: str = "reviews/review_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context