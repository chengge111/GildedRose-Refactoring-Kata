# -*- coding: utf-8 -*-

AGED_BRIE = "Aged Brie"
BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemUpdater:
    def update(self, item):
        raise NotImplementedError


class NormalUpdater(ItemUpdater):
    def update(self, item):
        if item.quality > 0:
            item.quality -= 1

        item.sell_in -= 1

        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1


class AgedBrieUpdater(ItemUpdater):
    def update(self, item):
        if item.quality < 50:
            item.quality += 1

        item.sell_in -= 1

        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1


class BackstageUpdater(ItemUpdater):
    def update(self, item):
        if item.quality < 50:
            item.quality += 1

            if item.sell_in <= 10 and item.quality < 50:
                item.quality += 1

            if item.sell_in <= 5 and item.quality < 50:
                item.quality += 1

        item.sell_in -= 1

        if item.sell_in < 0:
            item.quality = 0


class SulfurasUpdater(ItemUpdater):
    def update(self, item):
        pass


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def get_updater(self, item):
        if item.name == AGED_BRIE:
            return AgedBrieUpdater()
        elif item.name == BACKSTAGE:
            return BackstageUpdater()
        elif item.name == SULFURAS:
            return SulfurasUpdater()
        else:
            return NormalUpdater()

    def update_quality(self):
        for item in self.items:
            updater = self.get_updater(item)
            updater.update(item)