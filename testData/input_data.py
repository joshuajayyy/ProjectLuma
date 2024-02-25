import names
import random_address
import randominfo as ri

userLogFilePath = "C:/Users/j.guadalupe/PycharmProjects/PythonTesting/ProjectLuma/testData/user_log.txt"
random_name = names.get_first_name()
f_name = ri.get_first_name()
l_name = ri.get_last_name()
p_word = ri.random_password()
phone_number = ri.get_phone_number()


class InputData:

    create_account_data = [{
        "firstname": f_name,
        "lastname": l_name,
        "email": random_name+"@gmail.com",
        "password": p_word,
        "company": "Case Closed Company",
        "phone": phone_number
    }]

    selected_product = [{
        "product_name": "Stellar Solar Jacket",
        "size": "S",
        "quantity": 3
    }]

    # 'address1': '37600 Sycamore Street', 'address2': '', 'city': 'Newark', 'state': 'CA', 'postalCode': '94560',
    # 'coordinates': {'lat': 37.5261943, 'lng': -122.0304698}}
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
            writer.write(f_name + "\n")
            writer.write(l_name + "\n")
            writer.write(random_name+"@gmail.com" + "\n")
            writer.write(p_word + "\n")
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
