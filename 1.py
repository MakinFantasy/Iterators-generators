class FlatIterator:

    def __init__(self, target_list):

        self.target_list = target_list

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        for i in range(len(self.target_list)):
            if self.cursor == len(self.target_list) - 1:
                raise StopIteration
            self.cursor += 1
            for j in range(len(self.target_list[i])):
                print(self.target_list[i][j])
        return ''


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
    out_list = []
    for item in FlatIterator(nested_list):
        print(item)