# Travel and Exercise Calculator

This is a simple Python application that calculates total travel distance, exercise time, and calories burned based on user settings.

## Settings

- Age
- Gender
- Height
- Weight
- Transport (walking, running, cycling)
- Destinations (name, distance, time)

## Usage

To run the application, simply execute the `main.py` file. The results will be displayed in the console.

## Example

```python
# Example settings
settings = {
    "age": 25,
    "gender": "male",
    "height": 175,
    "weight": 70,
    "transport": "walking",
    "destinations": [
        {"name": "university", "distance": 5, "time": 60},
        {"name": "part-time job", "distance": 7, "time": 30},
        {"name": "gym", "distance": 3, "time": 20}
    ]
}

# Calculate results
results = calculate(settings)
for key, value in results.items():
    print(f"{key}: {value}")
