from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

# erweitern um alle Daten die man braucht
class Person(object):
    def __init__(self, email, first_name, last_name, city):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.city = city


    def get_email(self):
        return self.email
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_city(self):
        return self.city


#   in der Schleife werden die Personen Objekte durchlaufen und eine Funktion unserer Klasse Person verwendet
def write_to_file(persons):
    csv_file = open("person_list.csv", "w")
    csv_file.write("First name, Last name, Email, City\n")

    for person in persons:
        csv_file.write("%s,%s,%s,%s\n" % (person.first_name, person.last_name, person.email, person.city))

    csv_file.close()

def main():
    person_list = []

    url = "https://scrapebook22.appspot.com"
    response = urlopen(url).read()
    soup = BeautifulSoup(response)

    for link in soup.findAll("a"):
        if link.string == "See full profile":
            personurl = "https://scrapebook22.appspot.com" + link["href"]
            personhtml = urlopen(personurl).read()
            person_soup = BeautifulSoup(personhtml)

            # erstellen einer Person (derzeit nur mit der Mail adresse)
            email =person_soup.find("span", attrs={"class": "email"}).string
            name = person_soup.find("div", attrs={"class": "col-md-8"}).h1.string
            city = person_soup.find("span", attrs={"data-city": True}).string

            first_name, last_name = name.split(" ")

            person = Person(first_name=first_name, last_name=last_name, email=email, city=city)

            person_list.append(person)

    write_to_file(person_list)


if __name__ == "__main__":
    main()