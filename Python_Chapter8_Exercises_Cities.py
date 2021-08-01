def describe_city(city, country='ireland'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('dublin')
describe_city('berlin', 'germany')
describe_city('croke park')
