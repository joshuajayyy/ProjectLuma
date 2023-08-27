import names
import random_address
import randominfo as ri

userLogFilePath = "C:/Users/SLMP - Joshua/PycharmProjects/ProjectLuma/testData/user_log.text"
random_name = names.get_first_name()
fname = ri.get_first_name()
lname = ri.get_last_name()
#email = ri.get_email(ri.Person().set_attr(ri.get_first_name()))
pword = ri.random_password()
phone_number = ri.get_phone_number()

class InputData:

    create_account_data = [
        {"firstname": fname, "lastname": lname, "email": random_name+"@gmail.com", "password": pword,
         "company": "Case Closed Company", "phone": phone_number}
    ]

    selected_product = [
        {"product_name": "Stellar Solar Jacket", "size": "S", "quantity": 3}
    ]

    #{'address1': '37600 Sycamore Street', 'address2': '', 'city': 'Newark', 'state': 'CA', 'postalCode': '94560', 'coordinates': {'lat': 37.5261943, 'lng': -122.0304698}}
    random_name_address = [random_address.real_random_address()]

    states = [{
            'AK': 'Alaska',
            'AL': 'Alabama',
            'AR': 'Arkansas',
            'AS': 'American Samoa',
            'AZ': 'Arizona',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DC': 'District of Columbia',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'GU': 'Guam',
            'HI': 'Hawaii',
            'IA': 'Iowa',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'MA': 'Massachusetts',
            'MD': 'Maryland',
            'ME': 'Maine',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MO': 'Missouri',
            'MP': 'Northern Mariana Islands',
            'MS': 'Mississippi',
            'MT': 'Montana',
            'NA': 'National',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'NE': 'Nebraska',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NV': 'Nevada',
            'NY': 'New York',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'PR': 'Puerto Rico',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VA': 'Virginia',
            'VI': 'Virgin Islands',
            'VT': 'Vermont',
            'WA': 'Washington',
            'WI': 'Wisconsin',
            'WV': 'West Virginia',
            'WY': 'Wyoming'
    }]

    def logData(self):
        with open(userLogFilePath, 'w') as writer:
            writer.write(fname + "\n")
            writer.write(lname + "\n")
            writer.write(random_name+"@gmail.com" + "\n")
            writer.write(pword + "\n")
            writer.write(phone_number + "\n")

    def getUserFirstName(self):
        with open(userLogFilePath, 'r') as reader:
            return reader.readline().strip()

    def getUserLastName(self):
        with open(userLogFilePath, 'r') as reader:
            reader.readline()
            return reader.readline().strip()

    def getUserEmail(self):
        with open(userLogFilePath, 'r') as reader:
            reader.readline()
            reader.readline()
            return reader.readline().strip()

    def getUserPassword(self):
        with open(userLogFilePath, 'r') as reader:
            reader.readline()
            reader.readline()
            reader.readline()
            return reader.readline().strip()

    def getUserPhoneNumber(self):
        with open(userLogFilePath, 'r') as reader:
            reader.readline()
            reader.readline()
            reader.readline()
            reader.readline()
            return reader.readline().strip()


