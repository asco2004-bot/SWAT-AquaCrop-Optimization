# SWAT–AquaCrop Optimization Framework

This repository contains the Python scripts and workflows used in the study:

> **Quantile-Based Optimization of Upstream–Downstream Irrigation: A SWAT–AquaCrop Framework for Reducing Farmer Concern Frequency under Hydro-Climatic Variability** (submitted to *Environmental Modelling & Software*).

The framework integrates SWAT hydrological outputs with AquaCrop crop simulations and applies multi-objective optimization in Python to minimize farmer concern frequency.

## Installation

```bash
git clone https://github.com/YourUsername/SWAT-AquaCrop-Optimization.git
cd SWAT-AquaCrop-Optimization
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows
pip install -r requirements.txt
```

## Usage

Run the optimization with sample data:

```bash
python src/run_model.py --input data --output results
```

## Contact

Mahdi Moudi (moudi@cuit.edu.cn)
