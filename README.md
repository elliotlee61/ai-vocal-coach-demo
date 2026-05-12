# AI Vocal Coach Demo

This project is a proposal-day prototype for an AI vocal coach. The goal is to analyze a short singing clip and give beginner-friendly feedback.

## Current Demo

The current demo uses vocal audio from VocalSet / Annotated VocalSet and classifies a short clip into a basic vocal technique category such as breathy, vibrato, or straight tone. The prediction is converted into simple coaching feedback.

## Pipeline

Audio clip → feature extraction → technique classifier → predicted label → coaching feedback

## Dataset

Dataset source: VocalCoachingDatasets GitHub resource.
Planned dataset: VocalSet or Annotated VocalSet.

The full dataset is not included in this repository because of file size and licensing.

## How to Run

1. Install requirements:
pip install -r requirements.txt

2. Add dataset clips into:
data/breathy/
data/vibrato/
data/straight/

3. Train model:
python train_model.py

4. Run demo:
python demo.py

## Proposal Day Scope

For 5/12, the demo shows a small AI pipeline that analyzes a singing clip and outputs coaching feedback.

## Final Project Plan

Future work:
- Add NanoPitch pitch tracking
- Add note-level pitch accuracy
- Add pitch trace visualization
- Add more vocal technique categories
- Build a simple web interface
