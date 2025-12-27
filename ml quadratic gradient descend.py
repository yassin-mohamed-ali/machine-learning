lr = 0.01
guess_m1=1000
guess_m2=-500
guess_c=9999
data = [
    (0, 1), 
    (1, 6),    
    (2, 17),  
    (3, 34),  
    (4, 57)    
]


def func(x):
    return guess_m1 * (x**2) + guess_m2 * x + guess_c
def error(guess_m1,guess_m2,guess_c):
    theoretical_data = []
    dm1_contributions = []
    dm2_contributions = []
    dc_contributions = []
    errors=[]
    for tuple in data:
        x, y = tuple  
        theoretical_data.append((x, guess_m1 * (x**2) + guess_m2 * x + guess_c))
    for theoretical_point in theoretical_data:
        tx, ty = theoretical_point
        for point in data:
            x, y = point
            if x == tx:
                error = ty - y
                errors.append(error**2)
                dm1_contributions.append(error * (x**2))
                dm2_contributions.append(error * x) 
                dc_contributions.append(error)

    return [sum(errors)/len(errors), sum(dm1_contributions)/len(dm1_contributions), sum(dm2_contributions)/len(dm2_contributions), sum(dc_contributions)/len(dc_contributions)]
for i in range(9000):
    diff, dm1 , dm2, dc = error(guess_m1,guess_m2,guess_c)
    guess_m1 -= lr * dm1
    guess_m2 -= lr * dm2
    guess_c -= lr * dc
    print(f"Iteration {i}: m1 = {guess_m1}, m2 = {guess_m2}, c = {guess_c}, error = {diff}")

m1 = round(guess_m1,0)
m2 = round(guess_m2,0)
c = round(guess_c,0)
print(f"Found values: m1 = {m1}, m2 = {m2}, c = {c}")
print(f"y={m1}x^2 + {m2}x + {c}")
      
                