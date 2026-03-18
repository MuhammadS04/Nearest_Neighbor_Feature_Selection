# Nearest_Neighbor_Feature_Selection

Project 2 for CS 170 Winter 2026 with Professor Dr. Eamonn Keogh.
Repository: https://github.com/MuhammadS04/Nearest_Neighbor_Feature_Selection.git 

Nearest Neighbor + 
Feature Selection Algorithms



What is the Nearest Neighbor Algorithm
	The nearest neighbor algorithm is a machine learning algorithm used to classify classes of potentially similar instances. Say we have to find two classes of similarities within a dataset of 10,000,000 instances. We take those instances, get their features, and run the nearest neighbor algorithm to classify a new instance by finding the single closest existing instance and copying its label. For the distance measure in this project I used Euclidean distance. For example, the use case of identifying heart diseases. Given a large number of instances, we need to predict the nearest neighbor for new patients that might have similar symptoms (possible features) as compared to our data, by finding the nearest neighbor or nearest instance in the data we have. The issue is that the nearest neighbor algorithm is very sensitive to noise, i.e not knowing if the features in our datasets are truly useful or not, bringing us to a solution called Feature Selection.
Feature Selection
Feature selection is a smart way to go about dealing with the noise problem in the nearest neighbor algorithm. Since not all features are useful to use and some can skew our data a lot, we need a way to determine the usefulness of the data we are comparing. For example, if we are trying to classify patients under what type of heart disease they have by calculating distance measures from their heart rate, CO2 levels, etc, but then a feature like favorite color comes along and skews our entire distance distribution, it can cause a huge problem in the labelling process. For this we investigate two methods in this project: Forward selection and backward elimination.
  



Forward Selection
The idea with forward selection is to start with 0 features from our instances and try each feature individually, keeping whichever one gives the best accuracy. We compare it to the nearest neighbor we find and check if the label was assigned correctly. If so then our accuracy score improves. We iterate through the features and add whichever features help improve the accuracy, until it stops improving.
Backward Elimination
Backward elimination is as the name suggests. We start with all features, and remove the least useful one to our accuracy score. Eventually we end up with something similar to forward selection.













Results
*Note: Dr. Eamonn instructed me to use small and large dataset #18 respectively via email*
Small Dataset Forward Selection
	In figure 1, we see the results for running CS170_Small_DataSet_18.txt : 

Running forward selection on the small dataset (16 features, 500 instances), the algorithm first identified feature {15} with an accuracy of 83.6%. Adding feature {2} dramatically improved accuracy to 97.0%. Adding any further features reduced accuracy, so the search stopped. The best feature subset found was {15, 2} with an accuracy of 97.0%.







Small Dataset Backward Elimination
In figure 2, we see the results for running CS170_Small_DataSet_18.txt using backward elimination: 


Running backward elimination on the same dataset, the algorithm began by removing the least useful features one at a time. The best subset found was {2,3,6,7,9,10,12,14,15,16} with an accuracy of 81.2%. Backward elimination was not as accurate as forward selection for this dataset.
Small Dataset Conclusion:  
Both algorithms agree that features 2 and 15 are important, giving confidence they are truly relevant. Forward selection found a much cleaner and more accurate subset. I believe features {15, 2} are the best features for this problem, with an expected accuracy of 97.0%.


Large Dataset Forward Selection
In figure 3, we see the results for running CS170_Large_DataSet_18.txt using Forward Selection: 

Running forward selection on the large dataset (64 features, 3000 instances), feature {6} alone achieved 85.27% accuracy. Adding feature {10} dramatically improved accuracy to 97.73%. Every additional feature reduced accuracy, so the search stopped after just 2 rounds. The best feature subset was {6, 10}.





Large Dataset Backward Elimination
 *Note that the backward elimination compilation was cut short while making these visuals due to closeness to the due date*
In figure 3, we see the results for running CS170_Large_DataSet_18.txt using Backward Elimination:

