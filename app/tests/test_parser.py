"""
Tests regarding the parsing of user input
"""
from app.inputParser import parse
from app.constants import (test_se_trouve as SETROUVE,
                           test_adresse_de as ADRESSE,
                           test_se_situent as SESITUENT,
                           test_situées as SITUEES)


def test_parse_se_trouve():
    """
    Test that parser recognizes "se trouve"
    """
    result = parse(SETROUVE)
    assert result == ("%20musée""%20""d'art""%20""et""%20"
                      "d'histoire""%20""de""%20""Fribourg")


def test_parse_adresse_de():
    """
    Test that parser recognizes "adresse de"
    """
    result = parse(ADRESSE)
    assert result == ("%20tour""%20""eiffel")


def test_parse_se_situent():
    """
    Test that parser recognizes "se situent"
    """
    result = parse(SESITUENT)
    assert result == "%20Invalides"


def test_parse_situées():
    """
    Test that parser recognizes "situées"
    """
    result = parse(SITUEES)
    assert result == ("%20""chutes""%20""du%20Niagara")
