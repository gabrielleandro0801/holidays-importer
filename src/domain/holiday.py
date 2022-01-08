class Holiday:

    def __init__(self, date: str, name: str, category: str):
        self.__date = date
        self.__name = name
        self.__category = category

    def is_category(self, category: str) -> bool:
        return self.__category == category

    @property
    def date(self) -> str:
        return self.__date

    @property
    def name(self) -> str:
        return self.__name

    def to_json(self) -> dict:
        return {
            'date': self.__date,
            'name': self.__name,
            'type': self.__category
        }
