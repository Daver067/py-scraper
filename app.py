import requests
import re

def main():
    if True:
        read_file('website_list.csv')
        return
    URL = "https://www.cleanusa.com"
    page = requests.get(URL, timeout=5)
    if page.status_code != 200:
        print('page inaccessible')
        return 0
    #get_phone_numbers(page)
    #get_email_address(page)
    return 0

def read_file(filename):
    with open(filename, 'r') as readFile, open(filename.replace('.csv', '_new.csv'), 'w') as writeFile:
        for line in readFile:
            line = line.replace("\n", "")
            parts = line.split(";")
            if parts[0] == "Website": # Need to figure out the header to actually use here
                writeFile.write(";".join(parts) + '\n')
                continue
            page = requests.get(parts[0], timeout=5)

            # If theres an error reaching to page
            if page.status_code != 200:
                parts[1] = ('page inaccessible')
                parts[2] = ('page inaccessible')
                parts[3] = ('page inaccessible')
                writeFile.write(";".join(parts) + "\n")
                continue

            # Update the email part of th csv
            for email_address in get_email_address(page):
                parts[1] += str(email_address) + ","

            # Update the phone number section of the csv
            for index, phone_num in enumerate(get_phone_numbers(page)):
                if index == 0:
                    parts[2] += str(phone_num)
                else:
                    parts[2] += "," + str(phone_num)
            writeFile.write(";".join(parts) + "\n")



def get_phone_numbers(page):
    phone_regex = r"(?:\+?\d{1}\s?)?[(]?\d{3}[)]?[(\s)?.-]\d{3}[\s.-]\d{4}"
    numbers = re.findall(phone_regex, page.text)
    if len(numbers) == 0 or len(numbers) > 10:
        return ['no numbers found']
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
            return ['no emails found']
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
        return sorted_emails
main()