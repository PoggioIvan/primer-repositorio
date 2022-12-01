import datetime
from django.http import HttpResponse
from django.template import Template, Context 
from django.template import loader



def nombres(request,nombre):
    return HttpResponse(f"hola {nombre} como estas?")

def calcular_anio_nacimiento(request,edad):
    anio_actual= datetime.datetime.today().year
    anio_nacimiento=anio_actual-int(edad)
    return HttpResponse(f'<h3> usted nacio en {anio_nacimiento} </h3>')

def saludo_pro(self, nombre):
    saludo= f'<title> super saludo a {nombre} </title> <h2>hola {nombre}</h2> <br> <br> <h3>bienvenido a mi pagina</h3>'
    return HttpResponse(saludo)
    
    """primera forma de hacer un template"""
def template1(self):
    mihtml= open(r"C:\Users\Usuario\Desktop\python\APUNTES\VSC\django1\dj1\plantillas\template1.html")
    plantilla= Template(mihtml.read())
    mihtml.close()
    micontexto= Context()
    documento= plantilla.render(micontexto)
    return HttpResponse(documento)

'''def template2(self):
    mihtml1= open(r"C:\Users\Usuario\Desktop\python\APUNTES\VSC\django1\dj1\plantillas\template2.html")
    plantilla1= Template(mihtml1.read())
    mihtml1.close()
    micontexto= Context()
    documento= plantilla1.render(micontexto)
    return HttpResponse(documento)'''

"""segunda forma de hacer un template"""
def template2(self):
    diccionario={'nombre':'ivan','apellido':'poggio'}
    plantilla1= loader.get_template("template2.html")
    documento= plantilla1.render(diccionario)
    return HttpResponse(documento)


