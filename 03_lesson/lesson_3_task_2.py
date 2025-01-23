from smartphone import Smartphone

catalog = [
    Smartphone("TECNO", "SPARK 20", "+79634926226"),
    Smartphone("Xiaomi", "Redmi 12C", "+79825998079"),
    Smartphone("iPhone", "16 Pro Max", "+79847576777"),
    Smartphone("Samsung", "Galaxy A06", "+79833583257"),
    Smartphone("Nokia", "G22", "+79858255454")
]

for smartphone in catalog:
    print(f"{smartphone.brend} - {smartphone.model}. {smartphone.sub_number}")
