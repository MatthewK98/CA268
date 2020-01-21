from Queue import Queue

def split(q):
    #split queue in half
    queuelen, queuelen2, queuelen3 = len(q), len(q), len(q)
    q1, q2 = Queue(), Queue()
    while queuelen > queuelen2 // 2:
        q1.enqueue(q.dequeue())
        queuelen -= 1
    while queuelen3 > queuelen2 // 2:
        q2.enqueue(q.dequeue())
        queuelen3 -= 1
    return q1, q2