class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, product):
        if str(product.id) not in self.cart.keys():
            self.cart[product.id] = {
                "product_id": product.id,
                "name": product.nombre,
                "price": "{0:,.0f}".format(product.precio),
                "quantity": 1,
            }
        else:
            for key, value in self.cart.items():
                if key == str(product.id):
                    value["quantity"] = value["quantity"] + 1
                    break
            self.save()

    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def decrement(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):
                value["quantity"] = value["quantity"] - 1
                if value["quantity"] < 1:
                    self.remove(product)
                else:
                    self.save()
                break
            else:
                print("El producto no existe en el carrito")
                self.save()

    def increment(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):
                value["quantity"] = value["quantity"] + 1
                self.save()
                break
            else:
                print("El producto no existe en el carrito")
                self.save()

    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True

    def get_subtotal_price(self):
        total_price = sum(
            int(item["price"].replace(",", "").replace(".", "")) * item["quantity"] for item in self.cart.values())
        return 'CLP$ '+"{0:,.0f}".format(total_price)

    def get_iva(self):
        total_price = sum(
            int(item["price"].replace(",", "").replace(".", "")) * item["quantity"] for item in self.cart.values())
        return 'CLP$ '+"{0:,.0f}".format(total_price*0.19)

    def get_total_price(self):
        total_price = sum(
            int(item["price"].replace(",", "").replace(".", "")) * item["quantity"] for item in self.cart.values())
        return 'CLP$ '+"{0:,.0f}".format(total_price*1.19)


    def get_total_quantity(self):
        return sum(item["quantity"] for item in self.cart.values())

    def get_products(self):
        return self.cart.values()

    def count(self):
        return len(self.cart.values())
