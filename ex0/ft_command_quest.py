# ************************************************************************** #
#                                                                            #
#                                                       :::      ::::::::    #
#    ft_command_quest.py                              :+:      :+:    :+:    #
#                                                   +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari  +#+  +:+       +#+         #
#                                               +#+#+#+#+#+   +#+            #
#    Created: 2026/04/08 18:05:18 by mamiandr        #+#    #+#              #
#    Updated: 2026/04/11 21:41:25 by mamiandr       ###   ########.fr        #
#                                                                            #
# ************************************************************************** #

import sys


def ft_command_quest(arg: list) -> None:
    print("=== Command Quest ===")
    print(f"Program name: {arg[0]}")
    if (len(arg) <= 1):
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(arg) - 1}")
        for i in range(1, len(arg)):
            print(f"Argument {i}: {arg[i]}")
    print(f"Total arguments: {len(arg)}")


if __name__ == "__main__":
    ft_command_quest(sys.argv)
