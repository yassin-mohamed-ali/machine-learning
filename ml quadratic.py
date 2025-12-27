
guess_m1=-50
guess_m2=-50
guess_c=50
data = [
    (-5, 16),
    (-4, 9),
    (-3, 4),
    (-2, 1),
    (-1, 0),
    (0, 1),
    (1, 4),
    (2, 9),
    (3, 16),
    (4, 25),
    (5, 36)
]

def func(x):
    return guess_m1 * (x**2) + guess_m2 * x + guess_c
def error(guess_m1,guess_m2,guess_c):
    theoretical_data = []
    errors=[]
    for list in data:
        x, y = list  
        theoretical_data.append((x, guess_m1 * (x**2) + guess_m2 * x + guess_c))
    for theoretical_point in theoretical_data:
        tx, ty = theoretical_point
        for point in data:
            x, y = point
            if x == tx:
                errors.append(abs(ty - y)**2)
    return sum(errors)/len(errors)
for i in range(10000):
    current_error = error(guess_m1,guess_m2, guess_c)
    new_error_m1_plus = error(guess_m1 + 0.1, guess_m2, guess_c)
    new_error_m1_minus = error(guess_m1 - 0.1, guess_m2, guess_c)
    if new_error_m1_plus < current_error:
        guess_m1 += 0.1
    elif new_error_m1_minus < current_error:
        guess_m1 -= 0.1

    new_error_m2_plus = error(guess_m1, guess_m2 + 0.1, guess_c)
    new_error_m2_minus = error(guess_m1, guess_m2 - 0.1, guess_c)
    if new_error_m2_plus < current_error:
        guess_m2 += 0.1
    elif new_error_m2_minus < current_error:
        guess_m2 -= 0.1
    
    new_error_c_plus = error(guess_m1,guess_m2, guess_c + 0.1)
    new_error_c_minus = error(guess_m1,guess_m2, guess_c - 0.1)
    if new_error_c_plus < current_error:
        guess_c += 0.1
    elif new_error_c_minus < current_error:
        guess_c -= 0.1
    else:
        pass
    print(f"Current guesses: m1 = {guess_m1}, m2 = {guess_m2},  c = {guess_c}, error = {current_error}, i = {i}")
m1 = round(guess_m1,2)
m2 = round(guess_m2,2)
c = round(guess_c,2)
print(f"Found values: m1 = {m1}, m2 = {m2}, c = {c}")
print(f"y={m1}x^2 + {m2}x + {c}")
      
                