import os
import librosa
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


DATA_DIR = "data"
MODEL_PATH = "models/vocal_technique_model.pkl"


def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=22050)

    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
    mfcc_mean = np.mean(mfcc, axis=1)
    mfcc_std = np.std(mfcc, axis=1)

    features = np.concatenate([mfcc_mean, mfcc_std])
    return features


def load_dataset():
    X = []
    y = []

    for label in os.listdir(DATA_DIR):
        label_path = os.path.join(DATA_DIR, label)

        if not os.path.isdir(label_path):
            continue

        for file_name in os.listdir(label_path):
            if file_name.lower().endswith((".wav", ".mp3", ".flac")):
                file_path = os.path.join(label_path, file_name)
                features = extract_features(file_path)
                X.append(features)
                y.append(label)

    return np.array(X), np.array(y)


def main():
    X, y = load_dataset()

    if len(X) == 0:
        print("No audio files found. Add clips to data/breathy, data/vibrato, and data/straight.")
        return

    print(f"Loaded {len(X)} audio files.")
    print(f"Labels: {sorted(set(y))}")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print("\nEvaluation:")
    print(classification_report(y_test, predictions))

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print(f"\nSaved model to {MODEL_PATH}")


if __name__ == "__main__":
    main()
