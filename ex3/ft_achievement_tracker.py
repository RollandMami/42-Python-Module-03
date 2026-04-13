# ************************************************************************** #
#                                                                            #
#                                                       :::      ::::::::    #
#    ft_achievement_tracker.py                         :+:      :+:    :+:   #
#                                                   +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari  +#+  +:+       +#+         #
#                                               +#+#+#+#+#+   +#+            #
#    Created: 2026/04/08 18:05:18 by mamiandr        #+#    #+#              #
#    Updated: 2026/04/11 21:40:24 by mamiandr       ###   ########.fr        #
#                                                                            #
# ************************************************************************** #

import random

ACHIVEMENTS: set = {'Crafting Genius', 'Strategist', 'World Savior',
                    'Speed Runner', 'Survivor', 'Master Explorer',
                    'Treasure Hunter', 'Unstoppable', 'First Steps',
                    'Collector Supreme', 'Untouchable', 'Sharp Mind',
                    'Boss Slayer'
                    }


def gen_player_achievements() -> set:
    number_of_achievements: int = random.randint(1, len(ACHIVEMENTS) - 1)
    result: set = set(random.sample(list(ACHIVEMENTS), number_of_achievements))
    return result


def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")
    Alice: set = gen_player_achievements()
    Bob: set = gen_player_achievements()
    Charlie: set = gen_player_achievements()
    Dylan: set = gen_player_achievements()
    print(f"Player Alice: {Alice}")
    print(f"Player Bob: {Bob}")
    print(f"Player Charlie: {Charlie}")
    print(f"Player Dylan: {Dylan}")
    print(f"\nAll distinct achievements: \
{set.union(Alice, Bob, Charlie, Dylan)}")
    print(f"\nCommon achievements: \
{set.intersection(Alice, Bob, Charlie, Dylan)}")
    print(f"\nOnly Alice: {Alice.difference(Bob, Charlie, Dylan)}")
    print(f"Only Bob: {Bob.difference(Alice, Charlie, Dylan)}")
    print(f"Only Charlie: {Charlie.difference(Alice, Bob, Dylan)}")
    print(f"Only Dylan: {Dylan.difference(Alice, Bob, Charlie)}")
    print(f"\nAlice is missing: {ACHIVEMENTS.difference(Alice)}")
    print(f"Bob is missing: {ACHIVEMENTS.difference(Bob)}")
    print(f"Charlie is missing: {ACHIVEMENTS.difference(Charlie)}")
    print(f"Dylan is missing: {ACHIVEMENTS.difference(Dylan)}")


if __name__ == "__main__":
    ft_achievement_tracker()
