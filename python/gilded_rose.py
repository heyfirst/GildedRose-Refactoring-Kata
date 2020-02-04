# -*- coding: utf-8 -*-


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            elif item.name == "Aged Brie":
                item.increase_quality()
                item.sell_in = item.sell_in - 1

                if item.sell_in < 0:
                    item.increase_quality()

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.increase_quality()

                if item.sell_in < 11:
                    item.increase_quality()
                if item.sell_in < 6:
                    item.increase_quality()
                item.sell_in = item.sell_in - 1

                if item.sell_in < 0:
                    item.quality = 0

            else:
                item.decrease_quality()
                item.sell_in = item.sell_in - 1

                if item.sell_in < 0:
                    item.decrease_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def decrease_quality(self):
        if self.quality > 0:
            self.quality = self.quality - 1

    def increase_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1
