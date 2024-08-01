from django.shortcuts import render

# Create your views here.
def view_grazi(request):
    nome = 'Grazi'
    return render (request, 'atividade/template-grazi.html', 
                   context= {'nome': nome}
                   )
