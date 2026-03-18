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