# AI Vocal Coach Demo

## Project Overview

This project is a proposal-stage prototype for an AI vocal coach. The goal is to analyze a short singing clip and provide beginner-friendly feedback about vocal technique.

For Proposal Day, I built a small working demo that classifies a vocal clip as one of three technique categories:

- breathy
- straight
- vibrato

The demo then converts the predicted technique into simple coaching feedback.

## Dataset Selection

I started from the provided GitHub database:

https://github.com/charisrenee/VocalCoachingDatasets/blob/main/datasets.csv

I reviewed several dataset options from the database:

| Dataset | Why it matters | Use in this project |
|---|---|---|
| VocalSet | Contains vocal technique categories such as breathy, vibrato, belt, and others | Chosen for proposal demo |
| Annotated-VocalSet | Adds note-level and pitch/F0 annotations | Possible final project extension |
| GTSinger | Larger singing dataset with technique and pitch information | Possible future extension |
| VocalVerse / SingMD | Singing evaluation and expert feedback | Possible future scoring/feedback layer |
| SingEval | Karaoke-style singing assessment | Possible future evaluation dataset |

## Chosen Dataset for Proposal Demo

I chose VocalSet because it directly matches my current demo goal: vocal technique recognition.

For the proposal demo, I used a small local subset of VocalSet with three technique labels:

- breathy
- straight
- vibrato

The full dataset is not included in this repository because it is large and should remain local.

## Current Demo Pipeline

```text
VocalCoachingDatasets GitHub database
→ choose VocalSet
→ select breathy / straight / vibrato clips
→ extract MFCC audio features
→ train Random Forest classifier
→ predict vocal technique
→ output beginner-friendly coaching feedback
