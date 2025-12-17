# Image-Authenticity-Checker
### A Simplified Visual Verification Engine (VVE)

## Overview
The Image Authenticity Checker is a lightweight visual verification system that analyzes an image to determine whether it is Likely Original or Suspicious.

The system combines:

- Perceptual hashing (pHash) for visual similarity detection
- EXIF metadata inspection for trust signals
- Rule-based classification for explainable decisions

This project represents a simplified component of a larger Visual Verification Engine (VVE) used for detecting reused, stock, or manipulated images.

## Objectives
- Detect reused or stock images using perceptual hashing
- Identify missing or suspicious metadata
- Produce an explainable authenticity verdict
- Maintain modular, production-ready architecture

## Installation
### Requirements
- Python 3.9+

### Install Dependencies
- pillow 
- imagehash 
- numpy

## Usage
- Place known or reference images inside the reference_images/ directory.
- Place the image to analyze at the project root (or update the path).

## Run the engine:
- python run.py


## How It Works
1. Perceptual Hashing (pHash)
    - Generates a visual fingerprint for each image
    - Robust to resizing, compression, and minor edits
    - Similarity is computed using Hamming distance
    - Output is normalized to a 0–100% similarity score

2. Image Similarity Detection
    - Target image is compared against a directory of reference images
    - High similarity suggests reused or stock imagery

3. EXIF Metadata Extraction
    - The system extracts the following metadata fields when available:
    - Date Taken
    - Device Model
    - Orientation
    - Geolocation (GPS)
    - Modification Date
    - Missing or stripped EXIF data is treated as a risk signal.

4. Decision Logic
    - The final verdict is determined using simple, explainable rules:
        - If max_similarity ≥ 85% OR EXIF metadata is missing: Suspicious Image
        - Else: Likely Original

This logic can be easily extended or replaced with a scoring or ML-based classifier.