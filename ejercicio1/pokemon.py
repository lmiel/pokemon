
class pokemon():
    def __init__(self, Id, Nombre, Arma, Ptos_salud, Id_ataque, Id_denfesa):
        self.Id = Id
        if not isinstance(Id, int):
            raise TypeError("El Id debe ser un entero")
        self.Nombre = Nombre
        if not isinstance(Nombre, str):
            raise TypeError("El Nombre debe ser un string")
        self.Arma = Arma
        if not isinstance(Arma, Arma):
            raise TypeError("El Arma debe ser un arma")
        self.Ptos_salud = Ptos_salud
        if not isinstance(Ptos_salud, int) or Ptos_salud < 0 or Ptos_salud > 100:
            raise TypeError("El Id debe ser un entero entre 0 y 100")
        self.Id_ataque = Id_ataque
        if not isinstance(Id_ataque, int) or Id_ataque < 0 or Id_ataque > 10:
            raise TypeError("El Id_ataque debe ser un entero entre 0 y 10")
        self.Id_denfesa = Id_denfesa
        if not isinstance(Id_denfesa, int) or Id_denfesa < 0 or Id_denfesa > 10:
            raise TypeError("El Id_denfesa debe ser un entero entre 0 y 10")
        
