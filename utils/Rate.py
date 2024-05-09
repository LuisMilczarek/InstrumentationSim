from time import perf_counter, sleep

class Rate(object):
    def __init__(self,freq: float = 60) -> None:
        self._period = 1 / freq
        self._lastRead = 0

    
    def sleep(self):
        delta = perf_counter() - self._lastRead
        toSleep = self._period - delta
        if toSleep > 0:
            sleep(toSleep)
        self._lastRead = perf_counter()
