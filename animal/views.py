from django.shortcuts import render
from django.urls import reverse_lazy
from animal.models import Animal
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from animal.forms import AnimalForm
from animal.models import Animal

class AnimalList(ListView):
    model = Animal
    template_name = 'animal/animalList.html'
    paginate_by = 5    
    ordering = ['id']

class AnimalCreate(CreateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'animal/animalForm.html'
    success_url = reverse_lazy('animal_listar')

class AnimalUpdate(UpdateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'animal/animalForm.html'
    success_url = reverse_lazy('animal_listar')

class AnimalDelete(DeleteView):
    model = Animal
    template_name = 'animal/animalDelete.html'
    success_url = reverse_lazy('animal_listar')

