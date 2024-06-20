from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    date_register = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_product = models.PositiveIntegerField()
    date_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product, through='OrderProduct')
    total_sum = models.DecimalField(max_digits=10, decimal_places=2)
    date_order = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} by {self.client.name}'


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.product.name} in order {self.order.id}'


