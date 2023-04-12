#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pokemon import Pokemon
from weapon_type import WeaponType

"""
This Python module contains not only the class Pokemon, but also the test of
this Python class.

@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  pokemon.py
@author :  Antonio Artes Garcia (antonio.artesgarcia@ceu.es)
           Francisco Hernando Gallego (francisco.hernandogallego@ceu.es)
           Ruben Juarez Cadiz (ruben.juarezcadiz@ceu.es)

@version :  0.0.1, 08 November 2021
@information :  The Zen of Python
                  https://www.python.org/dev/peps/pep-0020/
                Style Guide for Python Code
                  https://www.python.org/dev/peps/pep-0008/
                Example NumPy Style Python Docstrings
                  http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
                doctest – Testing through documentation
                  https://pymotw.com/2/doctest/

@copyright :  Copyright 2021 GNU AFFERO GENERAL PUBLIC.
              All rights are reserved. Reproduction in whole or in part is
              prohibited without the written consent of the copyright owner.
"""


# Source packages.


class PokemonWater(Pokemon):
    def __init__(self, id, pokemon_name, weapon_type, health_points, attack_rating, defense_rating):
        super().__init__(id, pokemon_name, weapon_type, health_points, 0, defense_rating)
        self.attack_rating = attack_rating
        if not isinstance(attack_rating, int) or attack_rating < 11 or attack_rating > 20:
            raise TypeError("El attack_rating debe ser un entero entre 11 y 20")

    def __str__(self):
        return "Pokemon ID " + str(self.id) + " with name " + self.pokemon_name + " has as weapon " + self.weapon_type.name + " and health " + str(self.health_points)

def main():

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = PokemonWater(1, "Squirtle", WeaponType.HEADBUTT, 100, 12, 8)

    if pokemon_1.get_pokemon_name() == "Squirtle":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_weapon_type().name == "HEADBUTT":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_attack_rating() == 12:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defense_rating() == 8:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = PokemonWater(7, "Squirtle", WeaponType.HEADBUTT, 100, 15, 7)

    if str(pokemon_2) == "Pokemon ID 7 with name Squirtle has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." +
              " RESULT: " + str(pokemon_2))

    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonWater(3, "Squirtle", WeaponType.KICK, 97, 15, 8)

    if pokemon_3.is_alive():
        # With this the Pokemon should be retired.
        pokemon_3.fight_defense(200)

        if not pokemon_3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")

    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = PokemonWater(4, "Squirtle", WeaponType.ELBOW, 93, 11, 9)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 32:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")

    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = PokemonWater(5, "Squirtle", WeaponType.PUNCH, 99, 20, 10)
    pokemon_6 = PokemonWater(6, "Squirtle", WeaponType.PUNCH, 99, 18, 9)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 88:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
