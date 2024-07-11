import os
import json
import pandas as pd

# Function to extract data from Fit JSON files
def extract_fit_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Extracting relevant information
    fitness_activity = data['fitnessActivity']
    start_time = data['startTime']
    end_time = data['endTime']
    duration = data['duration']

    return {
        'Fitness Activity': fitness_activity,
        'Start Time': start_time,
        'End Time': end_time,
        'Duration': duration
    }

