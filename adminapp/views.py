from django.shortcuts import render, HttpResponseRedirect
from authapp.models import user
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/index.html')

# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_read(request):
#     context = {
#         'users': user.objects.all()
#     }
#     return render(request, 'adminapp/admin-users-read.html', context)

class UserListView(ListView):
    model = user
    template_name = 'adminapp/admin-users-read.html'
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


#
# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#
#             return HttpResponseRedirect(reverse('admins:admin_users_read'))
#         else:
#             print(form.errors)
#     else:
#         form = UserAdminRegisterForm()
#
#     context = {'form': form}
#
#     return render(request, 'adminapp/admin-users-create.html', context)

class UserCreateView(CreateView):
    model = user
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)
#
# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_update(request, id=None):
#     user_id = user.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user_id)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users_read'))
#     else:
#         form = UserAdminProfileForm(instance=user_id)
#
#     context = {
#         'form': form,
#         'current_user': user_id
#     }
#
#     return render(request, 'adminapp/admin-users-update-delete.html', context)


class UserUpdateView(UpdateView):
    model = user
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - update data'
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_delete(request, id):
#     curent_user = user.objects.get(id=id)
#     # curent_user.delete() - полное удаление из базы данных
#     curent_user.is_active = False
#     curent_user.save()
#     return HttpResponseRedirect(reverse('admins:admin_users_read'))

class UserDeleteView(DeleteView):
    model = user
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@user_passes_test(lambda u: u.is_superuser)
def admin_active_user(requesy, id):
    curent_user = user.objects.get(id=id)
    curent_user.is_active = True
    curent_user.save()
    return HttpResponseRedirect(reverse('admins:admin_users_read'))