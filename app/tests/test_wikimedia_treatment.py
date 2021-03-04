import app.constants as C_
from app.wikimedia import get_wikimedia_page_title as get_title
from app.wikimedia import get_wikimedia_page_summary as get_summary
from app.wikimedia import get_wikimedia_coordinates as get_coordinates


def test_get_wikimedia_page_title_OK():
    resultOK = get_title("tour"+"%20"+"Eiffel")
    assert resultOK == "Tour Eiffel"


def test_get_wikimedia_page_title_FAIL():
    resultFAIL = get_title("onfzubteundu")
    assert resultFAIL == "no title found"


def test_get_wikimedia_page_summary_OK():
    resultOK = get_summary("tour"+"%20"+"Eiffel")
    assert resultOK == C_.SUMMARY_API_OK


def test_get_wikimedia_page_summary_FAIL():
    resultFAIL = get_summary("onfzubteundu")
    assert resultFAIL == "no title found"


def test_get_wikimedia_page_summary_AMBIGUOUS():
    resultAMBIGUOUS = get_summary("Invalides")
    assert resultAMBIGUOUS == "ambiguity"


def test_get_wikimedia_coordinates_OK():
    resultOK = get_coordinates("tour"+"%20"+"Eiffel")
    assert resultOK == (48.858296, 2.294479)
