from django.core import paginator
from django.shortcuts import render, redirect
from .models import Category, Photo,Banner
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
import random
from django.core.paginator import EmptyPage, PageNotAnInteger , Paginator
# Create your views here.

def home(request):
    category = request.GET.get('category')
    banner = list(Banner.objects.order_by('-pk').all())
    banner =  random.sample(banner, 4)
    

    if category == None:
        photos = Photo.objects.order_by('-pk').all()
        paginator = Paginator(photos,12)
        page = request.GET.get('page')
        page_photos = paginator.get_page(page)
        photos_count = photos.count()
    else:
        photos = Photo.objects.filter(category__name=category)
        paginator = Paginator(photos,12)
        page = request.GET.get('page')
        page_photos = paginator.get_page(page)
        photos_count = photos.count()
    categories = Category.objects.all()
    context = {'categories': categories, 'photos': page_photos,'pic_count':photos_count,"banner":banner}
    return render(request, 'photos/home.html', context)

def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('gallery')
    return render(request, 'photos/login_register.html', {'page': page})


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                login(request, user)
                return redirect('gallery')
    context = {'form': form, 'page': page}
    return render(request, 'photos/login_register.html', context)


@login_required(login_url='login')
def gallery(request):
    user = request.user
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.filter(user=user).order_by('-pk')
        photos_count = photos.count()
    else:
        photos = Photo.objects.filter(
            category__name=category, user=user).order_by('-pk')

    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos,"pic_count":photos_count}
    return render(request, 'photos/gallery.html', context)


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    photo.imgviiews+=1
    photo.save()
    photos = list(Photo.objects.order_by('-pk').all())
    photos =  random.sample(photos, 3)
    return render(request, 'photos/photo.html', {'photo': photo , 'photos':photos})


@login_required(login_url='login')
def updateview(request, pk):
    photo = Photo.objects.get(id=pk)
    photo.delete()
    return redirect('gallery')


@login_required(login_url='login')
def addPhoto(request):
    user = request.user
 

    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])

        for image in images:
             Photo.objects.create(
                category=category,
                user=user,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'photos/add.html', context)
