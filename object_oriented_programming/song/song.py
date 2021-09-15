from object_oriented_programming import Text


class Song(Text):
    def number_of_lines(self):
        return len(self.text.split('\n'))
