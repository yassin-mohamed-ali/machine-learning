
guess_m1=1
guess_m2=1
guess_m3=1
guess_c=1
data = [
    [2, 50, 2, 120],
    [5, 70, 3, 150],
    [1, 60, 2, 130],
    [10, 80, 4, 180],
    [3, 90, 3, 170],
    [7, 100, 4, 200],
    [12, 110, 5, 220],
    [4, 95, 3, 180],
    [6, 85, 4, 190],
    [8, 120, 5, 240]
]
def func(x,y,z):
    return guess_m1 * x + guess_m2 * y + guess_m3 * z + guess_c
def error(guess_m1,guess_m2,guess_m3,guess_c):
    theoretical_data = []
    errors=[]
    for list in data:
        a,b,c,d = list  
        theoretical_data.append((a,b,c, guess_m1 * a + guess_m2 * b + guess_m3 * c + guess_c))
    for theoretical_point in theoretical_data:
        ta,tb,tc, ty = theoretical_point
        for point in data:
            a,b,c,d = point
            if a == ta and b == tb and c == tc:
                errors.append(abs(ty - d))
    return sum(errors)/len(errors)
for i in range(10000):
    current_error = error(guess_m1,guess_m2,guess_m3, guess_c)
    new_error_m1_plus = error(guess_m1 + 0.1, guess_m2, guess_m3, guess_c)
    new_error_m1_minus = error(guess_m1 - 0.1, guess_m2, guess_m3, guess_c)
    if new_error_m1_plus < current_error:
        guess_m1 += 0.1
    elif new_error_m1_minus < current_error:
        guess_m1 -= 0.1

    new_error_m2_plus = error(guess_m1, guess_m2 + 0.75, guess_m3, guess_c)
    new_error_m2_minus = error(guess_m1, guess_m2 - 0.75, guess_m3, guess_c)
    if new_error_m2_plus < current_error:
        guess_m2 += 0.75
    elif new_error_m2_minus < current_error:
        guess_m2 -= 0.75
    
    new_error_m3_plus = error(guess_m1, guess_m2, guess_m3 + 0.075, guess_c)
    new_error_m3_minus = error(guess_m1, guess_m2, guess_m3 - 0.075, guess_c)
    if new_error_m3_plus < current_error:
        guess_m3 += 0.075
    elif new_error_m3_minus < current_error:
        guess_m3 -= 0.075
    

    new_error_c_plus = error(guess_m1,guess_m2,guess_m3, guess_c + 1)
    new_error_c_minus = error(guess_m1,guess_m2,guess_m3, guess_c - 1)
    if new_error_c_plus < current_error:
        guess_c += 1
    elif new_error_c_minus < current_error:
        guess_c -= 1
    else:
        pass
    print(f"Current guesses: m1 = {guess_m1}, m2 = {guess_m2}, m3 = {guess_m3}, c = {guess_c}, error = {current_error}, i = {i}")
print(f"Found values: m1 = {round(guess_m1,2)}, m2 = {round(guess_m2,2)}, m3 = {round(guess_m3,2)} c = {round(guess_c,2)}")
print(func(6, 80, 3))        
                