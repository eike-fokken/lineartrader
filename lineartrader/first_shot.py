"""First shot."""

import json
from copy import deepcopy

import casadi

items: list[str] = [
    "Rentier",
    "Schneemann",
    "Tannenbaum",
    "Weihnachtsmütze",
    "Geschenk",
    "Lebkuchen",
]

trade_names: list[str] = [
    "Pascaline",
    "Isidor",
    "Elsbeth",
    "Weihnachtsmann",
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


print(json.dumps(trades, indent=2))

assert sorted(list(trades.keys())) == sorted(trade_names)

trade_numbers: dict[str, casadi.MX] = {
    trade: casadi.MX.sym(trade, 1) for trade in trade_names
}

casadi_variables = casadi.vertcat(*[trade for trade in trade_numbers.values()])

discrete = [True] * len(trade_numbers)

our_constraints = {
    item: sum([trade[item] * trade_numbers[name] for name, trade in trades.items()])
    for item in items
}
casadi_constraints = casadi.vertcat(*list(our_constraints.values()))

constraint_upper_bounds = [1e21] * len(items)
constraint_lower_bounds = [-stock[item] for item in items]


variable_lower_bounds = [0] * len(trades)
variable_upper_bounds = [1e21] * len(trades)

objective = -our_constraints["Rentier"]


problem = {"x": casadi_variables, "g": casadi_constraints, "f": objective}
solver = casadi.qpsol("solver", "highs", problem, {"discrete": discrete})

result = solver(
    x0=[0] * len(trades),
    lbx=variable_lower_bounds,
    ubx=variable_upper_bounds,
    lbg=constraint_lower_bounds,
    ubg=constraint_upper_bounds,
)
objective_value = result["f"]

print(f"\n\nDu kannst höchstens {-objective_value} Rentiere bekommen.")
