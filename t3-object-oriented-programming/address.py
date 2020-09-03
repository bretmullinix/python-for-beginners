class Address:
    def __init__(self, p_street, p_city, p_state, p_zip):

        self.street = p_street
        self.city = p_city
        self.state = p_state
        self.zip = p_zip

    def __str__(self):
        result = "\t" + self.street + "\n"
        result += "\t" + self.city + "\n"
        result += "\t" + self.state + " " + self.zip
        return result
