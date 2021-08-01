def city_country(city, country):
    """Return a string like 'Dublin, Ireland'."""
    return(city.title() + ", " + country.title())

city = city_country('dublin', 'ireland')
print(city)

city = city_country('london', 'england')
print(city)

city = city_country('venice', 'italy')
print(city)
