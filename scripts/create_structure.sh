#!/bin/bash

# Script to set up the project structure for Shash-llm-from-scratch

echo "Setting up the project structure..."

# Create data directories
mkdir -p data/raw
mkdir -p data/processed

# Create config directory
mkdir -p configs

# Create source code directory and placeholder files
mkdir -p src
touch src/tokenizer.py
touch src/model.py
touch src/train.py
touch src/evaluate.py
touch src/utils.py

# Create experiments directory
mkdir -p experiments

# Create notebooks directory
mkdir -p notebooks

echo "Project structure set up successfully!"
