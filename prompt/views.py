from django.shortcuts import render, get_object_or_404
from .models import Prompt
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
def prompt(request):
    prompts = Prompt.objects.filter().order_by('grade', 'type', 'index')
    return render(request, 'prompt/prompt.html', {'prompts':prompts})

def ai(request, pk):
    prompt = get_object_or_404(Prompt, index=pk)
    return render(request, 'prompt/ai.html', {'prompt': prompt})

class ChatGPTAPI(APIView):
    def post(self, request, format=None):
        prompt = request.data['prompt']
        response = prompt
        return Response(response, status=status.HTTP_200_OK)