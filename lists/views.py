from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    # return HttpResponse('<html><title>To-Do lists</title><body><h1>To-Do</h1></body></html>')
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', '')
    })
