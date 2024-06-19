from address import Address
from mailing import Mailing


to_address = Address("238563", "г.Светлогорск", "ул.Приморская", "д.1", "кв.5")
from_address = Address("600029", "г.Владимир",
                       "ул.Смоленская", "д.10", "кв.33")
mailing = Mailing(to_address, from_address, 430, 80513096912500)

print(f"Отправление № {mailing.track} из: {to_address.index} {to_address.city}, {to_address.street}, {to_address.house} - {to_address.apartment} в: {
      from_address.index}, {from_address.city}, {from_address.street}, {from_address.house} - {from_address.apartment}. Стоимость {mailing.cost} рублей.")
