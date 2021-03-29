"""
Tests for the wikimedia and places API response treatment
"""
import app.constants as C_
from app.wikimedia import (get_wikimedia_page_title as get_title,
                           get_wikimedia_page_summary as get_summary,
                           get_wikimedia_coordinates as get_coordinates)
import app.wikimedia as wikimedia

# Tests regarding the retrieval of the TITLE of the wikipedia page:


def mock_title_OK(arg):
    return C_.TITLE_API_OK


def mock_title_FAIL(arg):
    return C_.TITLE_API_NOT_FOUND


def test_get_wikimedia_page_title_OK(monkeypatch):
    monkeypatch.setattr(wikimedia, "get_json_title", mock_title_OK)
    resultOK = get_title("tour"+"%20"+"Eiffel")
    assert resultOK == "Tour Eiffel"


def test_get_wikimedia_page_title_FAIL(monkeypatch):
    """
    Test the wikipedia title page retrieving with INcorrect input
    """
    monkeypatch.setattr(wikimedia, "get_json_title", mock_title_FAIL)
    resultFAIL = get_title("onfzubteundu")
    assert resultFAIL == "no title found"

# Tests regarding the retrieval of the SUMMARY of the wikipedia page:


def mock_summary_OK(arg):
    return C_.SUMMARY_API_OK


def mock_summary_OK_2(arg):
    return C_.SUMMARY_API_OK_2


def mock_summary_FAIL(arg):
    return C_.ANSWER_NO_LOCATION_FOUND


def mock_summary_AMBIGUOUS(arg):
    return C_.SUMMARY_API_AMBIGUOUS


def test_get_wikimedia_page_summary_OK(monkeypatch):
    """
    Test the wikipedia page summary retrieving with correct input
    """
    monkeypatch.setattr(wikimedia, "get_json_summary", mock_summary_OK_2)
    resultOK = get_summary("tour"+"%20"+"Eiffel")
    assert resultOK == C_.SUMMARY_API_OK


def test_get_wikimedia_page_summary_FAIL(monkeypatch):
    """
    Test the wikipedia page summary retrieving with INcorrect input
    """
    monkeypatch.setattr(wikimedia, "get_json_summary", mock_summary_FAIL)
    resultFAIL = get_summary("onfzubteundu")
    assert resultFAIL == C_.ANSWER_NO_LOCATION_FOUND


def test_get_wikimedia_page_summary_AMBIGUOUS(monkeypatch):
    """
    Test the wikipedia page summary retrieving with ambiguous input
    """
    monkeypatch.setattr(wikimedia, "get_json_summary", mock_summary_AMBIGUOUS)
    resultAMBIGUOUS = get_summary("Invalides")
    assert resultAMBIGUOUS == C_.ANSWER_AMBIGUITY


def mock_coordinates_OK(arg):
    return C_.COORDINATES_API_OK


def test_get_wikimedia_coordinates_OK(monkeypatch):
    """
    Test the wikipedia page coordinates retrieving with correct input
    """
    monkeypatch.setattr(wikimedia, "get_json_coordinates", mock_coordinates_OK)
    resultOK = get_coordinates("tour"+"%20"+"Eiffel")
    assert resultOK == (48.858296, 2.294479)
