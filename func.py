def classify_rating(vote_average):
    """
    Convert a numeric rating (0–100) into a label.
    - 0–25%   → "Not Interested"
    - 26–50% → "Average"
    - 51–75% → "Good"
    - 76–100 → "Likable"
    """
    if vote_average <= 25:
        return "Not Interested"
    elif vote_average <= 50:
        return "Average"
    elif vote_average <= 75:
        return "Good"
    else:
        return "Likable"

    