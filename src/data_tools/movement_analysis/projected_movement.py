import json
import os
from pathlib import Path
import matplotlib.pyplot as plt

tool_root = Path(__file__).resolve().parent
repo_root = tool_root.parents[2]
output_dir = Path(os.getenv("MOVEMENT_ANALYSIS_OUTPUT_DIR", tool_root / "outputs"))
movement_file = Path(
    os.getenv(
        "ANIMAL_MOVEMENT_FILE",
        repo_root / "src" / "production" / "MongoDB" / "init" / "movements.json",
    )
)
output_file = Path(
    os.getenv("PROJECTED_MOVEMENT_OUTPUT_FILE", output_dir / "projected_movement.png")
)

with open(movement_file) as f:
    data = json.load(f)

for animal in data:
    if "movement" in animal:
        coords = animal["movement"]
        label = animal.get("name", "unknown")
    elif "animalTrueLLA" in animal:
        coords = [animal["animalTrueLLA"][:2]]
        label = animal.get("species", animal.get("animalId", "unknown"))
    else:
        continue

    x, y = zip(*coords)
    plt.plot(x, y, label=label, marker="o")

plt.title("Projected Animal Movements")
plt.xlabel("X Coordinates")
plt.ylabel("Y Coordinates")
plt.legend()
output_file.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_file)
plt.show()
