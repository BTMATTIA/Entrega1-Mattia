from django import forms

class TerrorForm(forms.Form):
    titulo= forms.CharField(label="Nombre Pelicula", max_length=50)
    valoracion=forms.IntegerField(label="Valoracion Pelicula",max_value=10)

class ComediaForm(forms.Form):
    titulo= forms.CharField(label="Nombre Pelicula", max_length=50)
    valoracion= forms.CharField(label="Valoracion Pelicula", max_length=2)

class AccionForm(forms.Form):
    titulo= forms.CharField(label="Nombre Pelicula", max_length=50)
    valoracion= forms.CharField(label="Valoracion Pelicula", max_length=2)
    