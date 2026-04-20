from django.test import TestCase
from django.urls import resolve, reverse
from unittest.mock import patch
from datetime import datetime

from human_ast_app.views import (
    get_random_prediction,
    get_daily_prediction,
    home,
    another,
    PREDICTIONS,
)

VALID_ZODIAC_SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces",
]

VALID_COLORS = {"violet", "gold", "crimson", "teal", "ivory", "royalblue"}


# ---------------------------------------------------------------------------
# get_random_prediction()
# ---------------------------------------------------------------------------

class GetRandomPredictionTests(TestCase):

    def test_predictions_dict_has_expected_categories(self):
        self.assertEqual(set(PREDICTIONS.keys()), {"love", "career", "health", "general"})

    def test_valid_category_returns_value_from_pool(self):
        for category in ("love", "career", "health", "general"):
            with self.subTest(category=category):
                result = get_random_prediction(category)
                self.assertIn(result, PREDICTIONS[category])

    def test_none_category_returns_string(self):
        result = get_random_prediction(None)
        all_predictions = [p for pool in PREDICTIONS.values() for p in pool]
        self.assertIn(result, all_predictions)

    def test_empty_string_category_returns_string(self):
        result = get_random_prediction("")
        all_predictions = [p for pool in PREDICTIONS.values() for p in pool]
        self.assertIn(result, all_predictions)

    def test_invalid_category_returns_string(self):
        result = get_random_prediction("invalid_category")
        all_predictions = [p for pool in PREDICTIONS.values() for p in pool]
        self.assertIn(result, all_predictions)

    def test_return_type_is_str(self):
        self.assertIsInstance(get_random_prediction("love"), str)

    def test_mocked_random_choice_returns_exact_value(self):
        expected = PREDICTIONS["love"][0]
        with patch("human_ast_app.views.random.choice", return_value=expected):
            result = get_random_prediction("love")
        self.assertEqual(result, expected)


# ---------------------------------------------------------------------------
# get_daily_prediction()
# ---------------------------------------------------------------------------

class GetDailyPredictionStructureTests(TestCase):

    def setUp(self):
        self.prediction = get_daily_prediction()

    def test_returns_dict(self):
        self.assertIsInstance(self.prediction, dict)

    def test_has_all_required_keys(self):
        expected_keys = {"sign", "date", "love", "career", "health", "overall", "lucky_number", "lucky_color"}
        self.assertEqual(set(self.prediction.keys()), expected_keys)

    def test_sign_is_valid_zodiac(self):
        self.assertIn(self.prediction["sign"], VALID_ZODIAC_SIGNS)

    def test_date_matches_today(self):
        expected = datetime.today().strftime("%B %d, %Y")
        self.assertEqual(self.prediction["date"], expected)

    def test_love_is_from_pool(self):
        self.assertIn(self.prediction["love"], PREDICTIONS["love"])

    def test_career_is_from_pool(self):
        self.assertIn(self.prediction["career"], PREDICTIONS["career"])

    def test_health_is_from_pool(self):
        self.assertIn(self.prediction["health"], PREDICTIONS["health"])

    def test_overall_is_from_pool(self):
        self.assertIn(self.prediction["overall"], PREDICTIONS["general"])

    def test_lucky_number_is_int(self):
        self.assertIsInstance(self.prediction["lucky_number"], int)

    def test_lucky_number_in_range(self):
        for _ in range(20):
            p = get_daily_prediction()
            self.assertGreaterEqual(p["lucky_number"], 1)
            self.assertLessEqual(p["lucky_number"], 99)

    def test_lucky_color_is_lowercase(self):
        for _ in range(10):
            p = get_daily_prediction()
            self.assertEqual(p["lucky_color"], p["lucky_color"].lower())

    def test_lucky_color_is_valid(self):
        for _ in range(10):
            p = get_daily_prediction()
            self.assertIn(p["lucky_color"], VALID_COLORS)


