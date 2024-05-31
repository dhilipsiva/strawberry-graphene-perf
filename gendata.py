from faker import Faker
fake = Faker()

def get_data():
    datum = dict(
    name=fake.name(),
    address=fake.address(),
    text=fake.text(),
    hex_color=fake.hex_color(),
    random_int=fake.random_int(),
    random_digit=fake.random_digit(),
    boolean=fake.boolean(),
    items=[fake.address() for _ in range(fake.random_digit())]
    )

data = [get_data() for _ in range(200000)]

with open("data.json", "w") as f:
    import json
    json.dump(data, f)
