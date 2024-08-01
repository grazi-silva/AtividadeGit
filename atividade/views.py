from django.shortcuts import render

# Create your views here.

def view_kayane(request):
    nome = 'kayane'
    return render(request, 'atividade/template-kayane.html',
                  context={'nome': nome}
                  )
