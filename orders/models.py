from django.db import models


# Create your models here.


class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    )
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    cart = models.ForeignKey('cart.Cart', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Order {self.id}"