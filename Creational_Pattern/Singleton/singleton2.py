class SingletonDecorator:
    def __init__(self, klass):
        self.klass = klass
        self._instance = None
    
    def __call__(self, *args, **kwargs):
        if self._instance == None:
            self._instance = self.klass(*args, **kwargs)
        return self._instance

@SingletonDecorator
class Logger:
    def __init__(self):
        self.start = None

    def write(self, msg):
        if self.start:
            print(self.start, msg)
        else:
            print(msg)

log1 = Logger()
log2 = Logger()

log1.start = "log1 # >:"
log1.write("Log1 is writing")

log2.start = "log2 # >:"
log2.write("Log2 is writing")