# MACHINE LEARNING 600 PRACTICAL 1
# Student name: Shivaar
# Student number: 402308101

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#27.
df = pd.read_csv("Phishing_Legitimate_full.csv")
#print(dataset)

#28.
print(df.head())
print(df.shape)

#29.
for col in df.columns:
    print(col)

#30.
print(df.info())

#31.
print(df.describe())

#32.
print(df.isnull().sum())

#33.
missing_per_column = df.isnull().sum()
print("\nMissing values per column :", missing_per_column)

total_missing = df.isnull().sum().sum()
print("\nTotal missing cells", total_missing)

if total_missing == 0:
    print("No imputations required")
else:
    print("Imputation is required")

#34.
identifier = "id"
target = "CLASS_LABEL"

predictors = [col for col in df.columns if col not in [identifier, target]]

print("Identifier:", identifier)
print("Target:", target)
print("Number of candidate predictors:", len(predictors))

#35.
#occurances of each class
class_counts = df["CLASS_LABEL"].value_counts()

class_percentages = df['CLASS_LABEL'].value_counts(normalize=True) * 100

#results
print("CLASS_LABEL counts:\n", class_counts)
print("\nCLASS_LABEL percentages:\n", class_percentages.round(2))


#explaintaion of why this is a structured, supervised and classification problem
print("This is a **structured problem** because the dataset is organized into rows (each website"
      " observation) and columns (predictor features plus the target label). It is a supervised"
      " classification task because the target column `CLASS_LABEL` provides known categories "
      "(phishing vs legitimate) that the model learns from in order to predict the correct class"
      " for new observations.")

#36.
df_work = df.copy()

Total_missing = df_work.isnull().sum().sum()
print("Total missing values : ", total_missing)

if total_missing == 0:
    print("No imputations performed")
else:
    print("Imputations performed")

#37.
before_rows = len(df_work)
duplicate_count = df_work.duplicated().sum()

#drop duplicates
df_work = df_work.drop_duplicates()
after_rows = len(df_work)

#results
print("Exact full-row duplicates:", duplicate_count)
print("Rows before:", before_rows)
print("Rows after:", after_rows)

#38.
feature_target_duplicates = df_work.drop(columns=['id']).duplicated().sum()

print("Repeated feature-plus-target patterns (excluding id):", feature_target_duplicates)

#39.
print("Repeated engineered feature patterns are not automatically proof that two rows represent "
      "the same website because different sites can share identical characteristics (for example, "
      "similar URL lengths, numeric counts, or page structures). Since these features are derived "
      "attributes rather than direct provenance, they cannot confirm duplication; therefore, the"
      " correct approach is to **retain them** unless external evidence shows they are duplicate"
      " observations, ensuring the dataset remains representative of diverse but potentially "
      "similar websites.")

#40.
non_numeric_predictors = df_work.drop(columns=['id','CLASS_LABEL']).select_dtypes(exclude=['number']).columns

print("Non-numeric predictor columns:", list(non_numeric_predictors))

# State whether encoding is required
if len(non_numeric_predictors) > 0:
    print("Encoding required: one-hot for categorical features, label encoding if ordinal.")
else:
    print("No encoding required: all predictors are numeric.")


#41.
print("CLASS_LABEL dtype:", df['CLASS_LABEL'].dtype)

# Confirm scaling rule
if pd.api.types.is_numeric_dtype(df['CLASS_LABEL']):
    print("CLASS_LABEL is already numeric and must NOT be included in predictor scaling.")
else:
    print("CLASS_LABEL is not numeric and requires encoding, but still must NOT be scaled as a predictor.")

#42.
constant_predictors = [col for col in df_work.drop(columns=['id','CLASS_LABEL']).columns
                       if df_work[col].nunique() == 1]

print("Constant predictors:", constant_predictors)

#remove them from predictor set
df_work = df_work.drop(columns=constant_predictors)
print("Removed constant predictors from predictor set.")

#43.
#separate predictors (X) and target (y)
X = df.drop(columns=['id','CLASS_LABEL'])
y = df['CLASS_LABEL']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

#44.
#display shapes
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

#verify class counts
print("\nClass counts in y_train:\n", y_train.value_counts())
print("\nClass counts in y_test:\n", y_test.value_counts())

#45.
features = ['UrlLength','HostnameLength','PathLength','QueryLength','NumNumericChars']

iqr_results = []

