# import pandas as pd
#
# df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
# print(df.head())
# print(df.shape)

# from sklearn.datasets import load_iris
# import pandas as pd
#
# iris = load_iris()
# df = pd.DataFrame(iris.data, columns=iris.feature_names)
# df["species"] = iris.target
# print(df.head())

#Full code answer
# Practical Questions – Chapter 2 (PCA)
# Done with help from study notes + trying the code myself

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris, load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ============================================================
# 1. Iris – load, preprocess, PCA
# ============================================================
print("=" * 50)
print("1. Iris dataset + PCA")
print("=" * 50)

iris = load_iris()
X_iris = iris.data
y_iris = iris.target

# scale first (PCA needs scaled data)
scaler_iris = StandardScaler()
X_iris_scaled = scaler_iris.fit_transform(X_iris)

# full PCA to see variance
pca_iris = PCA()
pca_iris.fit(X_iris_scaled)
cum_iris = np.cumsum(pca_iris.explained_variance_ratio_)

print("Explained variance ratio:", pca_iris.explained_variance_ratio_)
print("Cumulative variance:", cum_iris)

# keep components that cover at least 95%
n_iris = int(np.argmax(cum_iris >= 0.95) + 1)
print("Components for >=95% variance:", n_iris)

X_iris_pca = PCA(n_components=n_iris).fit_transform(X_iris_scaled)
print("Original shape:", X_iris.shape)
print("After PCA shape:", X_iris_pca.shape)

# simple 2D plot of first 2 PCs
pca2 = PCA(n_components=2)
X_iris_2d = pca2.fit_transform(X_iris_scaled)

plt.figure(figsize=(6, 4))
plt.scatter(X_iris_2d[:, 0], X_iris_2d[:, 1], c=y_iris, cmap="viridis")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Iris after PCA (2 components)")
plt.tight_layout()
plt.show()


# ============================================================
# 2. Breast Cancer – does accuracy improve after PCA?
# ============================================================
print("\n" + "=" * 50)
print("2. Breast Cancer – accuracy before vs after PCA")
print("=" * 50)

cancer = load_breast_cancer()
X_c = cancer.data
y_c = cancer.target

X_train, X_test, y_train, y_test = train_test_split(
    X_c, y_c, test_size=0.2, random_state=42, stratify=y_c
)

scaler_c = StandardScaler()
X_train_s = scaler_c.fit_transform(X_train)
X_test_s = scaler_c.transform(X_test)

# model on original scaled features
model_orig = LogisticRegression(max_iter=1000, random_state=42)
model_orig.fit(X_train_s, y_train)
acc_orig = accuracy_score(y_test, model_orig.predict(X_test_s))
print("Accuracy WITHOUT PCA:", round(acc_orig, 4))

# PCA – keep 95% variance
pca_c = PCA()
pca_c.fit(X_train_s)
cum_c = np.cumsum(pca_c.explained_variance_ratio_)
n_c = int(np.argmax(cum_c >= 0.95) + 1)
print("Components kept for 95% variance:", n_c)

pca_final = PCA(n_components=n_c)
X_train_pca = pca_final.fit_transform(X_train_s)
X_test_pca = pca_final.transform(X_test_s)

model_pca = LogisticRegression(max_iter=1000, random_state=42)
model_pca.fit(X_train_pca, y_train)
acc_pca = accuracy_score(y_test, model_pca.predict(X_test_pca))
print("Accuracy WITH PCA:", round(acc_pca, 4))

if acc_pca >= acc_orig:
    print("PCA did not hurt accuracy (similar or slightly better).")
else:
    print("Accuracy dropped a bit after PCA, but we used fewer features.")


# ============================================================
# 3. Synthetic high-dimensional data + PCA plot
# ============================================================
print("\n" + "=" * 50)
print("3. Synthetic high-D data visualised after PCA")
print("=" * 50)

np.random.seed(42)
# 300 samples, 50 features (high dimensional)
X_syn = np.random.randn(300, 50)

X_syn_scaled = StandardScaler().fit_transform(X_syn)
X_syn_2d = PCA(n_components=2).fit_transform(X_syn_scaled)

plt.figure(figsize=(6, 4))
plt.scatter(X_syn_2d[:, 0], X_syn_2d[:, 1], alpha=0.7)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Synthetic 50-D data reduced to 2-D with PCA")
plt.tight_layout()
plt.show()

print("Original synthetic shape:", X_syn.shape)
print("After PCA (2D) shape:", X_syn_2d.shape)
