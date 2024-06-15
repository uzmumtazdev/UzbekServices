from django.shortcuts import render
from .transliterate import to_cyrillic, to_latin
# Create your views here.
def transliterate(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        if query.isascii():
            latin = query
            kiril = to_cyrillic(query)
        else:
            latin = to_latin(query)
            kiril = query
        data = {
            'latin': latin,
            'kiril': kiril,
            'text': query
        }
        return render(request, 'transliterate.html', {'data': data})
    else:
        return render(request, 'transliterate.html')
