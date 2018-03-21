from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from produtos.models import Produto
from vendas.models import Venda
from .forms import PersonForm
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.utils import timezone
from django.urls import reverse_lazy


@login_required
def persons_list(request):
    persons = Person.objects.all()

    return render(
        request, 'person.html', {'persons': persons})


@login_required
def persons_new(request):
    if not request.user.has_perm('clientes.add_person'):
        return HttpResponse('Nao autorizado')
    elif not request.user.is_superuser:
        return HttpResponse('Nao e superusuario')

    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'person': person})


class PersonList(LoginRequiredMixin, ListView):
    model = Person


class PersonDetail(LoginRequiredMixin, DetailView):
    model = Person

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Person.objects.select_related('doc').get(id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['vendas'] = Venda.objects.filter(
            pessoa_id=self.object.id)
        return context


class PersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = '/clientes/person_list'


class PersonUpdate(LoginRequiredMixin, UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('person_list_cbv')


class PersonDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('clientes.deletar_clientes',)

    model = Person
    success_url = reverse_lazy('person_list_cbv')


class ProdutoBulk(View):
    def get(self, request):
        produtos = ['Banana', 'Maca', 'Limao', 'Laranja', 'Pera', 'Melancia']
        list_produtos = []

        for produto in produtos:
            p = Produto(descricao=produto, preco=10)
            list_produtos.append(p)

        Produto.objects.bulk_create(list_produtos)

        return HttpResponse('Funcionou')
