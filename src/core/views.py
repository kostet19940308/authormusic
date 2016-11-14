from django.shortcuts import render
from django.urls import reverse
from .models import User
from .forms import RegistrationForm
from django.shortcuts import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.views.generic import DetailView, UpdateView, CreateView


class UserView(DetailView):
    model = User
    template_name = "user.html"
    context_object_name = 'user_account'
    slug_field = 'username'

    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)
        context['profile'] = self.request.user
        return context


class UserEdit(UpdateView):
    model = User
    template_name = 'user_edit.html'
    fields = ('email', 'first_name', 'last_name', 'avatar')
    slug_field = 'username'

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)


class RegisterView(CreateView):
    model = User
    template_name = 'registration/registration_form.html'
    form_class = RegistrationForm

    def get_success_url(self):
        return reverse('mainpage:login')


def home(request):
    return render(request, 'home.html')