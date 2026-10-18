"""
Simple analysis script for Daikibo telemetry.
Usage: python src/analysis.py path/to/daikibo_telemetry.json
"""
import sys
import pandas as pd
import json


def load_data(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return pd.json_normalize(data)


def main(path):
    df = load_data(path)
    print(df.head())
    print(df.columns)
    print(df.info())

    # filter to breakdowns / unhealthy statuses
    breakdowns = df[df['status'] == 'unhealthy']

    # which factory had the most breakdowns
    factory_breakdowns = (
        breakdowns.groupby('factory')
        .size()
        .sort_values(ascending=False)
    )

    print(factory_breakdowns)

    # top factory and machine types that broke down there
    if not factory_breakdowns.empty:
        top_factory = factory_breakdowns.idxmax()

        machine_breakdowns = (
            breakdowns[breakdowns['factory'] == top_factory]
            .groupby('machine')
            .size()
            .sort_values(ascending=False)
        )

        print('Factory with most breakdowns:', top_factory)
        print(machine_breakdowns)
    else:
        print('No breakdowns found in data')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python src/analysis.py path/to/daikibo_telemetry.json')
    else:
        main(sys.argv[1])
