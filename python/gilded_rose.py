# -*- coding: utf-8 -*-
from items.factory import ItemFactory


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for i, item in enumerate(self.items):
            item = ItemFactory.create_item(item)
            item.update()
            self.items[i] = item
