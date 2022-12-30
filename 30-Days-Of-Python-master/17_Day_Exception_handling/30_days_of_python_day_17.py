names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

nordic_countries = []

def countries():
    
    for country in names:
        if country == "Estonia":
            nordic_countries.append({country: "es"})
        
        elif country == "Russia":
            nordic_countries.append({country: "ru"})

        else:
            nordic_countries.append(country)

    print(nordic_countries)


countries()