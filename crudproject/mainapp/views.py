from django.shortcuts import render, redirect
from .models import Item
# Create your views here.

def index(request):
    return render(request, 'index.html',{
        'item': Item.objects.all()
    })

def detailsView(request,id):
    return render(request, 'detail.html', {
        'forms': Item.objects.get(pk = id)
     })

def addView(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        form = Item(
            name =name,
            description= description
        )
        form.save()
        return redirect('/')
    return render(request, 'add.html')


def updateView(request, id):
    item1 = Item.objects.get(pk=id)
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        item1.name = name
        item1.description = description
        item1.save()
        return redirect('/')
    return render(request, 'update.html', {'item1': item1})

def deleteView(request,id):
    item = Item.objects.get(pk=id)
    item.delete()
    return redirect('/')

