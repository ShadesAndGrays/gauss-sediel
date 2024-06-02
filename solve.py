from fractions import Fraction
matA = []
x = []
b = []

iterations = 1

def print_mat():
    for i in range(4):
        print("|",end ="")
        for j in range(4):
            print(matA[i][j],end= " ")
        print("|")

def print_x():
    for i in range(4):
        print("[" + str(x[i]) + "]")


for i in range(4):
    temp = []
    for j in range(4):
        temp.append(Fraction(input("A"+str(i+1)+str(j+1)+": ")))
    matA.append(temp)

for i in range(4):
        b.append(Fraction(input("B"+str(i+1)+": ")))

for i in range(4):
        x.append(Fraction(input("X"+str(i+1)+": ")))


print_mat()
print_x()


iterations = int(input("Input number of iterations: "))

p1 = 0
p2 = 1
p3 = 2
p4 = 3

for i in range(iterations):
    x[p1] = - (1/matA[p1][p1]) * (matA[p1][p2] * x[p2] + matA[p1][p3] * x[p3] + matA[p1][p4] * x[p4] - b[p1])
    x[p2] = - (1/matA[p2][p2]) * (matA[p2][p1] * x[p1] + matA[p2][p3] * x[p3] + matA[p2][p4] * x[p4] - b[p2])
    x[p3] = - (1/matA[p3][p3]) * (matA[p3][p1] * x[p1] + matA[p3][p2] * x[p2] + matA[p3][p4] * x[p4] - b[p3])
    x[p4] = - (1/matA[p4][p4]) * (matA[p4][p1] * x[p1] + matA[p4][p2] * x[p2] + matA[p4][p3] * x[p3] - b[p4])
    print("Iteration ", i)
    print_x()
    pass

