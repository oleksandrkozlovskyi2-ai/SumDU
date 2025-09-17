def even_product(n):
    dob = 1
    for i in range(2, 2*n + 1, 2):
        dob *= i
    return dob
