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
    if gender.lower() == "male":
        table = MALE_BASIC
    elif gender.lower() == "female":
        table = FEMALE_BASIC
    else:
        raise ValueError(f"Invalid gender: {gender}")

    if scale not in table:
        raise ValueError(f"Scale '{scale}' not found in table for {gender}")

    scale_table = table[scale]

    T_score = scale_table.get(str(raw))
    if T_score is not None:
        return T_score
    else:
        return 0

def convert_supplementary(scale, raw, gender):
    if gender.lower() == "male":
        table = MALE_SUPPLEMENTARY
    elif gender.lower() == "female":
        table = FEMALE_SUPPLEMENTARY
    else:
        raise ValueError(f"Invalid gender: {gender}")

    if scale not in table:
        raise ValueError(f"Scale '{scale}' not found in supplementary table for {gender}")

    scale_table = table[scale]

    T_score = scale_table.get(str(raw))
    if T_score is not None:
        return T_score
    else:
        return 0

