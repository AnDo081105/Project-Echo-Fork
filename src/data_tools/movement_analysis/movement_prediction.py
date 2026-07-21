import json
import os
from collections import defaultdict
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

tool_root = Path(__file__).resolve().parent
output_dir = Path(os.getenv("MOVEMENT_ANALYSIS_OUTPUT_DIR", tool_root / "outputs"))
cleaned_data_file = Path(
    os.getenv("MOVEMENTS_CLEANED_FILE", output_dir / "cleaned_animal_movements.json")
)
output_file = Path(
    os.getenv("MOVEMENT_PREDICTION_OUTPUT_FILE", output_dir / "projected_movement.png")
)

with open(cleaned_data_file, 'r') as f:
    cleaned_data = json.load(f)

# Function to predict future movement based on cleaned coordinates
def predict_future_movement(coords, steps=3):
    if len(coords) < 2:
        print("Insufficient data for prediction.")
        return []

    # Use Linear Regression to predict future movement
    model = LinearRegression()

    # Prepare data for regression (treat latitudes as X and longitudes as Y)
    latitudes = np.array([coord[0] for coord in coords]).reshape(-1, 1)
    longitudes = np.array([coord[1] for coord in coords])

    model.fit(latitudes, longitudes)

    # Predict future coordinates
    last_lat = float(latitudes[-1, 0])
    predicted_coords = []
    for i in range(steps):
        predicted_long = model.predict([[last_lat + i]])
        predicted_coords.append([last_lat + i, predicted_long[0]])

    return predicted_coords

coords_by_species = defaultdict(list)
for record in cleaned_data:
    coords = record.get('animalTrueLLA')
    if isinstance(coords, list) and len(coords) == 2:
        coords_by_species[record.get('species', 'unknown')].append(coords)
    else:
        print(f"Invalid coordinate data: {coords}")

for species, cleaned_coords in coords_by_species.items():
    print(f"Species: {species}")
    print(f"Cleaned Coordinates: {cleaned_coords}")

    predicted_coords = predict_future_movement(cleaned_coords, steps=3)
    print(f"Predicted Coordinates: {predicted_coords}")

    lats, lons = zip(*cleaned_coords)
    plt.plot(lons, lats, marker="o", label=f"{species} (Observed)")

    if predicted_coords:
        pred_lats, pred_lons = zip(*predicted_coords)
        plt.plot(pred_lons, pred_lats, marker="x", label=f"{species} (Predicted)")

# Customize plot
plt.title("Projected Animal Movements")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc='upper right')

output_file.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_file)
plt.show()
