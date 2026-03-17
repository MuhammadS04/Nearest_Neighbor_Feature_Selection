
def euclidan_distance(list1, list2):
    distance = 0
    for i in range(len(list1)):
        distance += (list1[i] - list2[i]) ** 2
    return distance ** 0.5

def loo_cv_accuracy(data, features):
    correct = 0

    for i in range(len(data)):
        best_distance = float('inf')
        best_label = None

        for j in range(len(data)):

            if i == j:
                continue

            point1 = [data[i][f] for f in features]
            point2 = [data[j][f] for f in features]

            distance = euclidan_distance(point1, point2)

            if distance < best_distance:
                best_distance = distance
                best_label = data[j][0]

        if best_label == data[i][0]:
            correct += 1

    return correct / len(data)

