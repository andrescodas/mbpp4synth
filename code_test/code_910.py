import datetime
def check_date(m, d, y):
    """
    Write a function to validate a gregorian date.
    """
    try:
        m, d, y = map(int, (m, d, y))
        datetime.date(y, m, d)
        return True
    except ValueError:
        return False
