import time
import os

def euclidean_distance(list1, list2):
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

            distance = euclidean_distance(point1, point2)

            if distance < best_distance:
                best_distance = distance
                best_label = data[j][0]

        if best_label == data[i][0]:
            correct += 1

    return correct / len(data)

def forward_selection(data, total_features):
    selected_features = []
    best_accuracy = 0
    
    while True:
        best_round_accuracy = 0
        
        for f in range(1, total_features + 1): 
            if f not in selected_features:
                candidate = selected_features + [f]
                accuracy = loo_cv_accuracy(data, candidate)
                print(f"Using feature(s): {candidate} accuracy is {accuracy:.4f}")

                if accuracy > best_round_accuracy:
                    best_round_accuracy = accuracy
                    best_feature = f
        
        if best_round_accuracy > best_accuracy :  
            best_accuracy = best_round_accuracy                
            selected_features.append(best_feature)
            print(f"Feature set {best_feature} was best, accuracy is {best_round_accuracy:.4f}")
        else:
            break
    print(f"Finished search!! The best feature subset is", selected_features, "with an accuracy of", best_accuracy)
    return selected_features, best_accuracy      

def backward_elimination(data, total_features):
    selected_features = list(range(1, total_features + 1))
    best_accuracy = 0
    
    while True:
        best_round_accuracy = 0
        
        for f in range(1, total_features + 1): 
            if f  in selected_features:
                candidate = [x for x in selected_features if x != f]
                accuracy = loo_cv_accuracy(data, candidate)
                print(f"Using feature(s): {candidate} accuracy is {accuracy:.4f}")

                if accuracy > best_round_accuracy:
                    best_round_accuracy = accuracy
                    best_feature = f

        
        if best_round_accuracy > best_accuracy :  
            best_accuracy = best_round_accuracy                
            selected_features.remove(best_feature)
            print(f"Feature set {best_feature} was best, accuracy is {best_round_accuracy:.4f}")

        else:
            break
    
    print(f"Finished search!! The best feature subset is", selected_features, "with an accuracy of", best_accuracy)
    return selected_features, best_accuracy


def load_data(filepath):
    data = []
    with open(filepath, "r") as f:
        for line in f:
            if line.strip():  # skip empty lines
                row = [float(x) for x in line.split()]
                data.append(row)
    return data

def load_directory(directory):
    all_data = []
    for filename in os.listdir(directory):
        all_data += load_data(os.path.join(directory, filename))
    return all_data

def main():
    type = int(input("Welcome to Muhammad Sabeel's Nearest Neighbor Feature Selection Algorithm:\n Are you loading a (1) single file or (2) directory? "))
    file = (input("\nEnter file/directory name: "))

    if type == 1:
        data = load_data(file)
    if type == 2:
        data = load_directory(file)

    total_features = len(data[0]) - 1
    alg = int(input("What algorithm?\n (1) Forward Selection\n (2) Backward Elimination: "))
    print(f"Data loaded successfully. Number of features:", (total_features), "Number of instances (not including label):", len(data))

    start = time.time()  # ← start here

    if alg == 1:
        selected_features, accuracy = forward_selection(data, total_features)
    if alg == 2:
        selected_features, accuracy = backward_elimination(data, total_features)

    end = time.time()    # ← end here
    print(f"Time taken to run on this dataset: {end - start:.2f} seconds")

    print("Best features found:", selected_features)
    print("Accuracy:", accuracy)

if __name__ == "__main__":
    main()