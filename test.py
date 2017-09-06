from collections import deque
import threading

def consume_queue(dq):
    while True:
        # print('dq: {}'.format(dq))
        if len(dq) > 0:
            item = dq.pop()
            if item is StopIteration: break
            yield item

def consumer(q):
    for item in consume_queue(q):
        print("Consumed", item)
    print("Done")
 
in_q = deque()
con_thr = threading.Thread(target=consumer,args=(in_q,))
con_thr.start()
for i in range(100):
    in_q.appendleft(i)
in_q.appendleft(StopIteration)
con_thr.join()
