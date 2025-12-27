guess_m=1
guess_c=1
data = [
    (0, 12),
    (2, 15),
    (4, 25),
    (5, 24),
    (7, 32),
    (9, 36),
    (10, 41),
    (12, 45),
    (13, 49),
    (15, 55),
    (16, 52),   # slightly low
    (18, 65),
    (20, 68),
    (21, 74),
    (23, 78),
    (25, 90),   # outlier (high)
    (27, 92),
    (28, 94),
    (30, 101),
    (32, 105),
    (35, 113),
    (37, 120),
    (38, 121),
    (40, 130),  # outlier (high)
    (42, 132),
    (45, 146),
    (47, 148),
    (50, 160)
]
hypothesis_data = data
theoretical_data_error_margins = []
def error(guess_m,guess_c):
    theoretical_data = []
    errors=[]
    for point in hypothesis_data:
        x,y = point  
        theoretical_data.append((x, guess_m * x + guess_c))
    for theoretical_point in theoretical_data:
        tx, ty = theoretical_point
        for point in data:
            x, y = point
            if x == tx:
                errors.append(abs(ty - y))
    return sum(errors)/len(errors)

for j in data:
    hypothesis_data.remove(j)
    for i in range(1000):
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
        print(f"Current guesses: m = {guess_m}, c = {guess_c}, error = {current_error}, i = {i}")
    theoretical_data_error_margins.append(error(guess_m, guess_c))
for i in range(len(hypothesis_data)):
    if abs(max(theoretical_data_error_margins)-((sum(theoretical_data_error_margins))/len(theoretical_data_error_margins)))>0.1:
        theoretical_data_error_margins.remove(max(theoretical_data_error_margins))
for i in range(len(hypothesis_data)):
    if abs(min(theoretical_data_error_margins)-((sum(theoretical_data_error_margins))/len(theoretical_data_error_margins)))>0.1:
        theoretical_data_error_margins.remove(min(theoretical_data_error_margins))
for i in range(1000):
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
        print(f"Current guesses: m = {guess_m}, c = {guess_c}, error = {current_error}, i = {i}")        
print(f"Found values: m = {round(guess_m,0)}, c = {round(guess_c,0)}")
            
                    