# MACHINE LEARNING 600 PRACTICAL 2
# Student name: Shivaar
# Student number: 402308101

import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# ============================================================
# SECTION A - FOUNDATIONS AND REASONING - 40 MARKS
# ============================================================

# Question 1 - Define the learning problem [5 marks]

#6. Express this phishing project using Task (T), Experience (E), and Performance measure (P).
print("Task (T): Classify a website, represented by its extracted URL/HTML structural "
      "features, as phishing (1) or legitimate (0).")
print("Experience (E): The historical, already-labelled dataset of 10000 website records "
      "(Phishing_Legitimate_full.csv) that the model learns from during training.")
print("Performance measure (P): A classification metric evaluated on unseen data, for "
      "example accuracy, precision, recall, F1-score, or AUC.")

#7. Explain how improved performance would demonstrate learning.
print("Learning is demonstrated when, after being exposed to experience E, the model's "
      "performance measure P improves on data it was NOT trained on - for example its "
      "test-set accuracy or F1-score rises above a naive baseline (always predicting the "
      "majority class). This shows the model is generalising patterns from E rather than "
      "memorising it.")

# Question 2 - Choose the learning type [5 marks]

#8. Compare supervised and unsupervised learning.
print("Supervised learning trains on labelled data (known input-output pairs) so the "
      "algorithm learns a mapping from inputs to a known target. Unsupervised learning "
      "works with unlabelled data, finding structure or patterns without being told the "
      "correct answer in advance.")

#9. Use CLASS_LABEL to justify which type fits this project.
print("Every row already has a known CLASS_LABEL (1 = phishing, 0 = legitimate). Because "
      "the ground-truth answer is available for every training example, the model can "
      "learn a direct mapping from the predictor features to this label - this is "
      "supervised learning.")

#10. State one useful unsupervised question that could still be asked of the predictors.
print("Ignoring CLASS_LABEL entirely, could clustering (e.g. k-means) on the structural "
      "URL/HTML features reveal natural sub-groups of websites without ever using the "
      "label?")

# Question 3 - Classification or regression [5 marks]

#11. Explain why predicting CLASS_LABEL is classification rather than regression.
print("CLASS_LABEL only takes two discrete values, 0 or 1. Predicting it means assigning "
      "the website to one of a fixed set of categories, not estimating a continuous "
      "quantity - this is a binary classification problem, not regression.")

#12. Describe a related regression question and name its continuous target.
print("Related regression question: What is the estimated phishing-risk score (0-100%) "
      "of a website, based on its features? Continuous target: a phishing risk "
      "probability/score.")

#13. State why the target determines the problem type.
print("The nature of the target variable fixes the task type: a categorical/discrete "
      "target means classification, a continuous numeric target means regression.")

# Question 4 - Separate column roles [5 marks]

#14. Identify the identifier, target, and predictors.
print("Identifier: id")
print("Target: CLASS_LABEL")
print("Predictors: the remaining 48 numeric columns (every column except id and CLASS_LABEL)")

#15. Explain why id should normally be excluded from the predictors.
print("id is only a row-reference number with no genuine relationship to phishing "
      "behaviour. Leaving it in risks the model memorising row identities instead of "
      "learning real patterns, so it is excluded from X.")

#16. Explain why including CLASS_LABEL in X would be target leakage.
print("If CLASS_LABEL were included as a predictor, the model would be given the answer "
      "as an input feature. It would look near-perfect during training/testing, but that "
      "would be meaningless because the label is never available at real prediction time "
      "- this is target leakage.")

# Question 5 - Apply data science competencies [5 marks]

#17. Name the three competencies in the Data Science Venn Diagram.
print("1. Mathematics & Statistics")
print("2. Computer Science / Programming (hacking skills)")
print("3. Domain / Subject-matter expertise")

#18. Match two competencies to practical tasks in this project.
print("Programming: writing the Python/pandas/scikit-learn code used to load, clean, "
      "split and scale the dataset in this script.")
print("Mathematics & Statistics: calculating IQR outlier bounds, class percentages, and "
      "understanding why standardisation (mean=0, std=1) is needed before scaling.")

# Question 6 - Recognise benefit and risk [5 marks]

#19. State one operational benefit of a phishing classifier.
print("It can automatically flag malicious URLs in real time before a user clicks them, "
      "reducing successful phishing attacks and credential theft.")

#20. Describe one plausible failure and its consequence.
print("A false negative - the model classifies an actual phishing site as legitimate. "
      "Consequence: the user is not warned and may enter credentials on the malicious "
      "site, resulting in real financial loss or identity theft.")

