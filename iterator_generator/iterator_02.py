class MyIterator:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration()
        prev_current = self.current
        self.current += self.step
        return prev_current

instance = MyIterator(0, 10, 2)
print(next(instance))
print(next(instance))
print(next(instance))
for item in instance:
    print(item)
