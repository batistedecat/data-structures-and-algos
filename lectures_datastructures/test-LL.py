import time
from LinkedList import LinkedList, Node


def title(text):
    print()
    print(text)
    print("-" * len(text))


def draw(ll):
    parts = []
    curr = ll.head
    while curr is not None:
        parts.append(f"[{curr.data}]")
        curr = curr.next
    chain = " -> ".join(["head"] + parts + ["None"])
    head = ll.head.data if ll.head else None
    tail = ll.tail.data if ll.tail else None
    print(f"   {chain}")
    print(f"   size={ll.size}   head={head}   tail={tail}")


title("1. A single node")
n = Node("A")
print(f"   n.data = {n.data}")
print(f"   n.next = {n.next}   <- a new node does not point anywhere yet")


title("2. An empty list")
ll = LinkedList()
draw(ll)


title("3. add_first: every new node goes in front")
for x in [3, 2, 1]:
    ll.add_first(x)
    print(f"add_first({x})")
    draw(ll)
    if ll.size == 1:
        print(f"   head is tail? {ll.head is ll.tail}   <- with one node, they are the same object")


title("4. add_last_with_tail: the new node goes at the back")
ll.add_last_with_tail(4)
print("add_last_with_tail(4)")
draw(ll)


title("5. Following the arrows by hand")
print(f"   ll.head.data                = {ll.head.data}")
print(f"   ll.head.next.data           = {ll.head.next.data}")
print(f"   ll.head.next.next.data      = {ll.head.next.next.data}")
print(f"   ll.head.next.next.next.data = {ll.head.next.next.next.data}")
print(f"   ll.tail.next                = {ll.tail.next}   <- the last node points to None")


title("6. Two ways to add at the back, same result")
a = LinkedList()
b = LinkedList()
for x in ["x", "y", "z"]:
    a.add_last_no_tail(x)
    b.add_last_with_tail(x)
print("add_last_no_tail:")
draw(a)
print("add_last_with_tail:")
draw(b)


title("7. Why the tail pointer matters")
n_items = 5000

start = time.perf_counter()
slow = LinkedList()
for i in range(n_items):
    slow.add_last_no_tail(i)
t_slow = time.perf_counter() - start

start = time.perf_counter()
fast = LinkedList()
for i in range(n_items):
    fast.add_last_with_tail(i)
t_fast = time.perf_counter() - start

print(f"   {n_items} x add_last_no_tail:   {t_slow:.4f} s   <- walks the whole chain every time: O(n)")
print(f"   {n_items} x add_last_with_tail: {t_fast:.4f} s   <- jumps straight to the tail: O(1)")
print(f"   with tail is about {t_slow / t_fast:.0f}x faster")


title("8. print_walk")
print("   list:")
draw(ll)
print("   print_walk() output:")
ll.print_walk()