#21. Propose one control that reduces that risk.
print("Add a human-review layer for borderline-probability predictions, and continuously "
      "retrain the model on newly reported phishing sites so it keeps pace with evolving "
      "tactics.")

# Question 7 - Order the project cycle [5 marks]

#22. Place these activities in a defensible order.
print("1. Ask the question")
print("2. Acquire data")
print("3. Clean / prepare")
print("4. Test")
print("5. Report / refine")

#23. Explain why the question must be defined before data preparation.
print("The question determines what data is even relevant and what success looks like. "
      "Defining it first prevents wasted effort preparing irrelevant columns, and focuses "
      "every later decision on answering that specific question.")

# Question 8 - Create a mini project canvas [5 marks]

#24. One sentence each: problem, stakeholder, success measure, data source, privacy/bias risk.
print("Problem: Users and organisations are frequently targeted by phishing websites "
      "designed to steal credentials and financial information.")
print("Stakeholder: End users, IT security/SOC teams, and the organisation providing the "
      "browser or email security product.")
print("Success measure: A high recall and precision (or F1-score) for the phishing class "
      "on unseen test data.")
print("Data source: A structured, pre-extracted dataset of URL/HTML-based features for "
      "labelled legitimate and phishing websites (Phishing_Legitimate_full.csv).")
print("Privacy/bias risk: The dataset is a snapshot that may under-represent newer or "
      "region-specific phishing techniques, so the model could be biased toward the "
      "patterns present here.")


# ============================================================
# SECTION B - DATASET UNDERSTANDING AND QUALITY - 30 MARKS
# ============================================================

# Question 9 - Load and profile the dataset [5 marks]

DATA_FILE = Path("Phishing_Legitimate_full.csv")
df = pd.read_csv(DATA_FILE)
TARGET = "CLASS_LABEL"
ID_COL = "id"

#25. Display head(), shape, columns, info(), and describe().
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.info())
print(df.describe())

#26. Report the row count, column count, and number of numeric columns.
row_count, col_count = df.shape
numeric_col_count = df.select_dtypes(include="number").shape[1]

print("Row count:", row_count)
print("Column count:", col_count)
print("Numeric column count:", numeric_col_count)

# Question 10 - Audit column roles and balance [5 marks]

#27. Create a predictors list that excludes id and CLASS_LABEL, then report its length.
predictors = [c for c in df.columns if c not in [ID_COL, TARGET]]
print("Number of candidate predictors:", len(predictors))

#28. Report class counts and percentages in sorted order.
class_counts = df[TARGET].value_counts().sort_index()
class_percentages = df[TARGET].value_counts(normalize=True).sort_index() * 100

print("CLASS_LABEL counts (sorted):\n", class_counts)
print("CLASS_LABEL percentages (sorted):\n", class_percentages.round(2))

#29. Interpret whether the target is balanced.
print("Both classes contain exactly 5000 rows (50.0% each), so CLASS_LABEL is perfectly "
      "balanced. No resampling technique is required, and accuracy is a fair headline "
      "measure.")

# Question 11 - Implement five quality checks [5 marks]

#30. Check presence, type, range, length, and format using suitable columns or rules.
checks = []

# Presence check: no missing values anywhere
missing_total = df.isnull().sum().sum()
checks.append(["Presence", "No missing (null) values in any column", missing_total == 0])

# Type check: every predictor column has a numeric dtype
non_numeric_predictors = df[predictors].select_dtypes(exclude="number").columns.tolist()
checks.append(["Type", "All predictor columns are numeric", len(non_numeric_predictors) == 0])

# Range check: known binary flag columns only ever contain 0 or 1
binary_sample_cols = ["NoHttps", "InsecureForms", "IpAddress", "RandomString"]
range_ok = all(set(df[c].unique()).issubset({0, 1}) for c in binary_sample_cols)
checks.append(["Range", "Sample binary flag columns contain only {0,1}", range_ok])

# Length check: id column has exactly one unique id per row
length_ok = df[ID_COL].is_unique and df[ID_COL].nunique() == len(df)
checks.append(["Length", "id column is unique, one id per row", length_ok])

# Format check: CLASS_LABEL only contains the two valid category codes
format_ok = set(df[TARGET].unique()).issubset({0, 1})
checks.append(["Format", "CLASS_LABEL only contains valid codes {0,1}", format_ok])

#31. Show a compact pass/fail summary.
quality_summary = pd.DataFrame(checks, columns=["Check", "Description", "Pass"])
print(quality_summary.to_string(index=False))

