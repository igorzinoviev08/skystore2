from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        visiter = {}
        visiter['name'] = request.POST.get('name', None)
        visiter['phone'] = request.POST.get('phone', None)
        visiter['massage'] = request.POST.get('message', None)
        print(visiter)
    return render(request, 'catalog/contacts.html')
