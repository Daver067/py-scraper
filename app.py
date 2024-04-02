import requests
import re

def main():
    URL = "https://www.moveoutcleaningserviceaustin.com"
    page = requests.get(URL, timeout=5)
    get_phone_numbers(page)
    get_email_address(page)
    return 0

def get_phone_numbers(page):
    phone_regex = r"(?:\+?\d{1}\s?)?[(]?\d{3}[)]?[(\s)?.-]\d{3}[\s.-]\d{4}"
    numbers = re.findall(phone_regex, page.text)
    if len(numbers) == 0:
        print('didn\'t find any phone numbers')
        return None
    else:
        sorted_phone_numbers = []
        for phone_number in numbers:
            if phone_number in sorted_phone_numbers or phone_number == "(999) 999-9999":
                continue
            sorted_phone_numbers.append(phone_number)
        for num in sorted_phone_numbers:
            print(num)
        return sorted_phone_numbers


def get_email_address(page):
    regex = r'"mailto:\w{1,50}@\w{1,50}\.[a-z]{2,5}"'
    regex2 = r'\w{1,50}@\w{1,50}\.(?:ca|com)'
    emails = re.findall(regex, page.text, re.IGNORECASE)
    if len(emails) == 0:
        emails = re.findall(regex2, page.text, re.IGNORECASE)
        if len(emails) == 0:
            print('didn\'t find any emails')
            return 0
        sorted_emails = []
        for email in emails:
            if email in sorted_emails:
                continue
            sorted_emails.append(email)
        for email in sorted_emails:
            print(email)
    else:
        sorted_emails = []
        for email in emails:
            index = str(email).find("mailto:")
            email = str(email)[index + 7:]
            index = str(email).find("\'")
            email = str(email)[:index]
            if email in sorted_emails:
                continue
            sorted_emails.append(email)
            
        for email in sorted_emails:
            print(email)
main()