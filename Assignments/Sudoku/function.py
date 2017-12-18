def cross(a, b):
    return [s+t for s in a for t in b]

rows = 'ABCDEFGHI'
columns = '123456789'

boxes = cross(rows, columns)

row_units = [cross(r, columns) for r in rows]

column_units = [cross(rows, c) for c in columns]

square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123','456','789')]