class GetDailyPredictionZodiacTests(TestCase):

    def test_all_valid_signs_are_accepted(self):
        for sign in VALID_ZODIAC_SIGNS:
            with self.subTest(sign=sign):
                result = get_daily_prediction(sign)
                self.assertEqual(result["sign"], sign)

    def test_invalid_sign_falls_back_to_random(self):
        result = get_daily_prediction("Ophiuchus")
        self.assertIn(result["sign"], VALID_ZODIAC_SIGNS)

    def test_none_sign_falls_back_to_random(self):
        result = get_daily_prediction(None)
        self.assertIn(result["sign"], VALID_ZODIAC_SIGNS)

    def test_empty_string_sign_falls_back_to_random(self):
        result = get_daily_prediction("")
        self.assertIn(result["sign"], VALID_ZODIAC_SIGNS)


# ---------------------------------------------------------------------------
# URL resolution
# ---------------------------------------------------------------------------

class URLResolutionTests(TestCase):

    def test_home_url_resolves_to_home_view(self):
        resolver = resolve("/astology/home/")
        self.assertEqual(resolver.func, home)

    def test_luck_url_resolves_to_another_view(self):
        resolver = resolve("/astology/luck/")
        self.assertEqual(resolver.func, another)

    def test_unknown_path_returns_404(self):
        response = self.client.get("/astology/unknown/")
        self.assertEqual(response.status_code, 404)

    def test_bare_astology_prefix_returns_404(self):
        response = self.client.get("/astology/")
        self.assertEqual(response.status_code, 404)


# ---------------------------------------------------------------------------
# home view
# ---------------------------------------------------------------------------

class HomeViewTests(TestCase):

    def test_returns_200(self):
        response = self.client.get("/astology/home/")
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        response = self.client.get("/astology/home/")
        self.assertTemplateUsed(response, "human_ast_app/home.html")

    def test_does_not_use_wrong_template(self):
        response = self.client.get("/astology/home/")
        self.assertTemplateNotUsed(response, "human_ast_app/navi.html")

    def test_context_contains_prediction(self):
        response = self.client.get("/astology/home/")
        self.assertIn("prediction", response.context)

    def test_prediction_context_has_all_keys(self):
        response = self.client.get("/astology/home/")
        prediction = response.context["prediction"]
        for key in ("sign", "date", "love", "career", "health", "overall", "lucky_number", "lucky_color"):
            with self.subTest(key=key):
                self.assertIn(key, prediction)

    def test_prediction_sign_is_valid(self):
        response = self.client.get("/astology/home/")
        self.assertIn(response.context["prediction"]["sign"], VALID_ZODIAC_SIGNS)

    def test_prediction_lucky_number_in_range(self):
        response = self.client.get("/astology/home/")
        number = response.context["prediction"]["lucky_number"]
        self.assertGreaterEqual(number, 1)
        self.assertLessEqual(number, 99)

    def test_prediction_lucky_color_is_valid(self):
        response = self.client.get("/astology/home/")
        self.assertIn(response.context["prediction"]["lucky_color"], VALID_COLORS)

    def test_post_returns_200(self):
        # Views use render() without method restriction, so POST is accepted
        response = self.client.post("/astology/home/")
        self.assertEqual(response.status_code, 200)

    def test_mocked_prediction_passed_through_unchanged(self):
        mock_prediction = {
            "sign": "Leo", "date": "January 01, 2026",
            "love": "test love", "career": "test career",
            "health": "test health", "overall": "test overall",
            "lucky_number": 7, "lucky_color": "gold",
        }
        with patch("human_ast_app.views.get_daily_prediction", return_value=mock_prediction):
            response = self.client.get("/astology/home/")
        self.assertEqual(response.context["prediction"], mock_prediction)


# ---------------------------------------------------------------------------
# another view  (/astology/luck/)
# ---------------------------------------------------------------------------

class AnotherViewTests(TestCase):

    def test_returns_200(self):
        response = self.client.get("/astology/luck/")
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        response = self.client.get("/astology/luck/")
        self.assertTemplateUsed(response, "human_ast_app/navi.html")

    def test_does_not_use_wrong_template(self):
        response = self.client.get("/astology/luck/")
        self.assertTemplateNotUsed(response, "human_ast_app/home.html")

    def test_no_prediction_in_context(self):
        response = self.client.get("/astology/luck/")
        self.assertNotIn("prediction", response.context)

    def test_post_returns_200(self):
        # Views use render() without method restriction, so POST is accepted
        response = self.client.post("/astology/luck/")
        self.assertEqual(response.status_code, 200)
