"""Logic for Celebrations, i.e. Feasts and commemorations of Saints."""

from datetime import date

_PASCHA_LOOKUP_TABLE = {
    "2015": date(2015, 4, 12),
    "2016": date(2016, 5, 1),
    "2017": date(2017, 4, 16),
    "2018": date(2018, 4, 8),
    "2019": date(2019, 4, 28),
    "2020": date(2020, 4, 19),
    "2021": date(2021, 5, 2),
    "2022": date(2022, 4, 24),
    "2023": date(2023, 4, 16),
    "2024": date(2024, 5, 5),
    "2025": date(2025, 4, 20),
}


class DateNotFound(Exception):
    """Represents a date lookup that failed."""


def get_date_of_pascha(datelike):
    """Return the date of Pascha given a datetime.date-like object.

    Raises a DateNotFound exception if it cannot find the date.
    """
    year_string = datelike.strftime("%Y")
    try:
        return _PASCHA_LOOKUP_TABLE[year_string]
    except KeyError as key_error:
        msg = f"Could not find the date of Pascha for {year_string}."
        raise DateNotFound(msg) from key_error
