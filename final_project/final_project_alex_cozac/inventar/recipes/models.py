from django.db import models
from items.models import Item



class Recipe(models.Model):
    name = models.CharField(max_length=200)
    items = models.ManyToManyField(Item,)
    # item_1 = models.ForeignKey(Item, on_delete = models.DO_NOTHING, related_name='item1')
    # item_2 = models.ForeignKey(Item, on_delete = models.DO_NOTHING, related_name='item2')
    # item_3 = models.ForeignKey(Item, on_delete = models.DO_NOTHING, blank=True, related_name='item3', null=True)
    # item_4 = models.ForeignKey(Item, on_delete = models.DO_NOTHING, blank=True, related_name='item4', null=True)
    # item_5 = models.ForeignKey(Item, on_delete = models.DO_NOTHING, blank=True, related_name='item5', null=True)
    # item_6 = models.ForeignKey(Item, on_delete = models.DO_NOTHING, blank=True, related_name='item6', null=True)
    # item_7 = models.ForeignKey(Item, on_delete = models.DO_NOTHING, blank=True, related_name='item7', null=True)
    # item_8 = models.ForeignKey(Item, on_delete = models.DO_NOTHING, blank=True, related_name='item8', null=True)
    image = models.ImageField(upload_to='recipes/')

    def __str__(self):
        return self.name

