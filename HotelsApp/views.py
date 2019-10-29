from django.contrib.auth.views import LoginView, auth_login
from django.shortcuts import render, redirect
from django.views.generic.base import logger

from .forms import *


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def login_index(request):
    return render(request, 'login_index.html', {})

def about(request):
    return render(request, 'about.html', {})

def accomodation(request):
    return render(request, 'accommodation.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def blogsingle(request):
    return render(request, 'blog-single.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def elements(request):
    return render(request, 'elements.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

class CustomLoginView(LoginView):
    """
    Custom login view.
    """
    form_class = LoginForm
    template_name = 'HotelsApp/accounts/login.html'
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and self.request.user.is_staff: # and has_2fa(self.request):
            return redirect('{}'.format(self.request.GET.get('next', 'HotelsApp:login_index')))
        return super(CustomLoginView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        if self.request.user.is_staff: # and not has_2fa(self.request):
            logger.info('is staff but does not have 2FA, redirecting to Authority account creator')
            auth_login(self.request, form.get_user(), backend='django.contrib.auth.backends.ModelBackend')
            return redirect('2fa_register')
        return super(CustomLoginView, self).form_valid(form)


def user_profile(request):
    return render(request, 'HotelsApp/accounts/user_profile.html', {})

def login(request):
    return render(request, 'HotelsApp/accounts/login.html', {})

def logout(request):
    return render(request, 'HotelsApp/accounts/logged_out.html', {})

def password_reset_complete(request):
    return render(request, 'HotelsApp/accounts/password_reset_complete.html', {})

def password_reset_confirm(request):
    return render(request, 'HotelsApp/accounts/password_reset_confirm.html', {})

def password_reset_done(request):
    return render(request, 'HotelsApp/accounts/password_reset_done.html', {})

def password_reset_email(request):
    return render(request, 'HotelsApp/accounts/password_reset_email.html', {})

def password_reset_form(request):
    return render(request, 'HotelsApp/accounts/password_reset_form.html', {})
