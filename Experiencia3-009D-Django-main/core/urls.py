from django.urls import path 
from .views import formularioRegistro, indexd, QuienesSomos, contacto, galeria, peliculasAPI, formularioRegistro, listadocli, listadoproduc, formcliente, formproducto, formmodcliente, formmodproducto, formdelcliente, formdelproducto

urlpatterns =[
    path ('', indexd, name="indexd"),

    path ('QuienesSomos', QuienesSomos, name="QuienesSomos"),

    path ('contacto', contacto, name="contacto"),

    path ('galeria', galeria, name="galeria"),

    path ('peliculasAPI', peliculasAPI, name="peliculasAPI"),

    path ('formularioRegistro', formularioRegistro, name="formularioRegistro"),

    path ('listadocli', listadocli, name="listadocli"),

    path ('listadoproduc', listadoproduc, name="listadoproduc"),

    path ('formcliente', formcliente, name="formcliente"),

    path ('formproducto', formproducto, name="formproducto"),
    
    path ('formmodcliente/<id>', formmodcliente, name="formmodcliente"),
     
    path ('formmodproducto/<id>', formmodproducto, name="formmodproducto"),

    path('formdelcliente/<id>', formdelcliente, name="formdelcliente"),

    path('formdelproducto/<id>', formdelproducto, name="formdelproducto"),


]



