def get_feedback(label):
    feedback = {
        "breathy": "Your tone sounds breathy. Try using steadier airflow and keeping the sound more connected.",
        "vibrato": "You are using vibrato. Try keeping the vibrato rate even and avoid letting the pitch wobble too widely.",
        "straight": "Your tone sounds mostly straight and stable. Try maintaining that stability across the whole phrase."
    }

    return feedback.get(label, "The system detected a vocal technique, but feedback for this label is still being developed.")
