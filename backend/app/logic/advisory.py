from typing import Dict, Optional

def spraying_guard(weather_data: Dict) -> Optional[Dict]:
    """
    Rule: Advise against spraying if rain probability is high in the next 24 hours.
    """
    if 'hourly' not in weather_data or not weather_data['hourly']:
        return None

    try:
        rain_next24 = max([x.get("pop", 0) for x in weather_data["hourly"][:24]])
    except (TypeError, KeyError):
        return None # Handle malformed data

    if rain_next24 > 0.6:
        return {
            "type": "spray_guard",
            "severity": "high",
            "text": "मौसम में अगले 24 घंटों में बारिश की अधिक संभावना है। कीटनाशक छिड़काव से बचें और बारिश के बाद ही छिड़काव करें।",
            "reason": f"Rain probability is >60% ({rain_next24*100:.0f}%) in the next 24h, triggering the spray-avoidance rule.",
            "source": "Weather+rules"
        }
    return None

# Placeholder for other rules
def heat_irrigation_alert(weather_data: Dict) -> Optional[Dict]:
    # TODO: Implement this rule
    return None

def sowing_window_alert(weather_data: Dict) -> Optional[Dict]:
    # TODO: Implement this rule
    return None