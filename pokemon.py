# -*- coding: utf-8 -*-

from weapon_type import WeaponType

class Pokemon():

    def __init__(self, id, pokemon_name, weapon_type, health_points, attack_rating, defense_rating):
        self.id = id
        if not isinstance(id, int):
            raise TypeError("El id debe ser un entero")
        self.pokemon_name = pokemon_name
        if not isinstance(pokemon_name, str):
            raise TypeError("El pokemon_name debe ser un string")
        self.weapon_type = weapon_type
        if not isinstance(weapon_type, WeaponType):
            raise TypeError("El weapon_type debe ser un weapon_type")
        self.health_points = health_points
        if not isinstance(health_points, int) or health_points < 0 or health_points > 100:
            raise TypeError("Los health_points deben ser un entero entre 0 y 100")
        self.attack_rating = attack_rating
        if not isinstance(attack_rating, int) or attack_rating < 0 or attack_rating > 10:
            raise TypeError("El attack_rating debe ser un entero entre 0 y 10")
        self.defense_rating = defense_rating
        if not isinstance(defense_rating, int) or defense_rating < 0 or defense_rating > 10:
            raise TypeError("El defense_rating debe ser un entero entre 0 y 10")
    
    def __del__(self):
        return "Pokemon " + str(self.pokemon_name) + " has been deleted"
    
    def is_alive(self):
        return self.health_points > 0
    
    def fight_defense(self, points_of_damage):
        if self.defense_rating > points_of_damage:
            return False
        else:
            self.health_points = max(self.health_points - (points_of_damage - self.defense_rating),0)
            return True
        
    def fight_attack(self, pokemon_to_attack):
        return pokemon_to_attack.fight_defense(self.attack_rating)
    
    def __str__(self):
        return "Pokemon id " + str(self.id) + " with name " + self.pokemon_name + " has as weapon " + self.weapon_type.name + " and health " + str(self.health_points)

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_pokemon_name(self):
        return self.pokemon_name

    def set_pokemon_name(self, pokemon_name):
        self.pokemon_name = pokemon_name

    def get_weapon_type(self):
        return self.weapon_type

    def set_weapon_type(self, weapon_type):
        self.weapon_type = weapon_type

    def get_health_points(self):
        return self.health_points

    def set_health_points(self, health_points):
        self.health_points = health_points

    def get_attack_rating(self):
        return self.attack_rating

    def set_attack_rating(self, attack_rating):
        self.attack_rating = attack_rating

    def get_defense_rating(self):
        return self.defense_rating

    def set_defense_rating(self, defense_rating):
        self.defense_rating = defense_rating


def main():

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = Pokemon(1, "Ivysaur", WeaponType.HEADBUTT, 100, 8, 9)

    if pokemon_1.get_pokemon_name() == "Ivysaur":
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

    if pokemon_1.get_attack_rating() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defense_rating() == 9:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = Pokemon(2, "Chweapon_typender",
                        WeaponType.HEADBUTT, 100, 7, 10)

    if str(pokemon_2) == "Pokemon id 2 with name Chweapon_typender has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." +
              " RESULT: " + str(pokemon_2))

    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = Pokemon(3, "Wartortle", WeaponType.KICK, 97, 8, 9)

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
    pokemon_4 = Pokemon(4, "Squirtle", WeaponType.ELBOW, 93, 9, 6)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 29:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")

    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = Pokemon(5, "Venusaur", WeaponType.PUNCH, 99, 10, 7)
    pokemon_6 = Pokemon(6, "Charmeleon", WeaponType.PUNCH, 99, 9, 8)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 97:
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
