from django.shortcuts import render

# Create your views here.
import random
from datetime import datetime

PREDICTIONS = {
    "love": [
        "A meaningful connection is closer than you think — stay open to surprises.",
        "The stars favor honest conversations in your relationships this week.",
        "Venus aligns in your favor; don't be afraid to express your true feelings.",
        "A past connection may resurface — trust your intuition on how to proceed.",
    ],
    "career": [
        "Mercury's position signals a breakthrough idea is on its way to you.",
        "Your hard work is about to be noticed — stay consistent and patient.",
        "A new opportunity may arrive unexpectedly; keep your options open.",
        "Avoid major financial decisions until the new moon passes.",
    ],
    "health": [
        "The cosmos urge you to slow down and listen to your body today.",
        "A burst of energy is coming your way — channel it into movement.",
        "Rest is your superpower right now; don't underestimate sleep's magic.",
        "Mind and body are in harmony — a great week for new wellness habits.",
    ],
    "general": [
        "The universe is aligning things quietly in your favor. Trust the process.",
        "Change is approaching — embrace it rather than resist.",
        "Your intuition is unusually sharp today. Act on it.",
        "A small, overlooked detail will turn out to be very important.",
    ],
}

def get_random_prediction(category: str = None) -> str:
    """
    Returns a random astrology prediction string.
    
    Args:
        category: Optional. One of 'love', 'career', 'health', 'general'.
                  If None or invalid, picks a random category.
    
    Returns:
        A prediction string.
    """
    if category not in PREDICTIONS:
        category = random.choice(list(PREDICTIONS.keys()))
    
    prediction = random.choice(PREDICTIONS[category])
    return prediction


def get_daily_prediction(zodiac_sign: str = None) -> dict:
    """
    Returns a full daily prediction payload.
    Useful if your frontend wants richer data.
    """
    zodiac_signs = [
        "Aries", "Taurus", "Gemini", "Cancer",
        "Leo", "Virgo", "Libra", "Scorpio",
        "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]
    
    if zodiac_sign not in zodiac_signs:
        zodiac_sign = random.choice(zodiac_signs)
    
    return {
        "sign": zodiac_sign,
        "date": datetime.today().strftime("%B %d, %Y"),
        "love": get_random_prediction("love"),
        "career": get_random_prediction("career"),
        "health": get_random_prediction("health"),
        "overall": get_random_prediction("general"),
        "lucky_number": random.randint(1, 99),
        "lucky_color": random.choice(["Violet", "Gold", "Crimson", "Teal", "Ivory", "RoyalBlue"]).lower(),
    }


def home(request):
    prediction = get_daily_prediction()
    return render(request, "human_ast_app/home.html", {"prediction": prediction})

def another(request):
    return render(request, "human_ast_app/navi.html")


