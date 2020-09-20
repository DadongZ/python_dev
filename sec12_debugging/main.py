
# linting: allows us to detect some issues with our code as we code.

import requests

response = requests.get('https://randomuser.me/api/?results=10')

data = response.json()

for user in data['results']:
    print(user['name']['first'])

def greet(greeting, name):
    """[Test AutoDocstring]

    Args:
        greeting (str): greeting phrase
        name (str): name

    Returns:
        str: a greeting send to the name
    """
    return f'{greeting} {name}'


print(greet("How are you today", "Alex"))
