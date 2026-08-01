readings = [
    {"city": "Lagos", "temperature": " 32.5 ", "wind_speed": "8.2", "condition": "Sunny", "humidity_percent": 78},
    {"city": "Abuja", "temperature": "29.1", "wind_speed": "15.6", "condition": "RAIN", "humidity_percent": 65},
    {"city": "Kano", "temperature": "38.7", "wind_speed": "5.1", "condition": "sunnny", "humidity_percent": 22},
    {"city": "Port Harcourt", "temperature": " 27.3", "wind_speed": "22.4", "condition": "windy", "humidity_percent": 84},
    {"city": "Ibadan", "temperature": "34.2", "wind_speed": "3.8", "condition": "Cloudy ", "humidity_percent": 55},
    {"city": "Enugu", "temperature": "26.8", "wind_speed": "18.9", "condition": "RAIN", "humidity_percent": 71},
    {"city": "Kaduna", "temperature": "39.4 ", "wind_speed": "4.5", "condition": "sunny", "humidity_percent": 18},
    {"city": "Benin City", "temperature": "28.0", "wind_speed": "11.2", "condition": "cloudy", "humidity_percent": 60},
]

weather = {"sunny", "rain", "cloudy", "windy"}

def clean_wind_speed(wind_speed):
    return float(wind_speed.strip())

def clean_temperature(temp_str):
    return float(temp_str.strip())

def normalize_conditions(condition_str):
    return condition_str.strip().lower()

def is_valid_condition(condition):
    return condition.strip().lower() in weather

def summarize_by_condition(readings):
    count = {}
    for r in readings:
        condition = normalize_conditions(r.get("condition"))
        count[condition] = count.get(condition, 0) + 1
    return count

def find_extreme_heat(readings, threshold_temp):
    city = [dic['city'] for dic in readings if clean_temperature(dic['temperature']) > threshold_temp and clean_wind_speed(dic['wind_speed']) < 4.0]
    
    return city    

def most_extreme_city(readings):
    highest_temp = 0
    for i in readings:
        if clean_temperature(i['temperature']) > highest_temp:
            highest_temp = clean_temperature(i['temperature'])
            city_name = i['city'] 
    return city_name           