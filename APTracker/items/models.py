from django.db import models
from .utils import get_data

class Item(models.Model):
    name = models.CharField(max_length=220, blank=True)
    url = models.URLField()
    current_price = models.FloatField(blank=True)
    old_price = models.FloatField(default=0)
    price_difference = models.FloatField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('price_difference', '-created')

    def save(self, *args, **kwargs):
        name, price = get_data(self.url)
        if self.current_price:
            if price != self.current_price:
                diff = price - self.current_price
                self.price_difference = round(diff, 2)
                self.old_price = self.current_price
        else:
            self.price_difference = 0

        self.current_price = price
        self.name = name

        super().save(*args, **kwargs)