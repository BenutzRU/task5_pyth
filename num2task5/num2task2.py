import calendar
import re


def numch(phone_number):

    phone_number_pattern = re.compile(r"^(?:\+7|7|8)\d{10}$")


    if phone_number_pattern.match(phone_number) and len(phone_number) == 11 or len(phone_number) == 12:
        print("Телефон РУ региона.")
    else:
        print("Не РУ.")



phone = input("Enter phone num: ")
numch(phone)




def print_calendar(year, month):

    if not re.match("^\d+$", year) or not re.match("^\d+$", month):
        print("Error")
        return
    year = int(year)
    month = int(month)

    if month < 1 or month > 12:
        print("Error: 1 to 12")
        return

    print(calendar.month(year, month))


year = input("Год: ")
month = input("Месяц: ")
print_calendar(year, month)
