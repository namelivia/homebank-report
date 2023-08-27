from datetime import date, timedelta

def convert_date_from_homebank_format(homebank_date):
    dt = date(1, 1, 1)
    dt += timedelta(days=homebank_date)
    return dt

def convert_date_to_homebank_format(dt):
    return (dt - date(1, 1, 1)).days
