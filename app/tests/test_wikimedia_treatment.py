"""
Tests for the wikimedia API response treatment
"""
import urllib.request
import requests
import json
from io import BytesIO
import app.constants as C_
from app.wikimedia import get_wikimedia_page_title as get_title
from app.wikimedia import get_wikimedia_page_summary as get_summary
from app.wikimedia import get_wikimedia_coordinates as get_coordinates


def mockreturn_requestsGet(arg):
    print("resultmock {}:".format(json.dumps(
        C_.REQUESTS_MODEL_RESPONSE).encode('utf-8')))
    return json.dumps(C_.REQUESTS_MODEL_RESPONSE).encode('utf-8')


# def mockreturn_jsonLoads(arg):
#     return C_.TITLE_API_OK


def test_mock_get_wikimedia_page_title_OK(monkeypatch):
    monkeypatch.setattr(requests, 'get', mockreturn_requestsGet)
    # monkeypatch.setattr(json, 'loads', mockreturn_jsonLoads)
    resultOK = get_title("tour"+"%20"+"Eiffel")
    assert resultOK == "Tour Eiffel"


def test_get_wikimedia_page_title_OK():
    """
    Test the wikipedia title page retrieving with correct input
    """
    resultOK = get_title("tour"+"%20"+"Eiffel")
    assert resultOK == "Tour Eiffel"


def test_get_wikimedia_page_title_FAIL():
    """
    Test the wikipedia title page retrieving with INcorrect input
    """
    resultFAIL = get_title("onfzubteundu")
    assert resultFAIL == "no title found"


def test_get_wikimedia_page_summary_OK():
    """
    Test the wikipedia page summary retrieving with correct input
    """
    resultOK = get_summary("tour"+"%20"+"Eiffel")
    assert resultOK == C_.SUMMARY_API_OK


def test_get_wikimedia_page_summary_FAIL():
    """
    Test the wikipedia page summary retrieving with INcorrect input
    """
    resultFAIL = get_summary("onfzubteundu")
    assert resultFAIL == C_.ANSWER_NO_LOCATION_FOUND


def test_get_wikimedia_page_summary_AMBIGUOUS():
    """
    Test the wikipedia page summary retrieving with ambiguous input
    """
    resultAMBIGUOUS = get_summary("Invalides")
    assert resultAMBIGUOUS == C_.ANSWER_AMBIGUITY


def test_get_wikimedia_coordinates_OK():
    """
    Test the wikipedia page coordinates retrieving with correct input
    """
    resultOK = get_coordinates("tour"+"%20"+"Eiffel")
    assert resultOK == (48.858296, 2.294479)
