class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


def part1():
    part = 2
    dkey = 1 if part == 1 else 811589153

    with open('../../inputs/2022/day20.txt') as f:
        s = f.read().strip()

    r = []
    for l in s.split("\n"):
        n = dkey * int(l)
        r.append(Node(n))

    for a, b in zip(r,r[1:]):
        a.next = b
        b.prev = a

    r[-1].next = r[0]
    r[0].prev = r[-1]

    head = r[0]

    def show():
        print(head.val, head.next.val, head.next.next.val, head.next.next.next.val,
              head.next.next.next.next.val, head.next.next.next.next.next.val, head.next.next.next.next.next.next.val)

    for itr in range(1 if part == 1 else 10):
        for x in r:
            # Delete x
            show()
            x.prev.next = x.next
            x.next.prev = x.prev

            # Get x's prev and next
            a, b = x.prev, x.next
            move = x.val % (len(r) - 1)
            for _ in range(move):
                a = a.next
                b = b.next

            # Insert x
            a.next = x
            x.prev = a
            b.prev = x
            x.next = b

    for x in r:
        if x.val == 0:
            r = 0
            y = x
            for _ in range(3):
                for _ in range(1000):
                    y = y.next
                r += y.val
            print(r)


if __name__ == '__main__':
    part1()
