from synapyse.connection import Connection

class Signal:
    """Signal warps a scalar valued query with a
    connection, and exposes access to that scalar
    on demand."""
    def __init__(self, query, connection=Connection()):
        self.query = query
        self.connection = connection.establish()

    def get(self):
        return self.connection.scalar(self.query)
        
    