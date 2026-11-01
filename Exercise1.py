# 1. First, make sure your data dictionary is at the top
data = {
    "Nutritional values per 100 g": ["Protein (g)", "Fat (g)", "Carbohydrates (g)"],
    "Butter": [0.2, 82.5, 0.0],
    "Apple": [0.3, 0.2, 12.1],
    "Oats": [14.0, 6.9, 57.0],
    "Rye bread": [6.4, 4.7, 32.0]
}
def get_determinant(matrix):
    return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
            matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
            matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))


base_matrix = [
    [0.2, 0.3, 14.0],
    [82.5, 0.2, 6.9],
    [0.0, 12.1, 57.0]
]


targets = [50, 70, 260]

matrix_butter = [
     [50, 0.3, 14.0],
     [70, 0.2, 6.9],
     [260, 12.1, 57.0]
] 
matrix_apple = [
    [0.2, 50, 14.0],
    [82.9, 70, 6.9],
    [0.0, 260, 57.0]
]

matrix_oats = [
     [0.2, 0.3, 50],
     [82.5, 0.2, 70],
     [0.0, 12.1, 260]
]




d_main = get_determinant(base_matrix)
d_butter = get_determinant(matrix_butter)
d_apple = get_determinant(matrix_apple)
d_oats = get_determinant(matrix_oats)


matrix_butter = (d_butter / d_main * 100)
matrix_apple = (d_apple / d_main * 100)
matrix_oats = (d_oats / d_main * 100)

print(f"{matrix_butter:.1f} g butter")
print(f"{matrix_apple:.1f} g apple")
print(f"{matrix_oats:.1f} g oats")


#Week 2

base_matrix_w2 = [
     [0.2, 6.4, 14.0],
     [82.0, 4.7, 6.9],
     [0.0, 32.0, 57.0]
]
matrix_butter_w2 = [
     [50, 0.3, 14.0],
     [70, 0.2, 6.9],
     [260, 12.1, 57.0]
] 
matrix_ryebread_w2 = [
    [0.2, 14.0, 50],
    [82.5, 6,9, 70],
    [0.0, 57.0, 260]
]

matrix_oat_w2 = [
     [0.2, 0.3, 50],
     [82.5, 0.2, 70],
     [0.0, 12.1, 260]
]

d_main_w2 = get_determinant(base_matrix_w2)
d_butter_w2 = get_determinant(matrix_butter_w2)
d_rye_w2 = get_determinant(matrix_rye_w2)
d_oats_w2 = get_determinant(matrix_oats_w2)

butter_grams_w2 = (d_butter_w2 / d_main_w2 * 100)
rye_grams_w2 = (d_rye_w2 / d_main_w2 * 100)
oats_grams_w2 = (d_oats_w2 / d_main_w2 * 100)

print("--- Week 2 Diet Plan ---")
print(f"{butter_grams_w2:.1f} g butter")
print(f"{rye_grams_w2:.1f} g rye bread")
print(f"{oats_grams_w2:.1f} g oats")

if butter_grams_w2 < 0 or rye_grams_w2 < 0 or oats_grams_w2 < 0:
    print("Is this plan possible? No (Requires negative grams!)")
else:
    print("Is this plan possible? Yes")
