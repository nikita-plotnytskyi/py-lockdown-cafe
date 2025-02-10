import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
    VaccineError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        try:
            if "vaccine" not in visitor:
                raise NotVaccinatedError
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError
            if not visitor["wearing_a_mask"]:
                raise NotWearingMaskError
        except VaccineError:
            raise
        else:
            return f"Welcome to {self.name}"
