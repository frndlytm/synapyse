import numpy as np


class Cadence:
    """Cadence updates itself to a sleep time 
    by randomly normally distributing it around the
    queue length times the average wait time.
    
    The choice of distribution can be configured by
    the user and optimized by a model on their signal.
    """
    def __init__(self, bpm=20, distr=np.normal):
        self.bpm = bpm
        self.distr = distr

    def when(self):
        yield self.bpm

        self.bpm = self.distr.sample()
        self.distr = self.distr.update()

