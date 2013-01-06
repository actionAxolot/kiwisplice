import datetime

# Utility functions to do crap
MONTHS = [
    "ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO",
    "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"
]

MONTHS_DICT = {
    "ENERO": 1,
    "FEBRERO": 2,
    "MARZO": 3,
    "ABRIL": 4,
    "MAYO": 5,
    "JUNIO": 6,
    "JULIO": 7,
    "AGOSTO": 8,
    "SEPTIEMBRE": 9,
    "OCTUBRE": 10,
    "NOVIEMBRE": 11,
    "DICIEMBRE": 12,
}


def format_time_span(date):
    month = MONTHS[date.month - 1]
    day = date.day

    if day < 15:
        day = "1RA"
    else:
        day = "2DA"

    return u"%s de %s" % (day, month)


def get_months_header(*args, **kwargs):
    """
    Generate the necessary monthly headers for the dashboard tables
    """
    today = datetime.date.today()
    months = list()
    for x in xrange(0, 8):
        then = today + datetime.timedelta(days=31 * x)
        months.append(MONTHS[then.month - 1] + " " + str(then.year))

    return months

def get_reverse_months_header(*args, **kwargs):
    """
    Generate the necessary monthly headers for the dashboard tables
    """
    today = datetime.date.today()
    months = list()
    for x in xrange(0, 8):
        then = today - datetime.timedelta(days=31 * x)
        months.append(MONTHS[then.month - 1] + " " + str(then.year))

    return months