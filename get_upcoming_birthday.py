from datetime import datetime, timedelta

def get_upcoming_birthdays(users, days):
    current_date = datetime.now().date()
    target_date = current_date + timedelta(days=days)
    upcoming_birthdays = []

    for user in users:
        try:
            birthday = datetime.strptime(user["birthday"], "%Y-%m-%d").date()
            next_birthday = birthday.replace(year=current_date.year)
            if next_birthday < current_date:
                next_birthday = next_birthday.replace(year=current_date.year + 1)
            if next_birthday == target_date:
                upcoming_birthdays.append(user)
        except ValueError:
            # день народження user 29 лютого 
            if target_date.month == 2 and target_date.day == 29:
                upcoming_birthdays.append(user)
    return upcoming_birthdays