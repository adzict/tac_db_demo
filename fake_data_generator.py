from faker import Faker
import random
import csv

fake = Faker()

#testing providers
# test_fake_name = fake.name()
# test_fake_address = fake.address()
# test_fake_company = fake.company()
# test_fake_date_time = fake.date_time()
# test_fake_job = fake.job()

#print(test_fake_name, test_fake_address, test_fake_company, test_fake_date_time, test_fake_job)

#creating a complete fake profile
#test_fake_profile = fake.profile()

#print(test_fake_profile)

#fields needed: first name, last name, sex, mail, phone, city, current_ed_year, birthday, job

#providers list
#fake.first_name(), fake.last_name(), fake.sex(), fake.mail(),fake.phone(), fake.city() ,fake.random_digit_not_null(), fake.birthdate(), fake.job()

#print(fake.first_name(), fake.last_name(), fake.sex(), fake.mail(),fake.phone(), fake.city() ,fake.random_digit_not_null(), fake.birthdate(), fake.job())

# print(fake.first_name())
# print(fake.last_name())
# print(fake.email())
# print(fake.phone_number())
# print(fake.city())
# print(fake.random_digit_not_null())
# print(fake.date_of_birth())
# print(fake.job())

#------------- test_data csv
# Faker.seed(0)

# test_data = fake.csv(header = ('First Name', 'Last Name', 'Sex', 'Email', 'Phone Number', 'City', 'Current Ed Year', 'Date of Birth', 'Job Title'), data_columns = ('{{first_name}}', '{{last_name}}', {{fake.random_choices(elements = ('F', 'M'), length = 1)}}, '{{email}}', '{{phone_number}}', '{{city}}', '{{fake.random_choices(elements = (range(1,6)), length = 1)}}', '{{date_of_birth}}', '{{job}}'), num_rows = 5, include_row_ids = True)

# print(test_data)

# #------------ random digit/letter in range
# test_ed_year = fake.random_choices(elements = (range(1,6)), length = 1)
# test_sex = fake.random_choices(elements = ('F', 'M'), length = 1)
# print(test_ed_year, test_sex)


#--------------------- writting a csv with 5 rows

# Function to generate random sex choices
def generate_sex():
    return random.choice(['F', 'M'])

# Function to generate random education year
def generate_education_year():
    return random.randint(1, 5)

# Generate CSV data
test_data = []

for _ in range(500):  # Generate 5 rows of data
    row = [
        fake.first_name(),
        fake.last_name(),
        generate_sex(),
        fake.email(),
        fake.phone_number(),
        fake.city(),
        generate_education_year(),
        fake.name(),
        fake.date_of_birth(),
        fake.job()
    ]
    test_data.append(row)

# Add header
header = ['First Name', 'Last Name', 'Sex', 'Email', 'Phone Number', 'City', 'Current Ed Year', 'Primary Supervisor', 'Date of Birth', 'Job Title']
test_data.insert(0, header)

# Write data to CSV file
with open('test_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(test_data)

print("CSV data has been generated and saved as 'test_data.csv'.")