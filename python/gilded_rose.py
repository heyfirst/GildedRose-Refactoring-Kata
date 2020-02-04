# -*- coding: utf-8 -*-


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for i, item in enumerate(self.items):
            item = ItemFactory.create_item(item)
            item.update()
            self.items[i] = item


class ItemFactory:
    @staticmethod
    def create_item(item):
        if item.name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(name=item.name, sell_in=item.sell_in, quality=item.quality)

        if item.name == "Aged Brie":
            return AgedBrie(name=item.name, sell_in=item.sell_in, quality=item.quality)

        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePass(
                name=item.name, sell_in=item.sell_in, quality=item.quality
            )

        return Item(name=item.name, sell_in=item.sell_in, quality=item.quality)


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
        self.decrease_quality()

        self.sell_in = self.sell_in - 1

        if self.sell_in < 0:
            self.decrease_quality()


class Sulfuras(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        pass


class AgedBrie(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        self.increase_quality()

        self.sell_in = self.sell_in - 1
        
        if self.sell_in < 0:
            self.increase_quality()


class BackstagePass(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        self.increase_quality()

        if self.sell_in < 11:
            self.increase_quality()
        if self.sell_in < 6:
            self.increase_quality()

        self.sell_in = self.sell_in - 1

        if self.sell_in < 0:
            self.quality = 0
