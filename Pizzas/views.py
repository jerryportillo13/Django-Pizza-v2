from django.shortcuts import render, redirect
from .models import *
from .forms import *

#write code/function to interact with DB and connect to the html templates

# Create your views here.
def index(request):
    return render(request, 'Pizzas/index.html')

#all pizzas
def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')
    context = {'all_pizzas':pizzas}
    return render(request, 'Pizzas/pizzas.html', context)


#individual pizzas
def pizza(request, pizza_id):
    p = Pizza.objects.get(id=pizza_id)
    toppings = Topping.objects.filter(pizza=p)
    comment = Comment.objects.filter(pizza=p)
    context = {'pizza':p, 'toppings':toppings, 'comment':comment}
    return render(request, 'Pizzas/pizza.html', context)



#comments
def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()
            return redirect('Pizzas:pizza',pizza_id=pizza_id)

    context = {'form':form, 'pizza':pizza}
    return render(request, 'Pizzas/new_comment.html',context)




