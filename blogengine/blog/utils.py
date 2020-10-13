from django.shortcuts import render, get_object_or_404, redirect

from .models import *
from .forms import CommentForm

class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        if self.model == Post:
            form = CommentForm
            return render(request, self.template, context={self.model.__name__.lower(): obj, 'comment_form': form, 'admin_object': obj,
            'detail': True})
        return render(request, self.template, context={self.model.__name__.lower(): obj, 'admin_object': obj,
        'detail': True})


    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = CommentForm(request.POST)
        if bound_form.is_valid():
            new_comment = Comment(user = request.user.first_name,  body = bound_form.cleaned_data['body'], post = obj)
            #print(request.user)
            new_comment.save()
        return render(request, self.template, context={self.model.__name__.lower(): obj, 'comment_form': CommentForm, 'admin_object': obj,
        'detail': True})



class ObjectCreateMixin:
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={'form': form})


    def post(self, request):
        bound_form = self.model_form(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact = slug)
        bound_form = self.model_form(instance = obj)
        return render(request, self.template, context = {'form': bound_form, self.model.__name__.lower(): obj})


    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact = slug)
        bound_form = self.model_form(request.POST, instance = obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context = {'form': bound_form, self.model.__name__.lower(): obj})



class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None


    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact = slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact = slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))

