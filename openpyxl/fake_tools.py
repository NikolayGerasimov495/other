from faker import Faker
fake = Faker(['ru_RU'])


for _ in range(10):
    print(fake.name())

print()

# for _ in range(10):
#     print(fake.address())

# for _ in range(10):
#     print(fake.text())

# for _ in range(10):
#     print(fake.phone_number())


'''''Locale ru_RU
faker.providers.address
faker.providers.automotive
faker.providers.bank
faker.providers.color
faker.providers.company
faker.providers.credit_card
faker.providers.currency
faker.providers.date_time
faker.providers.internet
faker.providers.job
faker.providers.lorem
faker.providers.person
faker.providers.phone_number
faker.providers.ssn"'''''