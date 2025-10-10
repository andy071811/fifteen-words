from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy

from .models import Comment
from .forms import CommentForm

# Create your views here.

class Home(FormMixin, ListView):
    model = Comment
    template_name = 'home.html'
    context_object_name = 'comments'
    ordering = ['-id']
    paginate_by = 20
    form_class = CommentForm
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)