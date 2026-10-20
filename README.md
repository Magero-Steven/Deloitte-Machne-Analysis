# Deloitte Machne Analysis

The goal of the Daikibo telemetry analysis is to identify which factory experienced the most machine breakdowns in May 2021 and which machine types broke down most frequently at that factory.

This repository contains a starter project structure with a Jupyter notebook and a small analysis script. Add your raw telemetry file at data/daikibo_telemetry.json and run the notebook or the script.

Quick start

- Install dependencies: `pip install -r requirements.txt`
- Place your telemetry JSON at `data/daikibo_telemetry.json`
- Run the notebook: `jupyter notebook notebooks/Daikibo_Telemetry_Analysis.ipynb`
- Or run the script: `python src/analysis.py data/daikibo_telemetry.json`

---

Data Cleaning, EDA  and Analysis on  python
Use Python to load the JSON telemetry data and inspect its structure, including fields such as factory location, machine type, timestamp, and machine status.
```python
##1. Load and inspect the JSON file
import pandas as pd
import json

with open("daikibo_telemetry.json", "r") as file:
    data = json.load(file)

df = pd.json_normalize(data)

print(df.head())
print(df.columns)
print(df.info())

##2. Identify machine breakdowns
breakdowns = df[df["status"] == "unhealthy"]
--
##3. Find the factory with the most breakdowns
factory_breakdowns = (
    breakdowns.groupby("factory")
    .size()
    .sort_values(ascending=False)
)

print(factory_breakdowns)
--
##4. Identify the machines that broke most often at that factory
top_factory = factory_breakdowns.idxmax()
machine_breakdowns = (
    breakdowns[breakdowns["factory"] == top_factory]
    .groupby("machine")
    .size()
    .sort_values(ascending=False)
)

print("Factory with most breakdowns:", top_factory)
print(machine_breakdowns)
        
```
    
