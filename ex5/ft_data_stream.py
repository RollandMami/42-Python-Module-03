# ************************************************************************** #
#                                                                            #
#                                                       :::      ::::::::    #
#    ft_data_stream.py                                 :+:      :+:    :+:   #
#                                                   +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari  +#+  +:+       +#+         #
#                                               +#+#+#+#+#+   +#+            #
#    Created: 2026/04/08 18:05:18 by mamiandr        #+#    #+#              #
#    Updated: 2026/04/11 21:40:24 by mamiandr       ###   ########.fr        #
#                                                                            #
# ************************************************************************** #

import typing
import random


PLAYERS: list = ['bob', 'alice', 'dylan', 'charlie']
ACTION: list = ['run', 'eat', 'sleep', 'grab', 'move',
                'climb', 'swim', 'release']

def gen_event() -> typing.Generator:
    while True:
        yield random.choice(PLAYERS), random.choice(ACTION)

def consume_event(listes: list) -> typing.Generator:

    def del_elm(lst, elm) -> list:
        flag: int = 0
        result: list = []
        for x in lst:
            if (x == elm and not flag):
                flag = 1
            else:
                result.append(x)
        return result

    while (len(listes) > 0):
        choix: tuple = random.choice(listes)
        listes = del_elm(listes, choix)
        yield choix


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")
    evnt_gen = gen_event()
    for i in range(1000):
        event: tuple = next(evnt_gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    event_lst: list = []
    for i in range(10):
        event_lst.append(next(evnt_gen))
    print(f"Built list of 10 events: {event_lst}")
    consomable: typing.Generator = consume_event(event_lst)
    for event in consomable:
        print(f"Got event from list: {event}")
        print(f"Remains in list: {consomable}")

if __name__ == "__main__":
    ft_data_stream()
