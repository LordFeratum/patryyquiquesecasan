from django.views.generic import FormView

from web.forms import UserForm


class Home(FormView):
    template_name = 'index.html'
    form_class    = UserForm
