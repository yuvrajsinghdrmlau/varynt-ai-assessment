def classify_lead(data):

    score = 0

    if "urgent" in data["message"].lower():
        score += 40

    if "immediate" in data["timeline"].lower():
        score += 30

    if "10000" in data["budget"]:
        score += 20

    if score >= 70:
        lead_type = "HOT"

    elif score >= 40:
        lead_type = "WARM"

    else:
        lead_type = "COLD"

    return {
        "lead_type": lead_type,
        "score": score
    }