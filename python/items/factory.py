from items.model import Sulfuras, AgedBrie, BackstagePass, Item


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
