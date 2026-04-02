from sklearn.ensemble import IsolationForest
from sklearn.feature_extraction.text import TfidfVectorizer

def detect_anomalies(df):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["message"])

    model = IsolationForest(contamination=0.1)
    df["anomaly"] = model.fit_predict(X.toarray())

    anomalies = df[df["anomaly"] == -1]["message"].tolist()
    return anomalies