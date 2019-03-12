#!/usr/bin/python3
# -*- coding:utf-8 -*-
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class DouDiZhu:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'BigBoss SmallBoos'.split()

    def __init__(self):
        self._card = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._card)

    def __getitem__(self, item):
        return self._card[item]


if __name__ == '__main__':
    beer_card = Card('7', 'BigBoos')
    # print(beer_card)
    ddz = DouDiZhu()
    for card in ddz:
        print(card)



