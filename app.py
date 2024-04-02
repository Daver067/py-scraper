def main():
    import requests
    from bs4 import BeautifulSoup
    import re
    regex = r'"mailto:\w{1,50}@\w{1,50}\.[a-z]{2,5}"'
    regex2 = r'\w{1,50}@\w{1,50}\.(?:ca|com)'
    URL = "https://rockyridgedental.com"
    page = requests.get(URL, timeout=5)


    phone_regex = r"(?:\+?\d{1}\s?)?[(]?\d{3}[)]?[(\s)?.-]\d{3}[\s.-]\d{4}"
    numbers = re.findall(phone_regex, page.text)
    if len(numbers) == 0:
        print('didn\'t find any phone numbers')
    else:
        sorted_phone_numbers = []
        
        for phone_number in numbers:
            if phone_number in sorted_phone_numbers:
                continue
            sorted_phone_numbers.append(phone_number)
        for num in sorted_phone_numbers:
            print(num)
    #soup = BeautifulSoup(page.content, "html.parser")

    #emails = soup.find_all(href=re.compile('([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(.[A-Z|a-z]{2,})+')) or None
    #if emails == None:
    #    emails = soup.find_all(href=re.compile('mailto:')) or None
    #if emails == None:
    #    print('no emails found')
    #else:
    emails = re.findall(regex, page.text, re.IGNORECASE)
    if len(emails) == 0:
        emails = re.findall(regex2, page.text, re.IGNORECASE)
        if len(emails) == 0:
            print('didn\'t find any')
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