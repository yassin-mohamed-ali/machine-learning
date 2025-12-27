guess_m=1
guess_c=1
data=[(1,88),(2,151),(5,340),(10,655)]
def error(guess_m,guess_c):
    theoretical_data = []
    errors=[]
    for point in data:
        x,y = point  
        theoretical_data.append((x, guess_m * x + guess_c))
    for theoretical_point in theoretical_data:
        tx, ty = theoretical_point
        for point in data:
            x, y = point
            if x == tx:
                errors.append(abs(ty - y))
    return sum(errors)/len(errors)
for i in range(10000):
    current_error = error(guess_m, guess_c)
    new_error_m_plus = error(guess_m + 0.01, guess_c)
    new_error_m_minus = error(guess_m - 0.01, guess_c)
    if new_error_m_plus < current_error:
        guess_m += 0.01
    elif new_error_m_minus < current_error:
        guess_m -= 0.01
    else:
        pass
    new_error_c_plus = error(guess_m, guess_c + 0.01)
    new_error_c_minus = error(guess_m, guess_c - 0.01)
    if new_error_c_plus < current_error:
        guess_c += 0.01
    elif new_error_c_minus < current_error:
        guess_c -= 0.01
    else:
        pass
    print(f"Current guesses: m = {guess_m}, c = {guess_c}, error = {current_error}")
print(f"Found values: m = {round(guess_m,0)}, c = {round(guess_c,0)}")
        
                