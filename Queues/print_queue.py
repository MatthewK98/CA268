import sys

def print_queue(queue, front, back):
    while front != back:
        item = queue[front]
        front = (front + 1) % len(queue)
        print(item)
