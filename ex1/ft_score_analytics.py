# ************************************************************************** #
#                                                                            #
#                                                       :::      ::::::::    #
#    ft_score_analytics.py                            :+:      :+:    :+:    #
#                                                   +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari  +#+  +:+       +#+         #
#                                               +#+#+#+#+#+   +#+            #
#    Created: 2026/04/08 18:05:18 by mamiandr        #+#    #+#              #
#    Updated: 2026/04/11 21:40:24 by mamiandr       ###   ########.fr        #
#                                                                            #
# ************************************************************************** #

import sys


def ft_score_analytics(args: list) -> None:

    def print_list(data: list):
        k: int = 0
        print("Scores processed: [", end="")
        while (k < len(data)):
            print(f"{data[k]}", end="")
            if (k < len(data) - 1):
                print(", ", end="")
            k += 1
        print("]")
        print(f"Total players: {len(data)}")
        print(f"Total score: {sum(data)}")
        print(f"Average score: {round(sum(data)/len(data), 1)}")
        print(f"High players: {max(data)}")
        print(f"Low players: {min(data)}")
        print(f"Score range: {max(data) - min(data)}")

    print("=== Player Score Analytics ===")
    scores: list = []
    if (len(args) == 1):
        print("No scores provided. Usage: python3 ft_score_analytics.py \
<score1> <score2> ...")
        return None
    i: int = 1
    while (i < len(args)):
        try:
            elm: int = int(args[i])
            scores.append(elm)
        except ValueError:
            print(f"Invalid parameter: '{args[i]}'")
        i += 1
    if (not scores):
        print("No scores provided. Usage: python3 ft_score_analytics.py \
<score1> <score2> ...")
        return None
    print_list(scores)


if __name__ == "__main__":
    ft_score_analytics(sys.argv)
