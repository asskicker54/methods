import numpy as np

def make_identity(matrix: np.ndarray) -> np.ndarray:
    for nrow in range(len(matrix)-1, 0, -1):
        row = matrix[nrow]
        for upper_row in matrix[:nrow]:
            factor = upper_row[nrow]
            upper_row -= factor * row
    
    return matrix

def gauss(matrix: np.ndarray) -> np.ndarray:
    for nrow in range(len(matrix)):
        pivot = nrow + np.argmax(abs(matrix[nrow:, nrow]))
        if pivot != nrow:
            matrix[[nrow, pivot]] = matrix[[pivot, nrow]]
        row = matrix[nrow]
        divider = row[nrow]
            
        if abs(divider) < 1e-10:
            return
        row /= divider
        for lower_row in matrix[nrow + 1:]:
            factor = lower_row[nrow]
            lower_row -= factor * row
                
    make_identity(matrix)
    return matrix

matrix = np.array([
	[3, 2, -5, -1],
    [2, -1, 3, 13],
    [1, 2, -1, 9]
], dtype=np.float32)

print("\nОтвет:")
for i,x in enumerate(gauss(matrix)):
    print(f"x{i+1} = {round(x[-1], 3)}")

        