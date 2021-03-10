"""
Tests for the wikimedia API response treatment
"""
import app.constants as C_
from app.wikimedia import get_wikimedia_page_title as get_title
from app.wikimedia import get_wikimedia_page_summary as get_summary
from app.wikimedia import get_wikimedia_coordinates as get_coordinates


# def test_get_wikimedia_page_title_OK(mocker):
#     mocker.patch('app.wikimedia.get_wikimedia_page_title.requests.get',
#                  return_value=C_.TITLE_API_OK)
#     resultOK = get_title("tour"+"%20"+"Eiffel")
#     assert resultOK == "Tour Eiffel"

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
