from django.shortcuts import render, get_object_or_404
from .models import Prompt

# Create your views here.
def prompt(request):
    prompts = Prompt.objects.filter().order_by('grade', 'type', 'index')
    return render(request, 'prompt/prompt.html', {'prompts':prompts})

def ai(request, pk):
    prompt = get_object_or_404(Prompt, index=pk)
    return render(request, 'prompt/ai.html', {'prompt': prompt})