#32. Explain one limitation of your checks.
print("These checks confirm structural validity (correct dtype, expected range, no "
      "duplicate identifiers) but cannot verify semantic correctness - for example "
      "whether a NumDots value was extracted accurately from the real webpage.")

# Question 12 - Decide how to handle missing data [5 marks]

#33. Report missing cells by column and in total.
missing_per_column = df.isnull().sum()
total_missing = df.isnull().sum().sum()

print("Missing values per column:\n", missing_per_column)
print("Total missing cells:", total_missing)

#34. State the action required for this dataset.
if total_missing == 0:
    print("No imputation is required for this dataset - every cell is populated.")
else:
    print("Imputation is required for this dataset.")

#35. If a numeric predictor later contained missing values, propose a defensible treatment.
print("A defensible approach would be median imputation fitted on the training set only "
      "(medians are robust to outliers/skew), combined with an added missing-indicator "
      "column so the model can learn if the fact a value was missing carries signal. "
      "Fitting the imputation value on X_train only, then applying it unchanged to "
      "X_test, avoids leaking test-set information.")

# Question 13 - Distinguish two kinds of repetition [5 marks]

#36. Count exact full-row duplicates.
exact_duplicates = df.duplicated().sum()
print("Exact full-row duplicates:", exact_duplicates)

#37. Count repeated predictor-plus-target patterns after excluding id.
feature_target_duplicates = df.drop(columns=[ID_COL]).duplicated().sum()
print("Repeated feature-plus-target patterns (excluding id):", feature_target_duplicates)

#38. Explain why repeated patterns should not automatically be deleted.
print("A repeated feature-plus-target pattern is not automatic proof that two rows "
      "describe the same website - different, genuinely distinct websites can share "
      "identical values across these engineered structural features. Since these are "
      "derived attributes rather than a direct record of website identity, the correct "
      "approach is to retain such rows unless external evidence proves true duplication.")

# Question 14 - Explain acquisition and ETL [5 marks]

#39. Name one realistic method for acquiring similar website data.
print("Use a web crawler / URL-scraping pipeline, or subscribe to a threat-intelligence "
      "feed such as PhishTank or OpenPhish, that visits known-phishing and "
      "known-legitimate URLs and extracts the same structural features.")

#40. Describe one Extract, one Transform, and one Load activity.
print("Extract: pull the raw HTML source and URL string of each site during the crawl.")
print("Transform: parse the raw HTML/URL to compute numeric structural features (e.g. "
      "NumDots, PctExtHyperlinks) and assign CLASS_LABEL based on the verified source list.")
print("Load: insert/append the transformed feature rows into a structured store, e.g. a "
      "SQL table or a versioned CSV file like this one.")

#41. State one storage, privacy, or legal consideration.
print("Crawling and storing website content can raise legal/ethical issues - the crawler "
      "should respect robots.txt and each site's terms of service, and must avoid "
      "capturing personally identifiable information found on scraped pages.")


# ============================================================
# SECTION C - LEAKAGE-AWARE PREPROCESSING - 30 MARKS
# Core principle: any learned preprocessing rule must be fitted on training
# data only, then applied unchanged to test data.
# ============================================================

# Question 15 - Build X and y [5 marks]

#42. Create X from predictors and y from CLASS_LABEL.
X = df[predictors].copy()
y = df[TARGET].copy()

#43. Detect non-numeric and constant predictors.
non_numeric_cols = X.select_dtypes(exclude="number").columns.tolist()
constant_cols = [c for c in X.columns if X[c].nunique() == 1]

print("Non-numeric predictor columns:", non_numeric_cols)
print("Constant predictor columns:", constant_cols)

#44. Remove constant predictors and report the final predictor count.
X = X.drop(columns=constant_cols)
print("Final predictor count after removing constants:", X.shape[1])

# Question 16 - Create a reproducible split [5 marks]

#45. Create an 80/20 train-test split with random_state=42 and stratify=y.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

#46. Report all four shapes and the class counts in y_train and y_test.
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)
print("Class counts in y_train:\n", y_train.value_counts())
print("Class counts in y_test:\n", y_test.value_counts())

#47. Explain the purpose of random_state and stratify.
print("random_state=42 fixes the seed of the random number generator so the split is "
      "reproducible every time the code is run. stratify=y forces the train and test "
      "sets to preserve the same class proportions as the full dataset (50/50), "
      "preventing an unlucky split from over/under-representing either class.")

# Question 17 - Audit outliers [5 marks]

#48. Using X_train only, calculate IQR limits and flagged counts for the 5 features.
outlier_features = ["UrlLength", "HostnameLength", "PathLength", "QueryLength", "NumNumericChars"]

