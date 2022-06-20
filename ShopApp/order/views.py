from django.shortcuts import redirect, render
from order.models import OrderItem
from order.forms import OrderCreateForm
from cart.models import Cart
from order.tasks import order_created


# Create your views here.
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            order_created.delay(order.id)
            return redirect('home')
    else:
        form = OrderCreateForm
        return render(request, 'order/create.html',
            {'cart': cart,
            'form': form}
        )
