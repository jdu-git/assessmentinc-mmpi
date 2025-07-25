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

def convert_basic(scale: str, raw_score: int, gender: str) -> int:
    raw_score = str(raw_score)
    table = MALE_BASIC if gender.lower() == "male" else FEMALE_BASIC

    scale_table = table.get(scale)
    if not scale_table:
        raise ValueError(f"Scale {scale} is not in the table range for {gender}")

    T = scale_table.get(raw_score)
    if not T:
        raise ValueError(f"Raw score {raw_score} not found for scale {scale} in basic table for {gender}")

    return T

def convert_supplementary(scale: str, raw_score: int, gender: str) -> int:
    raw_score = str(raw_score)
    table = MALE_SUPPLEMENTARY if gender.lower() == "male" else FEMALE_SUPPLEMENTARY

    scale_table = table.get(scale)
    if not scale_table:
        raise ValueError(f"Scale {scale} is not in the table range for {gender}")

    T = scale_table.get(raw_score)
    if not T:
        raise ValueError(f"Raw score {raw_score} not found for scale {scale} in supplementary table for {gender}")

    return T
