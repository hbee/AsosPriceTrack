from django.db import models
from django.contrib.auth.models import User
from .utils import get_data

class Item(models.Model):
    name = models.CharField(max_length=220, blank=True)
    url = models.URLField()
    current_price = models.FloatField(blank=True)
    old_price = models.FloatField(default=0)
    price_difference = models.FloatField(default=0)
    sale = models.FloatField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='items')


    def __str__(self):
        return self.name

    class Meta:
        ordering = ('price_difference', '-created')

    def save(self, *args, **kwargs):
        name, price = get_data(self.url)
        if self.current_price:
            if price != self.old_price:
                diff = price - self.current_price
                self.price_difference = round(diff, 2)
                if self.old_price != 0:
                    self.sale = round((1 - (self.current_price / self.old_price)) * 100, 2)
        else:
            self.old_price = price
            self.price_difference = 0
            self.sale = 0

        self.current_price = price
        self.name = name

        super().save(*args, **kwargs)