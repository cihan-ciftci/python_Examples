import math

breaks = [(2, 3), (4, 5), (7, 8), (5, 9)]

def euclidean_distance(breaks1, breaks2):
    a1, b1 = breaks1
    a2, b2 = breaks2
    return math.sqrt((a2 - a1)**2 + (b2 - b1)**2)

breaksDistances = []
for i in range(len(breaks)):
    for j in range(i + 1, len(breaks)):
        dist = euclidean_distance(breaks[i], breaks[j])
        breaksDistances.append(dist)

min_distance = min(breaksDistances)

print("Breaks :", breaks)
print("breaksDistances :", breaksDistances)
print("Minimum Distances :", min_distance)