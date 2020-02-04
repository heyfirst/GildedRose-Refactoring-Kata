# -*- coding: utf-8 -*-


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

        if self.name == "Sulfuras, Hand of Ragnaros":
            self.__update_func = update_sulfuras
        elif self.name == "Aged Brie":
            self.__update_func = update_aged_brie
        elif self.name == "Backstage passes to a TAFKAL80ETC concert":
            self.__update_func = update_backstage
        else:
            self.__update_func = update_item

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def decrease_quality(self):
        if self.quality > 0:
            self.quality = self.quality - 1

    def increase_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1

    def update(self):
        self.__update_func(self)


def update_sulfuras(item):
    return item


def update_aged_brie(item):
    item.increase_quality()
    item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        item.increase_quality()

    return item


def update_backstage(item):
    item.increase_quality()

    if item.sell_in < 11:
        item.increase_quality()
    if item.sell_in < 6:
        item.increase_quality()

    item.sell_in = item.sell_in - 1

    if item.sell_in < 0:
        item.quality = 0

    return item


def update_item(item):
    item.decrease_quality()
    item.sell_in = item.sell_in - 1

    if item.sell_in < 0:
        item.decrease_quality()

    return item
