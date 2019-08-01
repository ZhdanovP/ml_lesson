import pandas as pd
from sklearn.preprocessing import StandardScaler

cust_df = pd.read_csv("Cust_Segmentation.csv")
cust_df.head()

X = df.values[:,1:]
X = np.nan_to_num(X)
Clus_dataSet = StandardScaler().fit_transform(X)

clusterNum = 3
k_means = KMeans(init = "k-means++", n_clusters = clusterNum, n_init = 12)
k_means.fit(X)
labels = k_means.labels_
print(labels)