iqr_results = []
for col in outlier_features:
    Q1 = X_train[col].quantile(0.25)
    Q3 = X_train[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    flagged = ((X_train[col] < lower) | (X_train[col] > upper)).sum()
    iqr_results.append([col, Q1, Q3, IQR, lower, upper, flagged])

iqr_df = pd.DataFrame(
    iqr_results,
    columns=["Feature", "Q1", "Q3", "IQR", "Lower Limit", "Upper Limit", "Flagged Outliers"]
)
print(iqr_df.to_string(index=False))

#49. Explain why QueryLength produces a zero-width IQR.
print("About 80% of QueryLength values in the training set are exactly 0 (no query "
      "string in the URL), so both Q1 and Q3 land on 0, making IQR = 0. Any non-zero "
      "QueryLength value then gets technically flagged as an outlier, even though "
      "non-zero query strings are common and can be meaningful.")

#50. Choose and justify an outlier action; do not apply it yet.
print("Recommended action: cap (winsorize) the four length/count features other than "
      "QueryLength at their IQR bounds, learned from X_train only, rather than deleting "
      "rows, since extreme URL/hostname/path lengths can be genuine phishing signal. "
      "QueryLength should not use the standard IQR rule (see #49) and would need a "
      "different, domain-informed rule instead. This action is only proposed here and "
      "is NOT applied in this script, per the leakage-aware instruction for this section.")

# Question 18 - Prevent preprocessing leakage [5 marks]

#51. Explain data leakage in this context.
print("Data leakage occurs when information from the test set is allowed to influence "
      "how the training pipeline is built. In preprocessing, this happens if a scaler or "
      "outlier rule is fitted using statistics computed from the whole dataset instead of "
      "the training partition alone.")

#52. Describe the correct fit/transform sequence for a scaler or outlier rule.
print("1. Split the data into train and test first. "
      "2. Fit the scaler/outlier rule using only X_train. "
      "3. Transform both X_train and X_test using that already-fitted rule - X_test is "
      "never used to (re-)fit anything.")

#53. State why fitting on the complete dataset gives an unfair evaluation.
print("If the scaler is fitted on the complete dataset, the test set's own mean/variance "
      "shapes the transformation later applied back to it. This makes the unseen test "
      "data artificially easier, inflating the reported evaluation metrics.")

# Question 19 - Scale and verify [5 marks]

#54. Fit StandardScaler on X_train and transform X_train and X_test.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns, index=X_train.index)
X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns, index=X_test.index)

#55. Confirm that the scaled arrays have the expected shapes and contain no NaN or infinite values.
print("X_train_scaled shape:", X_train_scaled.shape)
print("X_test_scaled shape:", X_test_scaled.shape)
print("Missing values in X_train_scaled:", X_train_scaled.isnull().sum().sum())
print("Missing values in X_test_scaled:", X_test_scaled.isnull().sum().sum())
print("Infinite values in X_train_scaled:", np.isinf(X_train_scaled.values).sum())
print("Infinite values in X_test_scaled:", np.isinf(X_test_scaled.values).sum())

#56. Explain why scaling is useful for some algorithms but not always necessary for trees.
print("Distance and gradient-based algorithms (k-NN, logistic regression, SVM, neural "
      "networks) are sensitive to the numeric scale of each feature, so scaling puts "
      "every feature on a comparable footing. Tree-based models split the data using "
      "threshold comparisons on one feature at a time, so the split quality is unaffected "
      "by the feature's absolute scale - trees generally do not need scaling.")

# Question 20 - Write the readiness recommendation [5 marks]

#57. Select two suitable supervised classification algorithms and justify each.
print("Logistic Regression: a strong, interpretable baseline that suits this scaled, "
      "almost entirely numeric feature set and binary target.")
print("Random Forest / Gradient-Boosted Trees: handles non-linear relationships and "
      "feature interactions well, robust to outliers, doesn't require scaling.")

#58. Select two evaluation measures and explain what each would reveal.
print("Recall (sensitivity) for the phishing class: reveals how many actual phishing "
      "sites the model successfully catches - missing one is the costlier error.")
print("Precision / F1-score: reveals how many flagged sites are truly phishing, guarding "
      "against false alarms; F1 balances both.")

#59. Give a final go / revise / stop recommendation, supported by one dataset result.
print("Go. The dataset is clean and ready for modelling: zero missing values, zero exact "
      "full-row duplicates, a perfectly balanced 50/50 class split, and 47 numeric, "
      "non-constant predictors after removing HttpsInHostname.")
