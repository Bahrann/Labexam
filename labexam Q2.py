def compute_cross_product(array1, array2):
    if len(array1) != 3 or len(array2) != 3:
        raise ValueError("Both arrays must be 3-dimensional (length 3).")
    

    cross_product = [
        array1[1] * array2[2] - array1[2] * array2[1],  
        array1[2] * array2[0] - array1[0] * array2[2],  
        array1[0] * array2[1] - array1[1] * array2[0]   
    ]
    return cross_product

array1 = [1, 2, 3]
array2 = [4, 5, 6]
result = compute_cross_product(array1, array2)
print("Cross Product:", result)  