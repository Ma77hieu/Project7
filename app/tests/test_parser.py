"""
Tests regarding the parsing of user input
"""
from app.inputParser import parse_exple
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
    assert result == " le musée d'art et d'histoire de Fribourg"


def test_parse_adresse_de():
    """
    Test that parser recognizes "adresse de"
    """
    result = parse(ADRESSE)
    assert result == " la tour eiffel"


def test_parse_se_situent():
    """
    Test that parser recognizes "se situent"
    """
    result = parse(SESITUENT)
    assert result == " les Invalides"


def test_parse_situées():
    """
    Test that parser recognizes "situées"
    """
    result = parse(SITUEES)
    assert result == " les chutes du Niagara"
