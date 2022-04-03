from fiscal_code.fiscal_code import gen_fiscal_code
from fiscal_code.gender import Gender
from datetime import datetime, MINYEAR
import pytest


def test_basic1():
    generated_code = gen_fiscal_code({
        "forename": "Matt",
        "surname": "Edabit",
        "gender": Gender.male,
        "dob": datetime(1900, 1, 1),
    })

    expected_code = "DBTMTT00A01"

    assert generated_code == expected_code


def test_basic2():
    generated_code = gen_fiscal_code({
        "forename": "Helen",
        "surname": "Yu",
        "gender": Gender.female,
        "dob": datetime(1950, 12, 1),
    })

    expected_code = "YUXHLN50T41"

    assert generated_code == expected_code


def test_basic3():
    generated_code = gen_fiscal_code({
        "forename": "Mickey",
        "surname": "Mouse",
        "gender": Gender.male,
        "dob": datetime(1928, 1, 16),
    })

    expected_code = "MSOMKY28A16"

    assert generated_code == expected_code


def test_a_girl_is_nobody():
    generated_code = gen_fiscal_code({
        "forename": "",
        "surname": "",
        "gender": Gender.female,
        "dob": datetime(MINYEAR, 1, 1),
    })

    expected_code = "XXXXXX01A41"

    assert generated_code == expected_code


def test_a_boy_is_nobody():
    generated_code = gen_fiscal_code({
        "forename": "",
        "surname": "",
        "gender": Gender.male,
        "dob": datetime(MINYEAR, 1, 1),
    })

    expected_code = "XXXXXX01A01"

    assert generated_code == expected_code


def test_error_missing_dob():
    with pytest.raises(ValueError):
        gen_fiscal_code({
            "forename": "Mickey",
            "surname": "Mouse",
            "gender": Gender.male,
        })


def test_error_missing_gender():
    with pytest.raises(ValueError):
        gen_fiscal_code({
            "forename": "Mickey",
            "surname": "Mouse",
            "dob": datetime(1928, 1, 16),
        })


def test_error_missing_surname():
    with pytest.raises(ValueError):
        gen_fiscal_code({
            "forename": "Mickey",
            "gender": Gender.male,
            "dob": datetime(1928, 1, 16),
        })


def test_error_missing_forename():
    with pytest.raises(ValueError):
        gen_fiscal_code({
            "surname": "Mouse",
            "gender": Gender.male,
            "dob": datetime(1928, 1, 16),
        })


def test_error_unsupported_gender():
    with pytest.raises(NotImplementedError):
        gen_fiscal_code({
            "forename": "Mickey",
            "surname": "Mouse",
            "gender": Gender.other,
            "dob": datetime(1928, 1, 16),
        })
