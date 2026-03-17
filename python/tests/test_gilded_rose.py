import unittest
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_aged_brie_increases_quality(self):
        items = [Item("Aged Brie", 5, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(11, items[0].quality)

    def test_aged_brie_increases_twice_after_expiry(self):
        items = [Item("Aged Brie", 0, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(12, items[0].quality)

    def test_backstage_pass_increase_by_two(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(12, items[0].quality)

    def test_backstage_pass_quality_drops_to_zero(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
