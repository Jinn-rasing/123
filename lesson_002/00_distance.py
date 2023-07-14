#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = dict()

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']
moscow_london = ( (moscow[0] - london[0])**2 + (moscow[1] - london[1])**2) ** .5
moscow_paris = ( (moscow[0] - paris[0])**2 + (moscow[1] - paris[1])**2) ** .5
# TODO здесь заполнение словаря
distances['Moscow'] = { }
distances['Moscow'] ['London'] = 145
distances['Moscow'] ['Paris'] = 130

london_paris = ( (paris[0] - london[0])**2 + (paris[1] - london[1])**2) ** .5

distances['London'] = { }
distances['London']['Moscow'] = 145
distances['London']['Paris'] = 42

distances['Paris'] = { }
distances['Paris'] ['Moscow'] = 130
distances['Paris'] ['London'] = 42

pprint(distances)

print(distances ['Moscow']['Paris'])


