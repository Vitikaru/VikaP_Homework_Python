from address import Address
from mailing import Mailing
to_address = Address(628305, 'Нефтеюганск', "11a микрорайон", '45', '19')
from_address = Address(391842, 'Скопин', 'Полевая', '51', '2')
track = "87542378"
cost = 4000
mailing = Mailing(to_address, from_address, cost, track)
print(mailing)
