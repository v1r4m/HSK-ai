from django.shortcuts import render
from .models import Prompt

# Create your views here.
def prompt(request):
    prompts = Prompt.objects.filter().order_by('grade', 'type', 'index')
    return render(request, 'prompt/prompt.html', {'prompts':prompts})