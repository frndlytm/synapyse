class Connection:
    """Connection keeps open a transport to share
    Objects over. A scalar-valued query is the
    first feature implemented; however whole
    other types of data can be observed in the
    future."""
    def __init__(self, name, engine, out="Primitive"):
        self.name = name
        self.engine = engine.build(name)
        self.out = out

    def _scalar(self, query):
        return self.engine.execute_scalar(query)

    def _vector(self, query):
        return self.engine.execute_vector(query)

    def execute(self, query):
        if out == "Primitive":
            return self._scalar(query)
        elif out == "Chunkable":
            return self.engine._vector(query)