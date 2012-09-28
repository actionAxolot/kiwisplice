# Utility functions to do crap
MONTHS = [
    "ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO",
    "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"
]


def format_time_span(date):
    month = MONTHS[date.month - 1]
    day = date.day

    if day < 15:
        day = "1RA"
    else:
        day = "2DA"

    return u"%s de %s" % (day, month)
