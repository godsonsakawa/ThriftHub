from django.shortcuts import render, get_object_or_404
from .cart import Cart
from Thrifthub.models import Product
from django.http import JsonResponse


# Create your views here.
def cart_summary(request):
    return render(request, 'cart.html')


def cart_add(request):
    # Get the cart
    cart = Cart(request)

    # Check if request method is POST
    if request.POST.get('action') == 'post':
        # Get product_id from the POST data
        product_id = int(request.POST.get('product_id'))
        # Default to 1 if not provided
        quantity = int(request.POST.get('quantity', 1))

        # lookup product in the database
        product = get_object_or_404(Product, id=product_id)

        # Save the product to the cart session
        cart.add(product=product, quantity=quantity)

        # Get Cart Quantity
        cart_quantity = cart.__len__()

        # Return a response
        # response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'quantity: ': cart_quantity})
        return response


def cart_delete(request, product_id):
    # Get the cart
    cart = Cart(request)

    # Remove the specified product from the cart
    cart.remove(product_id)

    # Get Cart Quantity
    cart_quantity = len(cart)

    # Return a response
    response = JsonResponse({'quantity': cart_quantity})
    return response


def cart_update(request):
    pass
