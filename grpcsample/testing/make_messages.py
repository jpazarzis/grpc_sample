"""Creates the tesing messages."""

import json
import faker


faker = faker.Faker()


def make_file(filename='msgs.py', count=50):
    size = 20000
    msgs = [
        {
            'name': faker.text(size),
            'story1': faker.text(size),
            'story2': faker.text(size),
            'story3': faker.text(size)
        }
        for _ in range(count)
    ]
    with open(filename, 'w') as f:
        f.write(f'MSGS = {json.dumps(msgs, indent=4)}')


if __name__ == '__main__':
    make_file()
