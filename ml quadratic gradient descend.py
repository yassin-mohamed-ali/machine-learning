lr = 0.01 # Learning rate
# Initial assumptions
guess_m1=1000
guess_m2=-500
guess_c=9999
data = [ # Data provided
    (0, 1), 
    (1, 6),    
    (2, 17),  
    (3, 34),  
    (4, 57)    
]


def func(x): # Assumed function
    return guess_m1 * (x**2) + guess_m2 * x + guess_c
def error(guess_m1,guess_m2,guess_c): # Function to detect error 
    theoretical_data = [] # List of data under assumptions
    # List of errors
    dm1_contributions = [] 
    dm2_contributions = []
    dc_contributions = []
    errors=[]
    for tuple in data:
        x, y = tuple # For value in point in data  
        theoretical_data.append((x, guess_m1 * (x**2) + guess_m2 * x + guess_c)) # Create assumed value
    for theoretical_point in theoretical_data:
        tx, ty = theoretical_point
        for point in data:
            x, y = point
            if x == tx:
                error = ty - y # Error as difference of point assumed and actual point
                errors.append(error**2) # Squared errors
                # Errors per contribution
                dm1_contributions.append(error * (x**2))
                dm2_contributions.append(error * x) 
                dc_contributions.append(error)

    # Returns list of mean of errors and contributions
    return [sum(errors)/len(errors), sum(dm1_contributions)/len(dm1_contributions), sum(dm2_contributions)/len(dm2_contributions), sum(dc_contributions)/len(dc_contributions)]
for i in range(9000): # 9,000 iterations of attempting
    # Mean of current errors
    diff, dm1 , dm2, dc = error(guess_m1,guess_m2,guess_c)
    # Gradient descent logic
    guess_m1 -= lr * dm1
    guess_m2 -= lr * dm2
    guess_c -= lr * dc
    print(f"Iteration {i}: m1 = {guess_m1}, m2 = {guess_m2}, c = {guess_c}, error = {diff}")

# Round values to integers
m1 = round(guess_m1,0)
m2 = round(guess_m2,0)
c = round(guess_c,0)
# Final result of slopes and c
print(f"Found values: m1 = {m1}, m2 = {m2}, c = {c}")
# Final result of eqation
print(f"y={m1}x^2 + {m2}x + {c}")
      
                