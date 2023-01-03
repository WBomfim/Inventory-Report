from collections.abc import Iterator


class InventoryIterator(Iterator):
    """Iterator for InventoryRefactor class"""

    def __init__(self, products):
        self._products = products
        self._index = 0

    def __next__(self):
        try:
            product = self._products[self._index]
        except IndexError:
            raise StopIteration()
        else:
            self._index += 1
            return product
