from django.shortcuts import render
from .models import Terror, Comedia, Accion
from django.http import HttpResponse
from AppEI.forms import TerrorForm, ComediaForm, AccionForm

# Create your views here.

def inicio(request):
    return render (request, "AppEI/inicio.html")

def terrorFormulario(request): 
    if request.method=="POST":
        form= TerrorForm(request.POST) 
        
        if form.is_valid():
            informacion=form.cleaned_data 
            
            titulo=informacion["titulo"] 
            valoracion=informacion["valoracion"] 
            terror= Terror(titulo=titulo, valoracion=valoracion)
            terror.save()
            terrores=Terror.objects.all()
            return render (request, "AppEI/leerTerror.html", {"Peliculas": terrores, "mensaje": "Pelicula guardada correctamente"})
        else:
            return render (request, "AppEI/TerrorFormulario.html", {"form": form, "mensaje": "Información no válida"})

    else: 
        formulario= TerrorForm()
        return render (request, "AppEI/TerrorFormulario.html", {"form": formulario})


def comediaFormulario(request):  
    if request.method=="POST":
        form= ComediaForm(request.POST) 
       
        if form.is_valid():
            informacion=form.cleaned_data 
            
            titulo=informacion["titulo"]
            valoracion=informacion["valoracion"]            
            comedia= Comedia(titulo=titulo, valoracion=valoracion)
            comedia.save()
            comedias=Comedia.objects.all()
            return render (request, "AppEI/leerComedia.html", {"Comedias": comedias, "mensaje": "Comedia guardada correctamente"})
        else:
            return render (request, "AppEI/ComediaFormulario.html", {"form": form, "mensaje": "Información no válida"})

    else: 
        formulario= ComediaForm()
        return render (request, "AppEI/ComediaFormulario.html", {"form": formulario})


def accionFormulario(request): 
    if request.method=="POST":
        form= AccionForm(request.POST) 
        
        if form.is_valid():
            informacion=form.cleaned_data 
            
            titulo=informacion["titulo"]
            valoracion=informacion["valoracion"]
            accion= Accion(titulo=titulo, valoracion=valoracion)
            accion.save()
            Acciones=Accion.objects.all()
            return render (request, "AppEI/leerAccion.html", {"Peliculas": Acciones, "mensaje": "Pelicula guardada correctamente"})
        else:
            return render (request, "AppEI/AccionFormulario.html", {"form": form, "mensaje": "Información no válida"})

    else: 
        formulario= AccionForm()
        return render (request, "AppEI/AccionFormulario.html", {"form": formulario})


def busquedaTerror(request):
    return render(request, "AppEI/busquedaTerror.html")

def buscar(request):
    
    titulo=request.GET["titulo"]
    if titulo!="":
        terrores= Terror.objects.filter(titulo__icontains=titulo) 
        return render (request, "AppEI/resultadosBusqueda.html", {"Peliculas": terrores})
    else:
        return render (request, "AppEI/busquedaTerror.html", {"mensaje": "Ingresa una pelicula para buscar!"})


def leerTerror(request):
    terrores=Terror.objects.all()
    return render (request, "AppEI/leerTerror.html", {"Peliculas": terrores})

def eliminarTerror(request, id):
    terror=Terror.objects.get(id=id)
    terror.delete()
    terrores=Terror.objects.all()
    return render (request, "AppEI/leerTerror.html", {"Peliculas": terrores, "mensaje": "Pelicula eliminada correctamente"})

def editarTerror(request, id):
    terror=Terror.objects.get(id=id)
    if request.method=="POST":
        form= TerrorForm(request.POST)        
        if form.is_valid():
            info=form.cleaned_data 
            terror.titulo=info["titulo"]
            terror.valoracion=info["valoracion"]   
            terror.save()
            terrores=Terror.objects.all()
            return render (request, "AppEI/leerTerror.html", {"Peliculas": terrores, "mensaje": "Pelicula editada correctamente"})
        pass
    else:
        formulario=TerrorForm(initial={"titulo":terror.titulo, "valoracion":terror.valoracion,})
        return render (request, "AppEI/editarTerror.html", {"form": formulario, "Pelicula": terror})


def leerComedia(request):
    comedias=Comedia.objects.all()
    return render (request, "AppEI/leerComedia.html", {"Comedias": comedias})

def eliminarComedia(request, id):
    comedia=Comedia.objects.get(id=id)
    comedia.delete()
    comedias=Comedia.objects.all()
    return render (request, "AppEI/leerComedia.html", {"Comedias": comedias, "mensaje": "Comedia eliminada correctamente"})

def editarComedia(request, id):
    comedia=Comedia.objects.get(id=id)
    if request.method=="POST":
        form= ComediaForm(request.POST)        
        if form.is_valid():
            info=form.cleaned_data 
            comedia.titulo=info["titulo"]
            comedia.valoracion=info["valoracion"]            
            comedia.save()
            comedias=Comedia.objects.all()
            return render (request, "AppEI/leerComedia.html", {"Comedias": comedias, "mensaje": "Comedia editada correctamente"})
        pass
    else:
        formulario=ComediaForm(initial={"titulo":comedia.titulo, "valoracion":comedia.valoracion})
        return render (request, "AppEI/editarComedia.html", {"form": formulario, "comedia": comedia})


def leerAccion(request):
    acciones=Accion.objects.all()
    return render (request, "AppEI/leerAccion.html", {"Peliculas": acciones})

def eliminarAccion(request, id):
    accion=Accion.objects.get(id=id)
    accion.delete()
    acciones=Accion.objects.all()
    return render (request, "AppEI/leerAccion.html", {"Peliculas": acciones, "mensaje": "Pelicula eliminada correctamente"})

def editarAccion(request, id):
    accion=Accion.objects.get(id=id)
    if request.method=="POST":
        form= AccionForm(request.POST)       
        if form.is_valid():
            info=form.cleaned_data 
            accion.titulo=info["titulo"]
            accion.valoracion=info["valoracion"]  
            accion.save()
            acciones=Accion.objects.all()
            return render (request, "AppEI/leerAccion.html", {"Peliculas": acciones, "mensaje": "Pelicula editada correctamente"})
        pass
    else:
        formulario=AccionForm(initial={"titulo":accion.titulo, "valoracion":accion.valoracion})
        return render (request, "AppEI/editarAccion.html", {"form": formulario, "Pelicula": accion})
