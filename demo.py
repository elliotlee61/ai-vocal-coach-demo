import os
import librosa
import numpy as np
import joblib

from feedback import get_feedback


MODEL_PATH = "models/vocal_technique_model.pkl"


def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=22050)

    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
    mfcc_mean = np.mean(mfcc, axis=1)
    mfcc_std = np.std(mfcc, axis=1)

    features = np.concatenate([mfcc_mean, mfcc_std])
    return features.reshape(1, -1)


def main():
    if not os.path.exists(MODEL_PATH):
        print("Model not found. Run train_model.py first.")
        return

    model = joblib.load(MODEL_PATH)

    file_path = input("Enter path to a singing audio file: ").strip()

    if not os.path.exists(file_path):
        print("File not found.")
        return

    features = extract_features(file_path)
    prediction = model.predict(features)[0]

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(features)[0]
        confidence = max(probabilities)
    else:
        confidence = None

    print("\nAI Vocal Coach Demo")
    print("-------------------")
    print(f"Audio file: {file_path}")
    print(f"Predicted technique: {prediction}")

    if confidence is not None:
        print(f"Confidence: {confidence:.2f}")

    print("\nCoach feedback:")
    print(get_feedback(prediction))


if __name__ == "__main__":
    main()
