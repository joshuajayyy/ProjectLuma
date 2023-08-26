import names

userLogFilePath = "C:/Users/SLMP - Joshua/PycharmProjects/ProjectLuma/testData/user_log.text"
random_name = names.get_first_name()


class InputData:

    create_account_data = [
        {"firstname": "Conan", "lastname": "Edogawa", "email": random_name+"@gmail.com", "password": "p@ssw0rd2023!!!"}
    ]

    selected_product = [
        {"product_name": "Stellar Solar Jacket", "size": "S", "quantity": 3}
    ]

    def logData(self):
        with open(userLogFilePath, 'w') as writer:
            writer.write(random_name+"@gmail.com")

    def getUserEmail(self):
        file = open(userLogFilePath)
        return file.readline()
