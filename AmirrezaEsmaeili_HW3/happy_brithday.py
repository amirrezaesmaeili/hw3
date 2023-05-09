from datetime import datetime
from jdatetime import date as jdate
from jdatetime import timedelta as jtimedelta


def calculate_remaining_time(birthday: datetime) -> tuple[int, int]:
    """
    Calculate the number of remaining days and minutes until the next birthday.

    Args:
        birthday (datetime): The birthdate.

    Returns:
        tuple[int, int]: A tuple containing the number of remaining days and minutes.
    """
    now = datetime.now()
    today = now.date()
    next_birthday = datetime(today.year, birthday.month,
                             birthday.day, now.hour, now.minute, now.second)

    if today > next_birthday.date():
        next_birthday = datetime(
            today.year + 1, birthday.month, birthday.day, now.hour, now.minute, now.second)

    remaining_time = next_birthday - now
    remaining_days = remaining_time.days
    remaining_minutes = remaining_time.seconds // 60

    return remaining_days, remaining_minutes


def convert_to_jalali(birthday: datetime) -> str:
    """
    Convert the given birthday to Jalali (Shamsi) calendar.

    Args:
        birthday (datetime): The birthdate.

    Returns:
        str: The birthday in Jalali calendar in the format 'YYYY-MM-DD'.
    """
    j_birthday = jdate.fromgregorian(date=birthday)
    j_birthday_str = j_birthday.strftime("%Y-%m-%d")
    return j_birthday_str


birthday_str = input(
    "Please enter your birthdate in the format (YYYY-MM-DD): ")
birthday = datetime.strptime(birthday_str, "%Y-%m-%d").date()

total_seconds = (datetime.now().date() - birthday).total_seconds()

remaining_days, remaining_minutes = calculate_remaining_time(birthday)
j_birthday_str = convert_to_jalali(birthday)

print(f"Total seconds elapsed from your birthdate: {total_seconds}")
print(
    f"Number of days and minutes remaining until your next birthday: {remaining_days} days, {remaining_minutes} minutes")
print(f"Your birthdate in Jalali calendar: {j_birthday_str}")
