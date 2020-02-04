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

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def decrease_quality(self):
        if self.quality > 0:
            self.quality = self.quality - 1

    def increase_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1

    def update(self):
        if self.name == "Sulfuras, Hand of Ragnaros":
            return

        elif self.name == "Aged Brie":
            self.increase_quality()
            self.sell_in = self.sell_in - 1

            if self.sell_in < 0:
                self.increase_quality()

        elif self.name == "Backstage passes to a TAFKAL80ETC concert":
            self.increase_quality()

            if self.sell_in < 11:
                self.increase_quality()
            if self.sell_in < 6:
                self.increase_quality()
            self.sell_in = self.sell_in - 1

            if self.sell_in < 0:
                self.quality = 0

        else:
            self.decrease_quality()
            self.sell_in = self.sell_in - 1

            if self.sell_in < 0:
                self.decrease_quality()
