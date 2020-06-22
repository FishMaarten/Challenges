class Matrix:
    def __init__(self, matrix:str):
        self.rows = [[int(c) for c in r.split(" ")] for r in matrix.split("\n")]
        self.columns = [[r[idx] for r in self.rows] for idx in range(len(self.rows[0]))]
