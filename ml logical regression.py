import math
guess_m1, guess_m2, guess_m3, guess_m4, guess_c=1 # Initial assumptions
data = [
    [25, 120, 2, 50, 1],
    [40, 80, 3, 70, 0],
    [30, 150, 4, 90, 1],
    [50, 60, 2, 40, 0],
    [35, 200, 5, 120, 1],
    [28, 90, 3, 65, 0]
]

def func(x,y,z,a): # The function formula
    return guess_m1 * x + guess_m2 * y + guess_m3 * z + guess_m4 * a + guess_c
def error(guess_m1,guess_m2,guess_m3,guess_m4,guess_c): # Function to detect errors
    theoretical_data = [] # Data under assumptions 
    errors=[] # Errors under assumptions
    for list in data:
        a,b,c,d,e = list  # Actual values of data
        theoretical_data.append((a,b,c,d, guess_m1 * a + guess_m2 * b + guess_m3 * c + guess_m4 * d + guess_c))
    for theoretical_point in theoretical_data:
        ta,tb,tc, td, ty = theoretical_point # Assumed values of data 
        for point in data:
            a,b,c,d,e = point
            if a == ta and b == tb and c == tc and d == td:
                errors.append(abs(ty - (1/(1+math.exp(-e))))) # Error as difference between read value and sigmoid of Assumed value
    return sum(errors)/len(errors) # Returns average of errors
for i in range(10000): # 10,000 iterations of attempting
    current_error = error(guess_m1,guess_m2,guess_m3,guess_m4, guess_c) # Current error
    new_error_m1_plus = error(guess_m1 + 0.01, guess_m2, guess_m3,guess_m4, guess_c) # Error per increase of m1
    new_error_m1_minus = error(guess_m1 - 0.01, guess_m2, guess_m3, guess_m4, guess_c) # Error per decrease of m1
    # Error direction for m1
    if new_error_m1_plus < current_error:
        guess_m1 += 0.1 
    elif new_error_m1_minus < current_error:
        guess_m1 -= 0.1

    new_error_m2_plus = error(guess_m1, guess_m2 + 0.75, guess_m3, guess_m4, guess_c) # Error per increase of m2
    new_error_m2_minus = error(guess_m1, guess_m2 - 0.75, guess_m3, guess_m4, guess_c) # Error per decrease of m2
    # Error direction of m2
    if new_error_m2_plus < current_error:
        guess_m2 += 0.75
    elif new_error_m2_minus < current_error:
        guess_m2 -= 0.75
    
    new_error_m3_plus = error(guess_m1, guess_m2, guess_m3 + 0.075, guess_m4, guess_c) # Error per increase of m3
    new_error_m3_minus = error(guess_m1, guess_m2, guess_m3 - 0.075, guess_m4, guess_c) # Error per decrease of m3
    # Error direction of m3
    if new_error_m3_plus < current_error:
        guess_m3 += 0.075
    elif new_error_m3_minus < current_error:
        guess_m3 -= 0.075

    new_error_m4_plus = error(guess_m1, guess_m2, guess_m3, guess_m4 + 0.075, guess_c) # Error per increase of m4
    new_error_m4_minus = error(guess_m1, guess_m2, guess_m3, guess_m4 - 0.075, guess_c) # Error per decrease of m4
    # Error direction of m4
    if new_error_m4_plus < current_error:
        guess_m4 += 0.075
    elif new_error_m4_minus < current_error:
        guess_m4 -= 0.075
    

    new_error_c_plus = error(guess_m1,guess_m2,guess_m3,guess_m4, guess_c + 1) # Error per increase of c
    new_error_c_minus = error(guess_m1,guess_m2,guess_m3,guess_m4, guess_c - 1) # Error per decrease of c
    # Error direction of c
    if new_error_c_plus < current_error:
        guess_c += 1
    elif new_error_c_minus < current_error:
        guess_c -= 1
    else:
        pass
    # Current progress
    print(f"Current guesses: m1 = {guess_m1}, m2 = {guess_m2}, m3 = {guess_m3}, m4 = {guess_m4} c = {guess_c}, error = {current_error}, i = {i}")
# Final result of slopes and c
print(f"Found values: m1 = {round(guess_m1,2)}, m2 = {round(guess_m2,2)}, m3 = {round(guess_m3,2)}, m4 = {round(guess_m4,2)} c = {round(guess_c,2)}")
# Final result
print(1 / (1 + math.exp(-func(33, 140, 3, 80))))        
                