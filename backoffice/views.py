from django.shortcuts import render, redirect

# Create your views here.
from backoffice.forms import *
from backoffice.models import *


def index(request):
    return render(request, 'index.html')

# ------------------------------------------------------------------------------------------------------------------
# Views CRUD pais


def pais_list(request):
    ctx = {'object_list': Pais.objects.all()}
    return render(request, 'pais/list.html', ctx)


def pais_add(request):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('pais_list')

    ctx = {'form': PaisForm()}
    return render(request, 'pais/add.html', ctx)


def pais_edit(request, pk):
    pais = Pais.objects.get(pk=pk)
    if request.method == 'POST':
        form = PaisForm(request.POST, instance=pais)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('pais_list')

    ctx = {'form': PaisForm(instance=pais)}
    return render(request, 'pais/edit.html', ctx)


def pais_delete(request, pk):
    pais = Pais.objects.get(pk=pk)
    if request.method == 'POST':
        pais.delete()
        return redirect('pais_list')

    ctx = {'object': pais}
    return render(request, 'pais/delete.html', ctx)


def pais_detail(request, pk):
    pais = Pais.objects.get(pk=pk)
    ctx = {'object': pais}

    return render(request, 'pais/detail.html', ctx)

# ------------------------------------------------------------------------------------------------------------------
# Views CRUD departamento


def departamento_list(request):
    ctx = {'object_list': Departamento.objects.all()}
    return render(request, 'departamento/list.html', ctx)


def departamento_add(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('departamento_list')

    ctx = {'form': DepartamentoForm()}
    return render(request, 'departamento/add.html', ctx)


def departamento_edit(request, pk):
    departamento = Departamento.objects.get(pk=pk)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('departamento_list')

    ctx = {'form': DepartamentoForm(instance=departamento)}
    return render(request, 'departamento/edit.html', ctx)


def departamento_delete(request, pk):
    departamento = Departamento.objects.get(pk=pk)
    if request.method == 'POST':
        departamento.delete()
        return redirect('departamento_list')

    ctx = {'object': departamento}
    return render(request, 'departamento/delete.html', ctx)


def departamento_detail(request, pk):
    departamento = Departamento.objects.get(pk=pk)
    ctx = {'object': departamento}

    return render(request, 'departamento/detail.html', ctx)

# ------------------------------------------------------------------------------------------------------------------
# Views CRUD provincia


def provincia_list(request):
    ctx = {'object_list': Provincia.objects.all()}
    return render(request, 'provincia/list.html', ctx)


def provincia_add(request):
    if request.method == 'POST':
        form = ProvinciaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('provincia_list')

    ctx = {'form': ProvinciaForm()}
    return render(request, 'provincia/add.html', ctx)


def provincia_edit(request, pk):
    provincia = Provincia.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProvinciaForm(request.POST, instance=provincia)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('provincia_list')

    ctx = {'form': ProvinciaForm(instance=provincia)}
    return render(request, 'provincia/edit.html', ctx)


def provincia_delete(request, pk):
    provincia = Provincia.objects.get(pk=pk)
    if request.method == 'POST':
        provincia.delete()
        return redirect('provincia_list')

    ctx = {'object': provincia}
    return render(request, 'provincia/delete.html', ctx)


def provincia_detail(request, pk):
    provincia = Provincia.objects.get(pk=pk)
    ctx = {'object': provincia}

    return render(request, 'provincia/detail.html', ctx)


# ------------------------------------------------------------------------------------------------------------------
# Views CRUD distrito


def distrito_list(request):
    ctx = {'object_list': Distrito.objects.all()}
    return render(request, 'distrito/list.html', ctx)


def distrito_add(request):
    if request.method == 'POST':
        form = DistritoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('distrito_list')

    ctx = {'form': DistritoForm()}
    return render(request, 'distrito/add.html', ctx)


def distrito_edit(request, pk):
    distrito = Distrito.objects.get(pk=pk)
    if request.method == 'POST':
        form = DistritoForm(request.POST, instance=distrito)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('distrito_list')

    ctx = {'form': DistritoForm(instance=distrito)}
    return render(request, 'distrito/edit.html', ctx)


def distrito_delete(request, pk):
    distrito = Distrito.objects.get(pk=pk)
    if request.method == 'POST':
        distrito.delete()
        return redirect('distrito_list')

    ctx = {'object': distrito}
    return render(request, 'distrito/delete.html', ctx)


def distrito_detail(request, pk):
    distrito = Distrito.objects.get(pk=pk)
    ctx = {'object': distrito}

    return render(request, 'distrito/detail.html', ctx)


# ------------------------------------------------------------------------------------------------------------------
# Views CRUD estacionamiento


def estacionamiento_list(request):
    ctx = {'object_list': Estacionamiento.objects.all()}
    return render(request, 'estacionamiento/list.html', ctx)


def estacionamiento_add(request):
    if request.method == 'POST':
        form = EstacionamientoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('estacionamiento_list')

    ctx = {'form': EstacionamientoForm()}
    return render(request, 'estacionamiento/add.html', ctx)


def estacionamiento_edit(request, pk):
    estacionamiento = Estacionamiento.objects.get(pk=pk)
    if request.method == 'POST':
        form = EstacionamientoForm(request.POST, instance=estacionamiento)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('estacionamiento_list')

    ctx = {'form': EstacionamientoForm(instance=estacionamiento)}
    return render(request, 'estacionamiento/edit.html', ctx)


def estacionamiento_delete(request, pk):
    estacionamiento = Estacionamiento.objects.get(pk=pk)
    if request.method == 'POST':
        estacionamiento.delete()
        return redirect('estacionamiento_list')

    ctx = {'object': estacionamiento}
    return render(request, 'estacionamiento/delete.html', ctx)


def estacionamiento_detail(request, pk):
    estacionamiento = Estacionamiento.objects.get(pk=pk)
    ctx = {'object': estacionamiento}

    return render(request, 'estacionamiento/detail.html', ctx)