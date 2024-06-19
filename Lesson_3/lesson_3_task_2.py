from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "Iphone 14", "+79101448989"))
catalog.append(Smartphone("Nokia", "3310", "+79101234567"))
catalog.append(Smartphone("Apple", "Iphone 12 Pro Max", "+79101449090"))
catalog.append(Smartphone("Siemens", "A65", "+79101509898"))
catalog.append(Smartphone("Sony Ericsson", "K750i", "+79201668080"))

for phone in catalog:
    print(f"{phone.brand} {phone.model}, {phone.number}")
