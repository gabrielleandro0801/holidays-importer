TYPES = {
    'NACIONAL': 'NACIONAL',
    'MUNICIPAL': 'MUNICIPAL',
    'FACULTATIVO': 'FACULTATIVO'
}


class Holiday:

    def __init__(self, date, name, type):
        self._date = date
        self._name = name
        self._type = type

    def is_type(self, type: str) -> bool:
        return self._type == type

    def get_date(self) -> str:
        return self._date

    def get_name(self) -> str:
        return self._name

    def get_type(self) -> str:
        return self._type

    def to_json(self) -> dict:
        return {
            'date': self._date,
            'name': self._name,
            'type': self._type
        }
