class VaccineError(Exception):
    def __str__(self) -> str:
        return "NotVaccinatedError should be raised with a message"


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "NotWearingMaskError should be raised with a message"
