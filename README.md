# MMPI-2 Scoring Automation Tool

A desktop application that automates psychological test scoring and graphing for the MMPI-2 assessment.

## Overview

This tool was developed to replace a manual, handwritten scoring process. It's currently in production use at a psychological assessment company in Norman, OK, 
saving hours of staff time weekly.

## Features

- Automated score calculation from raw input
- T-score conversion using standardized norms
- Graph generation for clinical profiles
- Simple GUI for non-technical users

## Tech Stack

- Python
- Matplotlib (graphing)
- Tkinter (GUI)
`
## Installation
```bash
git clone https://github.com/jdu-git/assessmentinc-mmpi.git
cd assessmentinc-mmpi
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python gui.py
```

## CI

![CI](https://github.com/jdu-git/assessmentinc-mmpi/actions/workflows/ci.yml/badge.svg)

Linting runs automatically on every push via GitHub Actions.
