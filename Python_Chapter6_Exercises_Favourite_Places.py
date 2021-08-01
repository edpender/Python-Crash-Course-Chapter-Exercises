favorite_places = {
    'eric': ['wild atlantic way', 'the alps', 'canary islands'],
    'erin': ['hawaii', 'iceland'],
    'james': ['mt. everest', 'the beach', 'paris']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())
