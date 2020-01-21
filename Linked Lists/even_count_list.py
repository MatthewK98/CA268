def even_count(self):
    count = 0
    pointer = self.head
    while pointer != None:
        if pointer.item % 2 == 0:
            count += 1
        pointer = pointer.next
    return count
    
import sys
from LinkedList import LinkedList
from even_count_list import even_count

def main():
    # Read each set
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]
    
    ll = LinkedList()
    
    for num in nums:
        ll.add(num)
    
    print(even_count(ll))

if __name__ == "__main__":
    main()