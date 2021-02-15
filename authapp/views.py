from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Sum
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from basket.models import Basket
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from authapp.models import user


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('Index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'authapp/login.html', context)



#
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Пользователь зарегистрирован')
#             return HttpResponseRedirect(reverse('auth:login'))
#     else:
#         form = UserRegisterForm()
#
#     context = {'form': form}
#
#     return render(request, 'authapp/register.html', context)

class UserRegisterView(CreateView):
    model = user
    template_name = 'authapp/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('auth:login')



def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('Index'))

@login_required
def profile(request):

    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:profile'))
    else:
        form = UserProfileForm(instance=request.user)




    context = {'form': form,
               'baskets': Basket.objects.filter(user=request.user),



               }
    return render(request, 'authapp/profile.html', context)