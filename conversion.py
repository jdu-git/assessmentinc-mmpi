import json
import os

BASE = os.path.dirname(__file__)

with open(os.path.join(BASE, "norms/male_basic.json")) as f:
    MALE_BASIC = json.load(f)

with open(os.path.join(BASE, "norms/female_basic.json")) as f:
    FEMALE_BASIC = json.load(f)

with open(os.path.join(BASE, "norms/male_supplementary.json")) as f:
    MALE_SUPPLEMENTARY = json.load(f)

with open(os.path.join(BASE, "norms/female_supplementary.json")) as f:
    FEMALE_SUPPLEMENTARY = json.load(f)


def convert_basic(scale, raw, gender):
    """Convert a raw score to a T-score for a basic scale.
    Returns None if no mapping exists."""
    gender = gender.lower()
    table = MALE_BASIC if gender == "male" else FEMALE_BASIC

    scale_table = table.get(scale)
    if scale_table is None:
        return None

    return scale_table.get(str(raw))


def convert_supplementary(scale, raw, gender):
    """Convert a raw score to a T-score for a supplementary scale.
    Returns None if no mapping exists."""
    gender = gender.lower()
    table = MALE_SUPPLEMENTARY if gender == "male" else FEMALE_SUPPLEMENTARY

    scale_table = table.get(scale)
    if scale_table is None:
        return None

    return scale_table.get(str(raw))

