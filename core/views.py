from django.shortcuts import render, HttpResponse,redirect
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


# Create your views here.

# def index(request):
#     item_list = Item.objects.all()
#     context = {
#         'item_list': item_list,
#     }
#     # template = loader.get_template('core/index.html')
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'core/index.html', context)

class IndexView(ListView):
    model = Item
    template_name = 'core/index.html'
    context_object_name = 'item_list'

class detail_view(DetailView):
    model = Item
    template_name = 'core/detail.html'

# def detail(request, item_id):
#     item = Item.objects.get(pk = item_id)
#     context = {
#         'item':item,
#     }
#     return render(request,'core/detail.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('core:index')
    
    return render(request,'core/item-form.html',{'form':form})

class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'core/item-form.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)


def update_item(request,id):
    item = Item.objects.get(id = id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('core:index')
    
    return render(request, 'core/item-form.html', {'form':form, 'item':item})


def delete_item(request, id):
    item = Item.objects.get(id = id)

    if request.method == 'POST':
        item.delete()
        return redirect('core:index')

    return render(request, 'core/item-delete.html',{'item': item})



   