import math
guess_m1=1
guess_m2=1
guess_m3=1
guess_m4=1
guess_c=1
data = [
    # Age, Budget(1000s), Bedrooms, Size(m²), Bought(0/1)
    [25, 120, 2, 50, 1],
    [40, 80, 3, 70, 0],
    [30, 150, 4, 90, 1],
    [50, 60, 2, 40, 0],
    [35, 200, 5, 120, 1],
    [28, 90, 3, 65, 0]
]

def func(x,y,z,a):
    return guess_m1 * x + guess_m2 * y + guess_m3 * z + guess_m4 * a + guess_c
def error(guess_m1,guess_m2,guess_m3,guess_m4,guess_c):
    theoretical_data = []
    errors=[]
    for list in data:
        a,b,c,d,e = list  
        theoretical_data.append((a,b,c,d, guess_m1 * a + guess_m2 * b + guess_m3 * c + guess_m4 * d + guess_c))
    for theoretical_point in theoretical_data:
        ta,tb,tc, td, ty = theoretical_point
        for point in data:
            a,b,c,d,e = point
            if a == ta and b == tb and c == tc and d == td:
                errors.append(abs(ty - (1/(1+math.exp(-e)))))
    return sum(errors)/len(errors)
for i in range(10000):
    current_error = error(guess_m1,guess_m2,guess_m3,guess_m4, guess_c)
    new_error_m1_plus = error(guess_m1 + 0.01, guess_m2, guess_m3,guess_m4, guess_c)
    new_error_m1_minus = error(guess_m1 - 0.01, guess_m2, guess_m3, guess_m4, guess_c)
    if new_error_m1_plus < current_error:
        guess_m1 += 0.1
    elif new_error_m1_minus < current_error:
        guess_m1 -= 0.1

    new_error_m2_plus = error(guess_m1, guess_m2 + 1, guess_m3, guess_m4, guess_c)
    new_error_m2_minus = error(guess_m1, guess_m2 - 1, guess_m3, guess_m4, guess_c)
    if new_error_m2_plus < current_error:
        guess_m2 += 0.75
    elif new_error_m2_minus < current_error:
        guess_m2 -= 0.75
    
    new_error_m3_plus = error(guess_m1, guess_m2, guess_m3 + 0.5, guess_m4, guess_c)
    new_error_m3_minus = error(guess_m1, guess_m2, guess_m3 - 0.5, guess_m4, guess_c)
    if new_error_m3_plus < current_error:
        guess_m3 += 0.075
    elif new_error_m3_minus < current_error:
        guess_m3 -= 0.075

    new_error_m4_plus = error(guess_m1, guess_m2, guess_m3, guess_m4 + 0.25, guess_c)
    new_error_m4_minus = error(guess_m1, guess_m2, guess_m3, guess_m4 - 0.25, guess_c)
    if new_error_m4_plus < current_error:
        guess_m4 += 0.075
    elif new_error_m4_minus < current_error:
        guess_m4 -= 0.075
    

    new_error_c_plus = error(guess_m1,guess_m2,guess_m3,guess_m4, guess_c + 1)
    new_error_c_minus = error(guess_m1,guess_m2,guess_m3,guess_m4, guess_c - 1)
    if new_error_c_plus < current_error:
        guess_c += 1
    elif new_error_c_minus < current_error:
        guess_c -= 1
    else:
        pass
    print(f"Current guesses: m1 = {guess_m1}, m2 = {guess_m2}, m3 = {guess_m3}, m4 = {guess_m4} c = {guess_c}, error = {current_error}, i = {i}")
print(f"Found values: m1 = {round(guess_m1,2)}, m2 = {round(guess_m2,2)}, m3 = {round(guess_m3,2)}, m4 = {round(guess_m4,2)} c = {round(guess_c,2)}")
print(1 / (1 + math.exp(-func(33, 140, 3, 80))))        
                