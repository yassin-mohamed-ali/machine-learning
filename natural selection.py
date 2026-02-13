import random
import numpy as np
class Cat:
    def __init__(self, num_food,m_num_food,base,position):
        self.num_food = num_food
        self.m_num_food = m_num_food
        self.base = base
        self.position = position
    def decisition(self):
        if self.num_food < self.m_num_food:
            movement=["left","right","up","down"]
            movement = random.choice(movement)
            if movement == "left":
                self.position[0]-=1
            elif movement == "right":
                self.position[0]+=1
            elif movement == "up":
                self.position[1]-=1
            elif movement == "down":
                self.position[1]+=1
            self.position[0] = max(0, min(99, self.position[0]))
            self.position[1] = max(0, min(99, self.position[1]))
        else:
            self.position = self.base.copy()
    def x(self):
        return self.position[0]
    def y(self):
        return self.position[1]
    
    def eat(self):
        self.num_food += 1
    def returned(self):
        if self.position == self.base:
            return True
        return False
    def reset(self):
        self.num_food = 0
class fish:
    def __init__(self, position):
        self.position = position
    def x(self):
        return self.position[0]
    def y(self):
        return self.position[1]
def update():
    world = np.zeros((100, 100))
    cats_returned = 0
    cats_returned = 0
    global fishes
    for cat in cats[:]:
        world[cat.y(),cat.x()] = 1
        for fish in fishes[:]:
            world[fish.y(),fish.x()] = 2
            if cat.position == fish.position:
                cat.eat()
                fishes.remove(fish)
        cat.decisition()
        if cat.returned():
            cats_returned+=1
    if cats_returned > len(cats) * 0.75:
        for cat in cats[:]:
            if not cat.returned():
                cats.remove(cat)
            else:
                for i in range(cat.num_food):
                    cats.append(Cat(0,cat.m_num_food,[random.randint(0,99),random.randint(0,99)],[random.randint(0,99),random.randint(0,99)]))
                cat.reset()
        fishes = [fish([random.randint(0,99),random.randint(0,99)]) for _ in range(1,50)]
def evaluate():
    m1,m2,m3,m4,m5,m6,m7,m8,m9,m10 = [0,]*10
    for cat in cats:
        x = cat.m_num_food
        if x == 1:
            m1+=1
        elif x == 2:
            m2+=1
        elif x == 3:
            m3+=1
        elif x == 4:
            m4+=1
        elif x == 5:
            m5+=1
        elif x == 6:
            m6+=1
        elif x == 7:
            m7+=1
        elif x == 8:
            m8+=1
        elif x == 9:
            m9+=1
        elif x == 10:
            m10+=1
    print(m1,m2,m3,m4,m5,m6,m7,m8,m9,m10)


cats = [Cat(0,random.randint(1,5),[random.randint(0,99),random.randint(0,99)],[random.randint(0,99),random.randint(0,99)]) for _ in range(1,50)]
fishes = [fish([random.randint(0,99),random.randint(0,99)]) for _ in range(1,50)]
world = np.zeros((100, 100))

for i in range(1,1000):
    update()
evaluate()