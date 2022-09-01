class BinarySearch():
    def __init__(self, list):
        self.up_border = len(list)
        self.down_border = 0
        self.list = list
        self.steps = 0


    def search(self, item):
        if item == self.list[0]:
            return item
        middle_of_the_list = (self.up_border + self.down_border) // 2
        value = self.list[middle_of_the_list]
        if item in self.list and self.up_border > self.down_border:
            self.steps += 1
            # print('up_border', self.up_border, 'down_border: ', self.down_border,  'middle_of_the_list: ', middle_of_the_list)
            if value == item:
                context = {
                    'item': item,
                    'steps': self.steps,
                }
                return context
            elif value > item:
                self.up_border = middle_of_the_list
                return self.search(item)
            elif value < item:
                self.down_border = middle_of_the_list
                return self.search(item)
            
        else:
            return "item is not inside of the list"