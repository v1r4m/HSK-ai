from django.shortcuts import render, get_object_or_404
from .models import Prompt
from adrf.views import APIView
import os
from openai import AsyncOpenAI
from decouple import config
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def prompt(request):
    prompts = Prompt.objects.filter().order_by('grade', 'type', 'index')
    return render(request, 'prompt/prompt.html', {'prompts':prompts})

def ai(request, pk):
    prompt = get_object_or_404(Prompt, index=pk)
    return render(request, 'prompt/ai.html', {'prompt': prompt})

class ChatGPTAPI(APIView):
    async def post(self, request, format=None):
        OPENAI_API_KEY = config("OPENAI_KEY")
        prompt = request.data['prompt']
        client = AsyncOpenAI(api_key=OPENAI_API_KEY)
        chat_completion = await client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "HSK에는 다음과 같은 빈칸에 알맞은 단어 넣기 문제 유형이 있습니다. \
                         男：你 （ ）他 ？他是谁 ？ 女：他是我的学生 。\
                            정답은 是 입니다. 이를 json 형식으로 표현하면 다음과 같습니다. \
                        {'question_and_answer_with_blank':'男：你 （ ）他 ？他是谁 ？ 女：他是我的学生 。','word_in_blank':'是'} \
                            위 유형처럼, 다음 지문을 이용하여 새로운 문제를 만들고 json 형태로 응답하시오. 답변에는 json만 있어야 합니다." + prompt + "\n",
                }
            ],
            model="gpt-3.5-turbo",
        )
        response = chat_completion.choices[0].message.content
        return Response(response, status=status.HTTP_200_OK)