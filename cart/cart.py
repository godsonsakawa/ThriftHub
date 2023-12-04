from Thrifthub.models import Product


class Cart:
    def __init__(self, request):
        # Initialize the Cart instance with the request object
        self.session = request.session

        # Get the current session for the 'session_key'
        cart = self.session.get('session_key')

        # If the user is new, no session key! create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make the cart is available on all pages of a site
        self.cart = cart

        # add the cart.context_processor.cart to the settings.py
    def add(self, product, quantity):
        # Add a product to the cart
        product_id = str(product.id)

        # Check if the product is already in the cart
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {'name': str(product.name), 'price': str(product.price), 'quantity': quantity}

        # Mark the session as modified to ensure changes are saved
        self.session.modified = True

    def remove(self, product_id):
        # Remove a product from the cart
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True


    def get_items(self):
        return self.cart.items()

    def get_cart_subtotal(self):
        subtotal = sum(
            item.get('quantity', 0) * Product.objects.get(id=product_id).price
            for product_id, item in self.cart.items())
        return round(subtotal, 2)

    def get_cart_total(self):
        # Add shipping cost logic or any other additional costs
        return self.get_cart_subtotal()

    def __len__(self):
        # Return the number of items in the cart
        return len(self.cart)
