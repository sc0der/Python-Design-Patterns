class Address:
    def __init__(self, street_address, city, country):
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'