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


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self._update_item(item)

    def _is_aged_brie(self, item):
        return item.name == AGED_BRIE

    def _is_backstage(self, item):
        return item.name == BACKSTAGE

    def _is_sulfuras(self, item):
        return item.name == SULFURAS

    def _increase_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1

    def _decrease_quality(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1

    def _set_quality_to_zero(self, item):
        item.quality = 0

    def _decrease_sell_in_if_needed(self, item):
        if not self._is_sulfuras(item):
            item.sell_in = item.sell_in - 1

    # --- Type-specific updates (pure refactor: same behavior, clearer structure) ---

    def _update_normal_item_before_sell_date(self, item):
        if item.quality > 0:
            if not self._is_sulfuras(item):
                self._decrease_quality(item)

    def _update_aged_brie_or_backstage_before_sell_date(self, item):
        if item.quality < 50:
            self._increase_quality(item)
            if self._is_backstage(item):
                if item.sell_in < 11:
                    if item.quality < 50:
                        self._increase_quality(item)
                if item.sell_in < 6:
                    if item.quality < 50:
                        self._increase_quality(item)

    def _update_after_sell_date(self, item):
        if not self._is_aged_brie(item):
            if not self._is_backstage(item):
                if item.quality > 0:
                    if not self._is_sulfuras(item):
                        self._decrease_quality(item)
            else:
                self._set_quality_to_zero(item)
        else:
            if item.quality < 50:
                self._increase_quality(item)

    def _update_item(self, item):
        # before sell date behavior
        if (not self._is_aged_brie(item)) and (not self._is_backstage(item)):
            self._update_normal_item_before_sell_date(item)
        else:
            self._update_aged_brie_or_backstage_before_sell_date(item)

        # decrement sell_in (except sulfuras)
        self._decrease_sell_in_if_needed(item)

        # after sell date behavior
        if item.sell_in < 0:
            self._update_after_sell_date(item)