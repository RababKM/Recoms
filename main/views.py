from django.shortcuts import render
from main.models import Recommendation, Category
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Create your views here.


def home(request):
    context = {}
    categories = Category.objects.all()
    context['categories'] = categories
    recommendations = Recommendation.objects.all()
    context['recommendations'] = recommendations

    return render(request, 'home.html', context)


def category_detail(request, pk):
    context = {}
    category = Category.objects.get(pk=pk)
    context['category'] = category

    return render(request, 'category_detail.html', context)


def recommendation_detail(request, pk):
    context = {}
    recommendation = Recommendation.objects.get(pk=pk)
    context['recommendation'] = recommendation

    return render(request, 'recommendation_detail.html', context)


def category_list(request):
    context = {}
    categories = Category.objects.all()
    context['categories'] = categories

    return render(request, 'category_list.html', context)


def cat_recommendations(request, pk):
    context = {}
    category = Category.objects.get(pk=pk)
    context['category'] = category

    return render(request, 'cat_recoms_list.html', context)


def location(request, pk):
    context = {}
    recommendation = Recommendation.objects.get(pk=pk)
    context['recommendation'] = recommendation

    return render(request, 'location.html', context)

@csrf_exempt
def submit_email(request):
    name = request.POST.get("name", None)
    email = request.POST.get("email", None)
    phone = request.POST.get("phone", None)
    message = request.POST.get("message", None)
    send_mail('users messages - %s' % name, message, email, ['recoms.com@gmail.com'], fail_silently=False)

    return HttpResponse('success')
