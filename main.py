from fiscal_code.fiscal_code import gen_fiscal_code
from fiscal_code.gender import Gender
from datetime import datetime


def main():
    gino = {
        "forename": "Gino",
        "surname": "D'Acampo",
        "gender": Gender.male,
        "dob": datetime(1976, 7, 17),
    }

    gino_code = gen_fiscal_code(gino)
    
    print("-- Gino --")
    print(gino)
    print(f"Code: {gino_code}\n")


if __name__ == "__main__":
    main()
