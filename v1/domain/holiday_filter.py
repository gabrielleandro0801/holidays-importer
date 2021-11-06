from v1.domain.holiday import Holiday, CATEGORIES

HOLIDAYS: dict = {
    'TO_INCLUDE': 'carnaval',
    'TO_IGNORE': 'antecipação'
}


class HolidayFilter:
    def __init__(self):
        pass

    def check_type(self, holiday: Holiday) -> Holiday or False:
        holiday_name: str = holiday.name.lower()

        if holiday.is_category(CATEGORIES["NACIONAL"]) or holiday.is_category(CATEGORIES["MUNICIPAL"]):
            return holiday if holiday_name.find(HOLIDAYS['TO_IGNORE']) == -1 else False

        return holiday if holiday_name.find(HOLIDAYS["TO_INCLUDE"]) == 0 else False
