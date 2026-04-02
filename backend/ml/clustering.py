from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

def cluster_logs(df):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["message"])

    kmeans = KMeans(n_clusters=5)
    df["cluster"] = kmeans.fit_predict(X)

    clusters = {}
    for i in range(5):
        clusters[f"cluster_{i}"] = df[df["cluster"] == i]["message"].tolist()

    return clusters