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

def ft_inventory_system(args: list) -> None:
    inventory_keys: list = []
    inventory_values: list = []
    inventory: dict = {}
    print("=== Inventory System ===\n")
    if (len(args) == 1):
        print("No items in inventory.")
        return
    for i in range(1, len(args)):
        try:
            key, value = args[i].split(":")
            inventory_keys.append(key)
            inventory_values.append(int(value))
        except ValueError:
            print(f"Invalid format for item: {args[i]}. Expected format: key:value")
    inventory = dict(zip(inventory_keys, inventory_values))
    print(f"Inventory items: {inventory}")
    print(f"Total unique items: {len(inventory)}")
    print(f"Sorted inventory: {sorted(inventory.keys())}")