class LinearSearch():
    def __init__(self, list):
        self.list = list
        self.steps = 0
    
    def search(self, item):
        if item in self.list:
            _item = self.list[self.steps]
            self.steps += 1
            if _item == item:
                context = {
                    'item': item,
                    'steps': self.steps,
                }
                return context
            else:
                return self.search(item=item)
        else:
            return "item is not in list"