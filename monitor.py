import time


class Monitor:
    """Monitor a Signal at a regular Cadence by 
    establishing a heartbeat and passing result
    on to handlers."""
    def __init__(self, signal, cadence, handlers=[], go=False):
        self.signal = signal
        self.cadence = cadence
        self.handlers = handlers

        if go:
            self.go()

    def go(self):
        """go spawns/forks a new process for each
        handler to listen to the signal. This 
        operation is safe on the database because 
        it is a read-only process. The target handlers 
        need to be write-safe.
        """
        for handler in self.handlers:
            # TODO: Spawn new processes for each handler.    
            continue

        while True:
            result = self.signal.get()
            processes.map(record, result)
            seconds = yield from cadence.when()
            time.sleep(seconds)


            