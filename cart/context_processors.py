from .cart import Cart


# create context processor so that our cart can work on all pages
def cart(request):
    # Return a dictionary containing the 'cart' variable, which is an instance of the Cart class
    return {'cart': Cart(request)}


# Context processors in Django allow you to add variables to the context of all templates,
# making those variables available globally in your templates.
