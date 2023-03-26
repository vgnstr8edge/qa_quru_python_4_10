from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    second_name: str
    email: str
    gender: str
    phone_number: str
    date_of_bd: str
    month_of_bd: str
    year_of_bd: str
    subject: str
    hobbie: str
    photo: str
    street: str
    state: str
    city: str
