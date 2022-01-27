class FlatIterator:
    def __init__(self,nested_list):
        self.cursor = -1
        self.target_list = nested_list
        self.list_len = len(self.target_list)

    def __iter__(self):
        self.cursor += 1
        self.nested_cursor = 0
        return self

    def __next__(self):
        if self.nested_cursor == len(self.target_list[self.cursor]):
            iter(self)
        if self.cursor == self.list_len:
            raise StopIteration
        self.nested_cursor += 1
        return self.target_list[self.cursor][self.nested_cursor - 1]

if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    nested_list_elements = [item for item in FlatIterator(nested_list)]
    print(nested_list_elements)
