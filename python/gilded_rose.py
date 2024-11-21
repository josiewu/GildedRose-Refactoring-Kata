# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            item.upgrade()


class Item(metaclass=ABCMeta):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    @abstractmethod
    def __repr__(self):
        pass

    def decrease_quality(self):
        if self.quality > 0:
            self.quality = self.quality - 1

    def increase_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1


class AgedBrieItem(Item):
    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def upgrade(self):
        self.sell_in = self.sell_in - 1
        self.increase_quality()
        if self.sell_in < 0:
            self.increase_quality()

class BackstageItem(Item):
    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def upgrade(self):
        self.sell_in = self.sell_in - 1
        self.increase_quality()
        if self.sell_in < 10:
            self.increase_quality()
        if self.sell_in < 5:
            self.increase_quality()
        if self.sell_in < 0:
            self.quality = self.quality - self.quality

class NormalItem(Item):
    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def upgrade(self):
        self.sell_in = self.sell_in - 1
        self.decrease_quality()
        if self.sell_in < 0:
            self.decrease_quality()
