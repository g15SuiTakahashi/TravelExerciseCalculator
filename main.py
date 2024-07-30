# 設定情報
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

def calculate(settings):
    total_distance = sum(d['distance'] for d in settings["destinations"])
    total_time = sum(d['time'] for d in settings["destinations"])
    
    # 簡単な消費カロリー計算 (仮の計算式)
    calories_per_km = {"walking": 50, "running": 80, "cycling": 30}
    calories_burned = total_distance * calories_per_km.get(settings["transport"], 50)
    
    result = {
        "Total Distance (km)": total_distance,
        "Total Time (min)": total_time,
        "Calories Burned (kcal)": calories_burned
    }
    
    return result

# 計算結果を表示
results = calculate(settings)
for key, value in results.items():
    print(f"{key}: {value}")
