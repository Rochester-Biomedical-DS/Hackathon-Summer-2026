

# The plan: 

# Can we predict the cell type based on MERFISH gene experession
# #pattern? 

# Working pipeline:
# 1. load the counts_train.csv file ( maybe train this alone first?)
# 2. load meta_train.csv file
# 3. Get the known cell type labels (from meta_train csv file)
# 4. Split the labeled cells into training portion and testing portion( training file ONLY)
# Question to self: how to split the data?
# 5. preprocess the gene counts ( then meta file later)
# 6. Train trying the logistic regression model first
# 7. predict the validation cells
# 8. calculate accuracy
# 9. inspect mistakes if its bad, to help determine new model choice
# 10. Decide the next model. random forest ? ( add list of models here)

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# -----------------------------
# Load training data
# -----------------------------

counts = pd.read_csv("data/counts_train.csv", index_col=0)
meta = pd.read_csv("data/meta_train.csv", index_col=0)

# Make sure gene counts and metadata refer to the same cells
assert counts.index.equals(meta.index)

X = counts
y = meta["MERFISH_cell_type_annotation"]


# -----------------------------
# Train / validation split
# -----------------------------

X_train, X_val, y_train, y_val = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# -----------------------------
# Preprocess gene counts
# -----------------------------

X_train_log = np.log1p(X_train)
X_val_log = np.log1p(X_val)


# -----------------------------
# Logistic Regression baseline
# -----------------------------

model = LogisticRegression(max_iter=2000)
model.fit(X_train_log, y_train)

y_pred = model.predict(X_val_log)

accuracy = accuracy_score(y_val, y_pred)
print("Validation accuracy:", accuracy)


# -----------------------------
# Train final model on all
# labeled training cells
# -----------------------------

final_model = LogisticRegression(max_iter=2000)
final_model.fit(np.log1p(X), y)


# -----------------------------
# Load test data
# -----------------------------

counts_test = pd.read_csv("data/counts_test.csv", index_col=0)
meta_test = pd.read_csv("data/meta_test.csv", index_col=0)

# The hackathon requires predictions in meta_test order
assert counts_test.index.equals(meta_test.index)

counts_test_log = np.log1p(counts_test)


# -----------------------------
# Predict test cell types
# -----------------------------

test_pred = final_model.predict(counts_test_log)


# -----------------------------
# Create submission file
# -----------------------------

prediction = pd.DataFrame({
    "Cell_ID": meta_test.index,
    "MERFISH_cell_type_annotation.y": test_pred
})

print("Prediction shape:", prediction.shape)
print("Number of predicted cell types:",
      prediction["MERFISH_cell_type_annotation.y"].nunique())

prediction.to_csv(
    "prediction/prediction.csv",
    index=False
)

print("Saved prediction/prediction.csv")


