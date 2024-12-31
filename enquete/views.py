from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

# Create your views here.

def index(request):

    ultima_lista_perguntas = Question.objects.order_by("-pub_date")[:5]

    context = {
        "ultima_lista_perguntas": ultima_lista_perguntas,
    }

    return render(request, "enquete/index.html", context)

# Detalhes da pergunta
def detail(request, question_id):
    return HttpResponse("Essa é a pergunta %s." % question_id)

# Resultados da pergunta
def results(request, question_id):
    response = "Esses são os resultados da pergunta %s."
    return HttpResponse(response % question_id)

# Voto referente à pergunta
def vote(request, question_id):
    return HttpResponse("Você está votando na pergunta %s." % question_id)