from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Category, Product
from django.contrib import messages
from .models import Profile

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

@login_required
def user_profile(request):
    return render(request, 'account/user_profile.html')

@login_required
def user_edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.add_message(request, messages.INFO, 'Профиль успешно обновлен')
            return redirect('user_edit')
        else:
            messages.add_message(request, messages.WARNING, 'Ошибка при обновлении вашего профиля')
            return redirect('user_edit')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
            'account/user_edit.html',
            {'user_form': user_form,
            'profile_form': profile_form})

def register(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            user_form = UserRegistrationForm(request.POST)
            if user_form.is_valid():
                # Create a new user object but avoid saving it yet
                new_user = user_form.save(commit=False)
                # Set the chosen password
                new_user.set_password(user_form.cleaned_data['password'])
                # Save the User object
                new_user.save()
                profile = Profile.objects.create(user=new_user)
                return render(request, 'account/register_done.html', {'new_user': new_user})
        else:
            return redirect('home')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/detail.html',
                  {'product': product})