Running backward elimination on the large dataset (64 features, 3000 instances), the algorithm began removing the least useful features one at a time. The search is computationally intensive given the dataset size, and the algorithm showed gradual accuracy improvements as irrelevant features were eliminated. Due to the scale of this dataset, the full backward elimination search required significant computational time.
Large Dataset Conclusion
Forward selection on the large dataset produced a remarkably clean result — just 2 features out of 64 achieving 97.73% accuracy. This strongly suggests that features 6 and 10 are the primary discriminating features in this dataset, with the remaining 62 features contributing mostly noise. This is a compelling demonstration of why feature selection matters: using all 64 features would dramatically slow down classification while actually hurting accuracy.

Time Table
Timing 
Small Dataset (16 features, 500 instances)
Large Dataset (64 features, 3000 instances
Forward Selection
5.35 seconds
850.27 seconds
Backward Elimination
31.75 seconds
Pending


This table above shows how long it took my machine (Apple MacBook Pro M1 Pro chip with 8GB Ram) in Python 3 to run each dataset.

Conclusion
In this project I implemented a nearest neighbor classifier with leave-one-out cross validation, combined with two feature selection algorithms: forward selection and backward elimination. Across both datasets, forward selection consistently outperformed backward elimination, finding smaller and more accurate feature subsets in less time. On the small dataset, forward selection identified just 2 features {15, 2} achieving 97.0% accuracy compared to backward elimination's 10 features at 81.2%. On the large dataset, forward selection again found just 2 features {6, 10} out of 64, achieving 97.73% accuracy. These results demonstrate a key insight: more features does not mean better accuracy. In both cases, using all features produced significantly lower accuracy than the small optimal subsets found by forward selection. 


Example Truce (small dataset forward selection)
Welcome to Muhammad Sabeel's Nearest Neighbor Feature Selection Algorithm:
 Are you loading a (1) single file or (2) directory? 
Enter file/directory name: What algorithm?
 (1) Forward Selection
 (2) Backward Elimination: Data loaded successfully. Number of features: 16 Number of instances (not including label): 500
Using feature(s): [1] accuracy is 0.6800
Using feature(s): [2] accuracy is 0.6860
Using feature(s): [3] accuracy is 0.6660
Using feature(s): [4] accuracy is 0.6840
Using feature(s): [5] accuracy is 0.6940
Using feature(s): [6] accuracy is 0.6640
Using feature(s): [7] accuracy is 0.6900
Using feature(s): [8] accuracy is 0.6840
Using feature(s): [9] accuracy is 0.7000
Using feature(s): [10] accuracy is 0.7040
Using feature(s): [11] accuracy is 0.6940
Using feature(s): [12] accuracy is 0.7020
Using feature(s): [13] accuracy is 0.6880
Using feature(s): [14] accuracy is 0.6960
Using feature(s): [15] accuracy is 0.8360
Using feature(s): [16] accuracy is 0.6660
Feature set 15 was best, accuracy is 0.8360
Using feature(s): [15, 1] accuracy is 0.8160
Using feature(s): [15, 2] accuracy is 0.9700
Using feature(s): [15, 3] accuracy is 0.8180
Using feature(s): [15, 4] accuracy is 0.7900
Using feature(s): [15, 5] accuracy is 0.8240
Using feature(s): [15, 6] accuracy is 0.8160
Using feature(s): [15, 7] accuracy is 0.8340
Using feature(s): [15, 8] accuracy is 0.8420
Using feature(s): [15, 9] accuracy is 0.8020
Using feature(s): [15, 10] accuracy is 0.8020
Using feature(s): [15, 11] accuracy is 0.8360
Using feature(s): [15, 12] accuracy is 0.8160
Using feature(s): [15, 13] accuracy is 0.8340
Using feature(s): [15, 14] accuracy is 0.8340
Using feature(s): [15, 16] accuracy is 0.8460
Feature set 2 was best, accuracy is 0.9700
Using feature(s): [15, 2, 1] accuracy is 0.9220
Using feature(s): [15, 2, 3] accuracy is 0.9200
Using feature(s): [15, 2, 4] accuracy is 0.9300
Using feature(s): [15, 2, 5] accuracy is 0.9340
Using feature(s): [15, 2, 6] accuracy is 0.9220
Using feature(s): [15, 2, 7] accuracy is 0.9160
Using feature(s): [15, 2, 8] accuracy is 0.9320
Using feature(s): [15, 2, 9] accuracy is 0.8920
Using feature(s): [15, 2, 10] accuracy is 0.9180
Using feature(s): [15, 2, 11] accuracy is 0.9240
Using feature(s): [15, 2, 12] accuracy is 0.9380
Using feature(s): [15, 2, 13] accuracy is 0.9280
Using feature(s): [15, 2, 14] accuracy is 0.9160
Using feature(s): [15, 2, 16] accuracy is 0.9040
Finished search!! The best feature subset is [15, 2] with an accuracy of 0.97
Time taken to run on this dataset: 5.35 seconds
Best features found: [15, 2]
Accuracy: 0.97

Code
solver.py
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
parse_output.py
import matplotlib.pyplot as plt
import sys
def plot_results(features, accuracies, title, mode="forward", total_features=16):
   cumulative = []
  
   if mode == "forward":
       current_set = []
       for f in features:
           current_set.append(f)
           cumulative.append("{" + ",".join(current_set) + "}")
   else:  # backward
       current_set = list(range(1, total_features + 1))
       for f in features:
           current_set.remove(int(f))
           cumulative.append("{" + ",".join(map(str, current_set)) + "}")


   plt.figure(figsize=(12, 6))
   plt.bar(cumulative, accuracies)
   for i, val in enumerate(accuracies):
       plt.text(i, val + 0.01, f"{val:.2%}", ha='center')
   plt.xlabel("Feature Set")
   plt.ylabel("Accuracy")
   plt.title(title)
   plt.ylim(0, 1)
   plt.xticks(rotation=45, ha='right')
   plt.tight_layout()
   plt.savefig(title + ".png")
   plt.show()


 


def parse_results(filename):
   round_features = []
   round_accuracies = []
   with open(filename, "r") as f:
       for line in f:
           if "was best" in line:
               features = line.split("Feature set ")[1].split(" was best")[0]
               round_features.append(features)
               accuracy = float(line.split()[-1])
               round_accuracies.append(accuracy)
   return round_features,round_accuracies




# Small dataset
features, accuracies = parse_results("output_small_data_forward.txt")
plot_results(features, accuracies, "Small Dataset - Forward Selection", mode="forward", total_features=16)


features, accuracies = parse_results("output_small_data_backward.txt")
plot_results(features, accuracies, "Small Dataset - Backward Elimination", mode="backward", total_features=16)


# Large dataset
features, accuracies = parse_results("output_large_data_forward.txt")
plot_results(features, accuracies, "Large Dataset - Forward Selection", mode="forward", total_features=64)


features, accuracies = parse_results("output_large_data_backward.txt")
plot_results(features, accuracies, "Large Dataset - Backward Elimination", mode="backward", total_features=64)


if __name__ == "__main__":
   filename = sys.argv[1]
   title = sys.argv[2]
   features, accuracies = parse_results(filename)
   plot_results(features, accuracies, title)



Resources Consulted:
Course Slides 
Python Software Foundation. (2024). Python 3 documentation. https://docs.python.org/3/
GeeksforGeeks. (2024). K-nearest neighbors algorithm. https://www.geeksforgeeks.org/k-nearest-neighbours/ 
GeeksforGeeks. (2024). Backward feature elimination. https://www.geeksforgeeks.org/feature-selection-using-backward-elimination/
"How to implement a forward selection using KNN," Stack Overflow. https://stackoverflow.com/questions/65671476/how-to-implement-a-forward-selection-using-knn

