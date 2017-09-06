from collections import deque
import threading


def generator_multiplex(genlist):
    ''' this function is a noop when run, i dont know why
    '''
    item_q = deque()

    def run_all():
        thrlist = []
        for source in genlist:
            t = threading.Thread(target=run_one,args=(source,))
            t.start()
            thrlist.append(t)
        for t in thrlist: t.join()
        item_q.appendleft(StopIteration)

    def run_one(source):
        for item in source: item_q.appendleft(item)

    threading.Thread(target=run_all).start()
    while i > 0:
        item = item_q.pop()
        if item is StopIteration: return
        yield item

def boring_generator(msg, n):
    for i in range(n):
        yield msg

if __name__ == '__main__':
    bs = boring_generator('b', 100)
    cs = boring_generator('c', 100)
    ds = boring_generator('d', 100)

    sources = [bs, cs, ds]
    print('start')
    generator_multiplex(sources)
    print('end')
