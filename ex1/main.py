# Lukas Sailer, Janik Steegmüller

def faktorial(n):
    fak = 1
    for i in range(1,n+1):
        fak = fak * i
    return fak

def binomial(n: int, k:int):
    return int(faktorial(n)/(faktorial(k)*faktorial(n-k)))



class PascalsTriangle:
    def __init__(self, num_rows=2):
        self.data = []
        self.gen = PascalsTriangle.binomial_generator()

    def update(self, num_rows):
        if num_rows < len(self.data):
            return
        for i in range(num_rows):
            self.data.append(next(self.gen))

    @staticmethod
    def binomial_generator():
        tree = [[1]]
        n = 1
        k = 1
        while True:
            tree.append([])
            for ik in range(k+1):
                x1 = 0 if ik-1 < 0 else tree[n-1][ik-1]
                x2 = 0 if ik >=k else tree[n-1][ik]
                tree[n].append(x1 + x2)
            k = k + 1
            n = n + 1
            yield tree[n-2]

    def __str__(self):
        pretty_print = ""
        for row in self.data:
            for i in range(len(self.data) - len(row)):
               pretty_print = f'{pretty_print} '
            for number in row:
                pretty_print = f'{pretty_print}  {number}'
            pretty_print = f'{pretty_print}\n'
        return pretty_print


if __name__ == '__main__':
    print(binomial(5, 0) == 1)
    print(binomial(2, 1) == 2)
    print(binomial(4, 2) == 6)
    print(binomial(0, 0) == 1)
    print(binomial(0, 0).__class__)

    pt = PascalsTriangle()
    pt.update(6)
    print(pt.data == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]])
    print(pt)
