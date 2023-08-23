from enum import EnumMeta

class MatrixEnum(EnumMeta):
    def __new__(cls, name, values, *args, **kwargs):
        if values:
            for value in values:
                if not isinstance(value, list):
                    raise TypeError("values must be a list of lists")
        return super().__new__(cls, name, *args, **kwargs)
        
    def __getitem__(self, item):
        if isinstance(item, int):
            return super().__getitem__(item)

        if isinstance(item, tuple):
            return self(item)

        raise TypeError("item must be an int or a tuple")

class TypePiece(MatrixEnum):
    LPIECE = [[1, 0, 0],[1, 1, 1]]
    LMPIECE = [[1, 1, 1],[1, 0, 0]]
    IPIECE = [[1, 1, 1, 1]]
    TPIECE = [[1, 1, 1],[0, 1, 0]]
    SQUAREPIECE = [[1,1],[1,1]]
    NPIECE = [[1 ,1, 0],[0, 1, 1]]
    ZPIECE = [[0, 1, 1],[1, 1, 0]]

    def value(self):
        return self._cell_values
