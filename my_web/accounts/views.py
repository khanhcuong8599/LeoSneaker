'''from django.shortcuts import render
from django.contrib.auth import login, get_user_model, logout
from django.http import HttpResponseRedirect
#from .forms import UserCreationForm, UserLoginForm'''
from django.views.generic import CreateView, FormView
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .forms import LoginForm, RegisterForm, GuestForm
from .models import GuestEmail

def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        email = form.cleaned_data.get("email")
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id']= new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("register")
    return redirect("register")

class LoginView(FormView):
    form_class = LoginForm
    success_url = "/"
    template_name = "login.html"

    def form_invalid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        else:
            print("ERROR")

        return super(LoginView, self).form_invalid(form)

def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('core:home')
    form = LoginForm()
    return  render(request,'login.html',{'form':form}
    )

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = 'login'

User = get_user_model()



def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        form.save()

    return render(request, 'register.html', context)



def log_out(request):
    logout(request)
    return redirect('core:home')

