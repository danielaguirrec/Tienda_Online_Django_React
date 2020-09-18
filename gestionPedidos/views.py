from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioContacto

# Create your views here.

def busquedad_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
  #  mensaje = "Articulo buscado: %r "%request.GET["prd"]
    if request.GET["prd"]:
        producto = request.GET["prd"]
        if len(producto) > 20:
            mensaje= "Ha buscado con un string muy grande"
        else: 
            articulos = Articulos.objects.filter(nombre__icontains =producto)
            return render(request, "resultados_busqueda.html",{"articulos":articulos,"query":producto})
    else: 
        mensaje = "No enviaste nada "
    return HttpResponse(mensaje)

def contacto(request):
    if request.method=='POST':
        miFormulario = FormularioContacto(request.POST)
        if miFormulario.is_valid(): 
            infForm = miFormulario.cleaned_data
            send_mail(infForm['asunto'],
            infForm['mensaje'],
            infForm.get('email',''),['daniel.aguirrec@udea.edu.co'],)
            return render(request, "gracias.html")
    else:
        miFormulario = FormularioContacto()
    return render(request,"formulario_contacto.html",{"form":miFormulario})

        
"""to = request.POST['email']
subject = request.POST['Asunto']
message = request.POST['mensaje'] 
email_from = settings.EMAIL_HOST_USER 
print([to,])
# recipient_list =["daniel.aguirrec@udea.edu.co"]
send_mail(subject, message, email_from, [to])
return render(request,"gracias.html")
else:
    return render(request,"contacto.html")"""

