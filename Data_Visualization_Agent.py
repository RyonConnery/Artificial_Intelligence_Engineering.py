# Step 1: Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


# Step 2: Load the Iris dataset
iris = load_iris()
X = iris.data  # Feature matrix
y = iris.target  # Target vector


# Step 3: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)


# Step 4: Initialize and train the decision tree classifier
clf = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

clf.fit(X_train, y_train)


# Step 5: Evaluate the classifier's performance
y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(
    f"Accuracy of the Decision Tree Classifier: "
    f"{accuracy:.2f}"
)


# Step 6: Visualize the decision tree
plt.figure(figsize=(12, 8))

plot_tree(
    clf,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True
)

plt.title("Decision Tree Visualization")
plt.show()


# Step 7: Display the textual representation of the tree
tree_rules = export_text(
    clf,
    feature_names=iris.feature_names
)

print("Decision Tree Rules:")
print(tree_rules)
