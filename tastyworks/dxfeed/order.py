from tastyworks.dxfeed.mapped_item import MappedItem


class Order(MappedItem):
    DXFEED_TEXT = 'Order'

    def __init__(self, data=None):
        super().__init__(data=data)
