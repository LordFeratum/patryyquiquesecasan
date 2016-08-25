from django.views.generic.edit import FormView
from django.views.generic import View
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from web.models import Photo

from django.contrib.auth import authenticate

from web.forms import UserForm
from web.forms import PhotoForm

from cloudinary.forms import cl_init_js_callbacks


class Home(FormView):
    template_name = 'index.html'
    form_class    = UserForm
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data['username'].encode('utf-8')
        name = form.cleaned_data['nombre'].encode('utf-8')
        surname = form.cleaned_data['apellidos'].encode('utf-8')
        email = form.cleaned_data['email']
        password = form.cleaned_data['password'].encode('utf-8')

        new_user = User.objects.create_user(username, email, password)
        new_user.first_name = name
        new_user.last_name = surname
        new_user.save()

        logged_user = authenticate(username=username, password=password)

        return super(Home, self).form_valid(form)

    def form_invalid(self, form):
        return super(Home, self).form_invalid(form)


class Gallery(View):
    def get(self, request):
        images = Photo.objects.all()

        context = {'form': PhotoForm(),
                   'thumbmail': dict(crop="thumb", gravity="face"),
                   'images': images}

        return render(request, 'gallery.html', context)

    def post(self, request):
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return redirect('/gallery')

# class Gallery(FormView):
#     template_name = 'gallery.html'
#     form_class    = PhotoForm
#     success_url   = '/'
#
#     def form_valid(self, form):
#         form.save()
#
#         return super(Gallery, self).form_valid(form)