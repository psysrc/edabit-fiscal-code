from fiscal_code.gender import Gender
import datetime

def _first_n_chars_in(string: str, num: int, search_chars: str) -> str:
    """Returns the first 'num' characters from 'string' that appear in 'search_chars'."""

    if num <= 0:
        return ""

    if len(search_chars) == 0:
        return ""

    output = ""

    for c in string:
        if c in search_chars:
            output += c

            if len(output) >= num:
                break

    return output

def _first_n_consonants(string: str, num: int) -> str:
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    return _first_n_chars_in(string.upper(), num, consonants)


def _first_n_vowels(string: str, num: int) -> str:
    vowels = "AEIOU"
    return _first_n_chars_in(string.upper(), num, vowels)


def _name_snippet(name: str) -> str:
    snippet_len = 3

    snippet = _first_n_consonants(name, snippet_len)

    snippet += _first_n_vowels(name, snippet_len - len(snippet))

    snippet += "X" * (snippet_len - len(snippet))

    return snippet


def _surname_snippet(person: dict) -> str:
    return _name_snippet(person["surname"])


def _remove_char_at(string: str, index: int) -> str:
    return string[:index] + string[index + 1:]


def _forename_snippet(person: dict) -> str:
    forename = person["forename"]

    output = ""

    first_4_consonants = _first_n_consonants(forename.upper(), 4)

    if len(first_4_consonants) == 4:
        output = _remove_char_at(first_4_consonants, 1)
    else:
        output = _name_snippet(forename)

    return output


def _last_2_digits_from_year(year) -> str:
    return str(year)[-2:].zfill(2)


def _month_code(month) -> str:
    month_codes = {
        1: "A", 2: "B", 3: "C", 4: "D",
        5: "E", 6: "H", 7: "L", 8: "M",
        9: "P", 10: "R", 11: "S", 12: "T"
    }

    return month_codes[month]


def _dob_gender_snippet(day, gender) -> str:
    dob_day = day

    if gender == Gender.female:
        dob_day += 40
    
    return str(dob_day).zfill(2)


def _date_gender_snippet(person: dict) -> str:
    dob = person["dob"]
    gender = person["gender"]

    output = _last_2_digits_from_year(dob.year)

    output += _month_code(dob.month)

    output += _dob_gender_snippet(dob.day, gender)

    return output


def _validate_person(person: dict):
    for i in ["forename", "surname", "gender", "dob"]:
        if i not in person:
            raise ValueError(f"Cannot generate fiscal code (key '{i}' is missing)")
    
    if person["gender"] not in [Gender.male, Gender.female]:
        gender = person["gender"]
        raise NotImplementedError(f"Cannot generate fiscal code (gender '{gender}' not supported)")


def gen_fiscal_code(person: dict) -> str:
    _validate_person(person)

    code = _surname_snippet(person)

    code += _forename_snippet(person)

    code += _date_gender_snippet(person)

    return code
