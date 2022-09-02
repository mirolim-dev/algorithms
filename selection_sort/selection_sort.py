class SelectionSort:
    def __init__(self, data_list):
        self.data_list = data_list
        self.sorted_list = []
    
    def sort_by_decriese(self):
        if self.data_list == []:
            return self.sorted_list
        max_data = self.data_list[0]
        for i in self.data_list:
            if i > max_data:
                max_data = i
        self.sorted_list.append(max_data)
        self.data_list.remove(max_data)
        return self.sort_by_decriese()

    def sort_by_incriese(self):
        if self.data_list == []:
            return self.sorted_list
        min_data = self.data_list[0]
        for i in self.data_list:
            if i < min_data:
                min_data = i
        self.sorted_list.append(min_data)
        self.data_list.remove(min_data)
        return self.sort_by_incriese()