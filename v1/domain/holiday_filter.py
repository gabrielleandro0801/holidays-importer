from v1.domain.holiday import Holiday, TYPES

HOLIDAYS = {
    'TO_INCLUDE': 'carnaval',
    'TO_IGNORE': 'antecipação'
}


class HolidayFilter:
    def __init__(self):
        pass

    def check_type(self, holiday: Holiday) -> Holiday or False:
        holiday_name: str = holiday.get_name().lower()

        if holiday.is_type(TYPES["NACIONAL"]) or holiday.is_type(TYPES["MUNICIPAL"]):
            return holiday if holiday_name.find(HOLIDAYS['TO_IGNORE']) == -1 else False

        return holiday if holiday_name.find(HOLIDAYS["TO_INCLUDE"]) == 0 else False
