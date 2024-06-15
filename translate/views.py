from django.shortcuts import render
from googletrans import Translator
# Create your views here.
translator = Translator()
def translate(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        lang = translator.detect(query)
        if lang.lang == 'uz':
            text_uz = query
            text_en = translator.translate(query, dest='en').text
        elif lang.lang == 'en':
            text_uz = translator.translate(query, dest='uz').text
            text_en = query
        else:
            text_uz = query
            text_en = text_uz
        data = {
            'text_uz': text_uz,
            'text_en': text_en,
            'text': query
        }
        return render(request, 'translate.html',  {'data': data})
    else:
        return render(request, 'translate.html')


