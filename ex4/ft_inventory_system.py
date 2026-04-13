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
    inventory: set = set(args)
    print(f"Inventory items: {inventory}")
    print(f"Total unique items: {len(inventory)}")
    print(f"Sorted inventory: {sorted(inventory)}")