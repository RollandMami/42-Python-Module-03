# ************************************************************************** #
#                                                                            #
#                                                       :::      ::::::::    #
#    ft_inventory_system.py                            :+:      :+:    :+:   #
#                                                   +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari  +#+  +:+       +#+         #
#                                               +#+#+#+#+#+   +#+            #
#    Created: 2026/04/08 18:05:18 by mamiandr        #+#    #+#              #
#    Updated: 2026/04/11 21:40:24 by mamiandr       ###   ########.fr        #
#                                                                            #
# ************************************************************************** #

import sys


class InventoryError(Exception):
    def __init__(self, message):
        super().__init__(message)


class SplitError(InventoryError):
    pass


class DuplicateError(InventoryError):
    pass


def ft_inventory_system(args: list) -> None:
    inventory: dict = {}
    print("=== Inventory System ===")
    for i in range(1, len(args)):
        try:
            elm = args[i].split(":")
            if (len(elm) <= 1 or len(elm) > 2):
                raise SplitError("Error - invalid parameter")
            key, value = elm[0], elm[1]
            if key in inventory:
                raise DuplicateError("Redundant item")
            v: int = int(value)
            inventory[key] = v
        except DuplicateError as e:
            print(f"{e} '{key}' - discarding")
        except SplitError as e:
            print(f"{e} '{args[i]}'")
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
        i += 1
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)} items:\
{sum(inventory.values())}")
    if (len(inventory) > 0):
        total: int = sum(inventory.values())
        maximum: int = max(inventory.values())
        minimum: int = min(inventory.values())
        found_it: int = 0
        for k, v in inventory.items():
            print(f"Item {k} represents {round((v / total)*100, 1)}%")
        for k in inventory:
            if (inventory[k] == maximum):
                if (not found_it):
                    print(f"Item most abundant: {k} with quantity {maximum}")
                    found_it = 1
        found_it = 0
        for k in inventory:
            if (inventory[k] == minimum):
                if (not found_it):
                    print(f"Item least abundant: {k} with quantity {minimum}")
                    found_it = 1
    inventory.update({"magic_item" : 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    ft_inventory_system(sys.argv)