for col in features:
    Q1 = X_train[col].quantile(0.25)
    Q3 = X_train[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    flagged = ((X_train[col] < lower) | (X_train[col] > upper)).sum()
    iqr_results.append([col, lower, upper, flagged])

# Display neatly
iqr_df = pd.DataFrame(iqr_results, columns=['Feature','Lower Limit','Upper Limit','Flagged Outliers'])
print(iqr_df)


#46.
print("The IQR rule should not be applied blindly to certain types of features because"
      " its assumptions break down:"
      "For binary indicators (0/1 variables), the quartiles are fixed (Q1 = 0, Q3 = 1), "
      "so the IQR is always 1. Applying the outlier rule would incorrectly flag normal "
      "values as “outliers,” even though both 0 and 1 are valid."
      "For a zero‑inflated feature where both Q1 and Q3 equal 0, the IQR collapses to 0. In "
      "that case, any non‑zero value would be flagged as an outlier, even if those values are"
      " legitimate and informative.")

#47.
print("For the length/count features (like UrlLength, HostnameLength, PathLength, QueryLength,"
      " NumNumericChars), a defensible treatment balances realism with robustness:"
      "Retain plausible extremes: Very long URLs or hostnames can genuinely occur in phishing sites,"
      " so discarding them outright risks losing signal."
      "Cap selected features: Use the training‑derived IQR limits to cap extreme values rather than"
      " remove rows. This prevents distortion while keeping all observations."
      "Apply a robust transformation: For skewed count distributions, a log or square‑root transform "
      "reduces the influence of large values without discarding them."
      "Combination justification")

#48.
# FIX: the limits dict previously referenced url_lower, host_lower, etc. that were never
# created anywhere in the script (that's the "Unresolved reference" bug PyCharm flagged).
# The lower/upper bounds for each feature were already calculated in #45 and stored in
# iqr_df, so build the dict straight from there instead of from undefined variables.
limits = {
    row['Feature']: {'lower': row['Lower Limit'], 'upper': row['Upper Limit']}
    for _, row in iqr_df.iterrows()
}

# Apply limits to X_test without recomputing
X_test_capped = X_test.copy()
for col, lim in limits.items():
    X_test_capped[col] = X_test_capped[col].clip(lower=lim['lower'], upper=lim['upper'])

# Confirm row counts and labels unchanged
print("Row count before:", X_test.shape[0])
print("Row count after:", X_test_capped.shape[0])
print("\nClass counts unchanged:\n", y_test.value_counts())

#49.
scaler = StandardScaler()

#fit on training predictors only
scaler.fit(X_train)

print("Scaler fitted on X_train predictors only.")

#50.
#assume scaler has already been fitted on X_train
scaler = StandardScaler()
scaler.fit(X_train)

#transform training and test predictors
X_train_scaled = pd.DataFrame(
    scaler.transform(X_train),
    columns=X_train.columns,
    index=X_train.index
)

X_test_scaled = pd.DataFrame(
    scaler.transform(X_test),
    columns=X_test.columns,
    index=X_test.index
)

# Confirm shapes and integrity
print("X_train_scaled shape:", X_train_scaled.shape)
print("X_test_scaled shape:", X_test_scaled.shape)

#51.
#display shapes
print("X_train_scaled shape:", X_train_scaled.shape)
print("X_test_scaled shape:", X_test_scaled.shape)

#confirm no missing values
print("Missing values in X_train_scaled:", X_train_scaled.isnull().sum().sum())
print("Missing values in X_test_scaled:", X_test_scaled.isnull().sum().sum())

#confirm no infinite values
print("Infinite values in X_train_scaled:", np.isinf(X_train_scaled.values).sum())
print("Infinite values in X_test_scaled:", np.isinf(X_test_scaled.values).sum())

#52.
print("Scaling is crucial because it ensures that features contribute fairly "
      "and meaningfully in models that rely on distances, gradients, or variance:"
      "Distance‑based models (e.g., k‑NN, clustering)  "
      "These models compute similarity using Euclidean or other distance metrics."
      " If one feature has a much larger numeric range (say URL length in hundreds "
      "vs. binary flags in 0/1), it will dominate the distance calculation. Scaling "
      "equalizes ranges so all predictors influence the distance measure appropriately."
      "Gradient‑based models (e.g., logistic regression, neural networks, SVMs)  "
      "Optimization relies on gradient descent. If features are on very different scales,"
      " the cost function contours become skewed, causing slow or unstable convergence. "
      "Standardization makes the optimization landscape smoother, speeding up training "
      "and improving stability."
      "Principal Component Analysis (PCA) "
      "PCA is variance‑based: it identifies directions of maximum variance. Without scaling, "
      "features with large numeric ranges artificially dominate the variance, biasing the "
      "principal components. Standardization ensures PCA reflects genuine structure rather "
      "than raw magnitude differences.")

#53.
print("If you fit the scaler before the train/test split, you allow information from the"
      " test set to influence the scaling parameters (mean and standard deviation). That’s"
      " data leakage because the model indirectly “sees” the test distribution during training, "
      "which inflates performance estimates."
      "If you fit the scaler separately on X_test, you create a different feature space: the test"
      " set gets scaled with its own mean and variance, which no longer match the training set. "
      "This breaks consistency, because the model expects predictors transformed in the same way "
      "as the training data.")