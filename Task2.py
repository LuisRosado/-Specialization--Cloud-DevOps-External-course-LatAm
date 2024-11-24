'''
DESCRIPTION:
How much Will you spend?
Given a dictionary of items and their costs and an array specifying the items bought, calculate the total cost of the items plus a given tax.
If item exist in the given cost values, the item is ignored.
Output should be rounded to two decimal places.
'''

# La función suma el costo de los artículos comprados que están en el diccionario de costos y luego aplica la tasa de impuesto al total. El resultado se redondea a dos decimales.
def calculate_total_cost(item_costs, items_bought, tax_rate):
    total_cost = 0
    for item in items_bought:
        if item in item_costs:
            total_cost += item_costs[item]
    total_cost_with_tax = total_cost * (1 + tax_rate)
    return round(total_cost_with_tax, 2)

