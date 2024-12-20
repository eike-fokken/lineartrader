from copy import deepcopy

items: list[str] = [
    "Rentier",
    "Schneemann",
    "Tannenbaum",
    "Weihnachtsmütze",
    "Geschenk",
    "Lebkuchen",
]


default_stock: dict[str, int] = {item: 0 for item in items}
stock = deepcopy(default_stock)
stock["Schneemann"] = 14
stock["Weihnachtsmütze"] = 21
stock["Tannenbaum"] = 10

trades: dict[str, dict[str, int]] = {}

pascalines_trade = deepcopy(default_stock)
pascalines_trade["Rentier"] = 1
pascalines_trade["Schneemann"] = -2
pascalines_trade["Tannenbaum"] = -1
pascalines_trade["Geschenk"] = -1
trades["Pascaline"] = pascalines_trade


isidors_trade = deepcopy(default_stock)
isidors_trade["Rentier"] = 2
isidors_trade["Schneemann"] = -2
isidors_trade["Weihnachtsmütze"] = -6
isidors_trade["Lebkuchen"] = -3
trades["Isidor"] = isidors_trade

elsbeths_trade = deepcopy(default_stock)
elsbeths_trade["Tannenbaum"] = -5
elsbeths_trade["Lebkuchen"] = 3
trades["Elsbeth"] = elsbeths_trade


weihnachtsmanns_trade = deepcopy(default_stock)
weihnachtsmanns_trade["Geschenk"] = 1
weihnachtsmanns_trade["Weihnachtsmütze"] = -3
trades["Weihnachtsmann"] = weihnachtsmanns_trade
