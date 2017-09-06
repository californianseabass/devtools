
# turns any single argument function into a generator
def generate(f):
    ''' example: 
        gen_sqrt = generate(math.sqrt)
            for x in gen_sqrt(xrange(100)):
                print x
    '''
    def gen_func(s):
        for item in s:
            print('item: ', item)
            yield f(item)
    return gen_func


def trace(source):
    ''' debugging utility
    '''
    for item in source:
        print item
        yield item

class storelast(object):
    ''' stores the last generated object from a generator

    '''
    def __init__(self,source):
        self.source = source
    def next(self):
        item = self.source.next()
        self.last = item
        return item
    def __iter__(self):
        return self

def follow(thefile, shutdown=None):
    ''' You can't shutdown a generator from another thread/process, must use a flag as below
        example:
            import threading,signal
            shutdown = threading.Event()
            def sigusr1(signo,frame):
                print "Closing it down"
            shutdown.set()
            signal.signal(signal.SIGUSR1,sigusr1)
            lines = follow(open("access-log"),
            shutdown
            )
            for line in lines:
                print line,
    '''
    thefile.seek(0,2)
    while True:
        if shutdown and shutdown.isSet(): break
                line = thefile.readline()
                if not line:
                   time.sleep(0.1)
                   continue
                yield line