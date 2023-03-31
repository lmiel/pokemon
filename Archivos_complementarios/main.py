#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pokemon import Pokemon
from random import random

"""This Python method contains the application of the Game.

@contents :  This module contains the complete implementation of the application
             of the Game.
@project :  N/A
@program :  N/A
@file :  main.py
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

def get_data_from_user(name_file):
  lista_pokemon = []
  file = open(name_file, "r")
  for linea in file.readlines():
    pokemon = linea.split(",") #para cada linea del fichero, separamos los datos por comas y los guardamos en una lista
    lista_pokemon.append(Pokemon(pokemon[0], pokemon[1], pokemon[2], pokemon[3], pokemon[4], pokemon[5])) #id, pokemon_name, weapon_type, health_points, attack_rating, defense_rating
  return lista_pokemon

def get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):
  lista_pokemon = list_of_pokemons.get(coach_to_ask)
  for pokemon in lista_pokemon:
    if not pokemon.is_alive():
      lista_pokemon.remove(pokemon)
  return lista_pokemon

def coach_is_undefeated(list_of_pokemons):
  if len(list_of_pokemons) == 0:
    return False
  return True

def main():
  
  print("Welcome to the Game.")
  print("Let's start to set the configuration of each game user. \n")

  pokemons_coach_1 = get_data_from_user("coach_1_pokemons.csv")
  pokemons_coach_2 = get_data_from_user("coach_2_pokemons.csv")
  
  print("------------------------------------------------------------------")
  print("The Game starts...")
  print("------------------------------------------------------------------")

  list_of_pokemons = {}
  list_of_pokemons[1] = pokemons_coach_1
  list_of_pokemons[2] = pokemons_coach_2

  current_round = 1
  while coach_is_undefeated(list_of_pokemons[1]) and coach_is_undefeated(list_of_pokemons[2]):
    print("Current round: ", current_round)
    print("------------------------------------------------------------------")
    
    pokemon_coach_1 = random.choice(get_pokemon_in_a_list_of_pokemons(1, list_of_pokemons))
    pokemon_coach_2 = random.choice(get_pokemon_in_a_list_of_pokemons(2, list_of_pokemons))
    
    print(pokemon_coach_1.get_pokemon_name(), " is facing ", pokemon_coach_2.get_pokemon_name())
    print(pokemon_coach_1)
    print(pokemon_coach_2)

    #Mientras coach 1 y coach 2 esten vivos
    while pokemon_coach_1.is_alive() and pokemon_coach_2.is_alive():
      if pokemon_coach_1.fight_attack(pokemon_coach_2):
        print(pokemon_coach_1.get_pokemon_name(), " attacked ", pokemon_coach_2.get_pokemon_name(), " and caused ", pokemon_coach_1.get_attack_rating(), " damage points")
      else:
        print(pokemon_coach_2.get_pokemon_name(), " defended ", pokemon_coach_1.get_pokemon_name(), "'s attack")
      
      if pokemon_coach_2.is_alive():
        if pokemon_coach_2.fight_attack(pokemon_coach_1):
          print(pokemon_coach_2.get_pokemon_name(), " attacked ", pokemon_coach_1.get_pokemon_name(), " and caused ", pokemon_coach_2.get_attack_rating(), " damage points")
        else:
          print(pokemon_coach_1.get_pokemon_name(), " defended ", pokemon_coach_2.get_pokemon_name(), "'s attack")
      
      print(pokemon_coach_1)
      print(pokemon_coach_2)
      
    if pokemon_coach_1.is_alive():
      print(pokemon_coach_1.get_pokemon_name(), " won this round")
      list_of_pokemons[2].remove(pokemon_coach_2)
    else:
      print(pokemon_coach_2.get_pokemon_name(), " won this round")
      list_of_pokemons[1].remove(pokemon_coach_1)
    
    print("------------------------------------------------------------------")
    current_round += 1
 
  print("------------------------------------------------------------------")
  print("The Game has end...")
  print("------------------------------------------------------------------")

  print("------------------------------------------------------------------")
  print("Statistics")
  print("------------------------------------------------------------------")
  if coach_is_undefeated(list_of_pokemons[1]):
    print("Game User 1: won the game!")
  else:
    print("Game User 2: won the game!")


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()

# EOF
