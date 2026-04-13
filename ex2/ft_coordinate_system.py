# ************************************************************************** #
#                                                                            #
#                                                       :::      ::::::::    #
#    ft_coordinate_system.py                           :+:      :+:    :+:   #
#                                                   +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari  +#+  +:+       +#+         #
#                                               +#+#+#+#+#+   +#+            #
#    Created: 2026/04/08 18:05:18 by mamiandr        #+#    #+#              #
#    Updated: 2026/04/11 21:40:24 by mamiandr       ###   ########.fr        #
#                                                                            #
# ************************************************************************** #

import math


def get_player_pos() -> tuple:
    while (True):
        try:
            x: float = 0.0
            y: float = 0.0
            z: float = 0.0
            inputs: str = input("Enter new coordinates as floats in format\
'x,y,z': ")
            values: list = inputs.split(",")
            if (len(values) != 3):
                print("Invalid syntax")
                continue
            result: list = []
            for elm in values:
                try:
                    elm = float(elm.strip())
                    result.append(elm)
                except ValueError:
                    print(f"Error on parameter '{elm}': could not \
convert string to float: '{elm}'")
            if (len(result) == 3):
                x, y, z = result
                return x, y, z
        except Exception:
            print("Invalid syntax")
        except KeyboardInterrupt:
            return 0.0, 0.0, 0.0


def ft_coordinate_system() -> None:

    def distance(p1: tuple, p2: tuple) -> float:
        return math.sqrt(
            (p2[0] - p1[0])**2 +
            (p2[1] - p1[1])**2 +
            (p1[2] - p2[2])**2
        )

    center: tuple = (0.0, 0.0, 0.0)
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    f: tuple = get_player_pos()
    print(f"Got a first tuple: ({f[0]}, {f[1]}, {f[2]})")
    print(f"It includes: (X={f[0]}, Y={f[1]}, Z={f[2]})")
    dist: float = round(distance(center, f), 4)
    print(f"Distance to center: {dist}")
    print("\nGet a second set of coordinates")
    s: tuple = get_player_pos()
    dist = round(distance(f, s), 4)
    print(f"Distance to center: {dist}")


if __name__ == "__main__":
    ft_coordinate_system()
