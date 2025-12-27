import math
lr=0.0001
guess_m1=1
guess_m2=1
guess_m3=1
guess_m4=1
guess_c=1
data = [
    [22, 180, 3, 85, 1],
    [45, 95, 2, 55, 0],
    [36, 160, 4, 90, 1],
    [29, 110, 3, 65, 0],
    [50, 75, 2, 45, 0],
    [33, 140, 3, 80, 1],
    [41, 100, 3, 60, 0],
    [27, 130, 3, 70, 1],
    [38, 155, 4, 95, 1],
    [31, 120, 3, 75, 1],
    [46, 85, 2, 50, 0],
    [24, 175, 3, 88, 1],
    [39, 105, 3, 68, 0],
    [30, 145, 4, 82, 1],
    [42, 90, 2, 55, 0]
    
]

def func(x,y,z,a):
    return guess_m1 * x + guess_m2 * y + guess_m3 * z + guess_m4 * a + guess_c
def predict(x,y,z,a):
    return sigmoid(func(x/50,y/200,z/5,a/120))
def sigmoid(x):
    x = max(min(x, 50), -50) 
    return 1 / (1 + math.exp(-x))

def error(guess_m1,guess_m2,guess_m3,guess_m4,guess_c):
    theoretical_data = []
    errors=[]
    dm1_contributions = []
    dm2_contributions = []
    dm3_contributions = []
    dm4_contributions = []
    dc_contributions = []

    for list in data:
        a,b,c,d,e = list  
        a /= 50
        b /= 200
        c /= 5
        d /= 120
        error = sigmoid(guess_m1 * a + guess_m2 * b + guess_m3 * c + guess_m4 * d + guess_c) - e
        errors.append(error**2)
        dm1_contributions.append(error * a)
        dm2_contributions.append(error * b)
        dm3_contributions.append(error * c)
        dm4_contributions.append(error * d)
        dc_contributions.append(error)
        
    
    return [sum(errors)/len(errors), sum(dm1_contributions)/len(dm1_contributions), sum(dm2_contributions)/len(dm2_contributions), sum(dm3_contributions)/len(dm3_contributions), sum(dm4_contributions)/len(dm4_contributions), sum(dc_contributions)/len(dc_contributions)]

 
for i in range(10000000):
    current_error, dm1, dm2, dm3, dm4, dc = error(guess_m1,guess_m2,guess_m3,guess_m4, guess_c)
    guess_m1-= lr * dm1
    guess_m2-= lr * dm2
    guess_m3-= lr * dm3
    guess_m4-= lr * dm4
    guess_c-= lr * dc
    if i % 20000 == 0:
        print(f"Current guesses: predicted value = {predict(33,140,3,80)} m1 = {round(guess_m1,2)}, m2 = {round(guess_m2,2)}, m3 = {round(guess_m3,2)}, m4 = {round(guess_m4,2)} c = {round(guess_c,2)}, error = {round(current_error,4)}, i = {i}")
    if error(guess_m1,guess_m2,guess_m3,guess_m4, guess_c)[0]<0.01:
        break
print(f"Found values: m1 = {round(guess_m1,2)}, m2 = {round(guess_m2,2)}, m3 = {round(guess_m3,2)}, m4 = {round(guess_m4,2)} c = {round(guess_c,2)}")
print(predict(34,150,3,85))        
                