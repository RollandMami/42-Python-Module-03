# ************************************************************************** #
#                                                                            #
#                                                       :::      ::::::::    #
#    ft_data_alchemist.py                              :+:      :+:    :+:   #
#                                                   +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari  +#+  +:+       +#+         #
#                                               +#+#+#+#+#+   +#+            #
#    Created: 2026/04/08 18:05:18 by mamiandr        #+#    #+#              #
#    Updated: 2026/04/11 21:40:24 by mamiandr       ###   ########.fr        #
#                                                                            #
# ************************************************************************** #

import random


def ft_data_alchemist() -> None:
    initial_data: list = [
        'Alice', 'bob', 'Charlie',
        'dylan', 'Emma', 'Gregory',
        'john', 'kevin', 'Liam'
        ]
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {initial_data}")
    new_capitalized: list = [player.capitalize() for player in initial_data]
    print(f"New list with all names capitalized: {new_capitalized}")
    new_only_capital: list = [
        player for player in initial_data if player[0].isupper()
    ]
    print(f"New list of capitalized names only: {new_only_capital}\n")
    score_dict: dict = {
        player: random.randint(1, 1000) for player in new_capitalized
        }
    print(f"Score dict: {score_dict}")
    total_score: int = sum(score_dict.values())
    numbers: int = len(score_dict)
    average: float = round(total_score / numbers, 2)
    print(f"Score average is {average}")
    higher_score: dict = {
        player: score for player, score in score_dict.items()
        if score > average
        }
    print(f"Hight scores: {higher_score}")


if __name__ == "__main__":
    ft_data_alchemist()
