# -*- coding: utf-8 -*-
"""Module for handling inventory update logic in the Gilded Rose system."""

from item_wrappers import item_factory

# pylint: disable=too-few-public-methods
class GildedRose:
    """Main class that processes a list of items and updates their quality and sell-in values."""

    def __init__(self, items):
        """Initialize GildedRose with a list of items."""
        self.items = items

    def update_quality(self):
        """Update quality and sell-in of each item using its respective wrapper."""
        for item in self.items:
            wrapper = item_factory(item)
            wrapper.update()
