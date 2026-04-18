class figuras:
    def Tipo(self):
        print("Es una figura geometrica")

class tres_Lados(figuras):
    def __init__(self):
        self.__lados=3

    def Ladosf(self):
        return self.__lados
    def NumeroLados(self):
        print(f"Tiene {self.__lados} Lados")

    def NumeroLadosIguales(self):
        print("Todavia no hay informacion suficiente")

class escalenos(tres_Lados):
    def NumeroLadosIguales(self):
        print("Todos sus lados son de diferente longitud")

class isosceles(tres_Lados):
    def NumeroLadosIguales(self):
        print("Tiene 2 lados iguales")

class equilatero(tres_Lados):
    def NumeroLadosIguales(self):
        print("Todos sus lados son iguales")

class acutangulo(tres_Lados):
    def TipoDeAngulos(self):
        print("Todos sus lados son agudos(menos de 90 grados)")

class trectangulo(tres_Lados):
    def TipoDeAngulo(self):
        print("Tiene un angulo recto(90 grados)")

class obtusangulo(tres_Lados):
    def TipoDeAngulo(self):
        print("Tiene un angulo obtuso(mayor a 90 grados), los otros dos son agudos")

class equilatero_Acutangulo(equilatero,acutangulo):
    def Figura(self):
        print("Es un triangulo equilatero y acutangulo")

class isosceles_acutangulo(isosceles,acutangulo):
    def Figura(self):
        print("Es un triangulo isosceles y acutangulo")

class isosceles_Rectangulo(isosceles,trectangulo):
    def Figura(self):
        print("Es un triangulo isosceles y rectangulo")

class isosceles_obtusangulo(isosceles,obtusangulo):
    def Figura(self):
        print("Es un triangulo isosceles y obtusangulo")

class escaleno_acutangulo(escalenos,acutangulo):
    def Figura(self):
        print("Es un triangulo escaleno y acutangulo")

class escaleno_rectangulo(escalenos, trectangulo):
    def Figura(self):
        print("Es un triangulo escaleno y rectangulo")

class escaleno_obtusangulo(escalenos,obtusangulo):
    def Figura(self):
        print("Es un triangulo escaleno y obtusangulo")

class cuatro_Lados(figuras):
    def __init__(self):
        self.__lados=4

    def Ladosf(self):
        return self.__lados
    def NumeroLados(self):
        print(f"Tiene {self.__lados} Lados")


class cuadrilateros(cuatro_Lados):
    def LadosParalelos(self):
        print("Puede tener lados paralelos")  

class paralelogramo(cuadrilateros):
    def LadosParalelos(self):
        print("Tiene 2 pares de lados paralelos y congruentes")

class cuadrado(paralelogramo):
    def Lados(self):
        print("Tiene 4 lados iguales")
    def Angulos(self):
        print("Tiene 4 Angulos rectos")  

class rectangulo(paralelogramo):
    def Lados(self):
        print("Tiene lados opuestos")
    def Angulos(self):
        print("Tiene 4 Angulos rectos")  

class rombo(paralelogramo):
    def Lados(self):
        print("Tiene 4 lados iguales")
    def Angulos(self):
        print("No tiene Angulos rectos")  

class romboide(paralelogramo):
    def Lados(self):
        print("Tiene lados opuestos")
    def Angulos(self):
        print("Tiene angulos distintos a 90 grados")  

class trapecio(cuadrilateros):
    def LadosParalelos(self):
        print("Tiene solo un par de lados paralelos")

class trapecio_rectangulo(trapecio):
    def Angulos(self):
        print("Tiene un angulo recto")

class trapecio_isosceles(trapecio):
    def Lados(self):
        print("Lados no paralelos iguales")

class trapecio_escaleno(trapecio):
    def Lados(self):
        print("Tiene todos los lados diferentes")
    def Angulos(self):
        print("Tiene todos los angulos diferentes")

class trapezoides(cuadrilateros):
    def LadosParalelos(self):
        print("No tienen lados paralelos")

class cinco_lados(figuras):
    def __init__(self):
        self.__lados=5

    def Ladosf(self):
        return self.__lados
    def NumeroLados(self):
        print(f"Tiene {self.__lados} Lados")

class pentagono(cinco_lados):
    def Figura(self):
        print("Es un pentagono")

class seis_lados(figuras):
    def __init__(self):
        self.__lados=6

    def Ladosf(self):
        return self.__lados
    def NumeroLados(self):
        print(f"Tiene {self.__lados} Lados")

class hexagono(seis_lados):
    def Figura(self):
        print("Es un hexagono")

class siete_lados(figuras):
    def __init__(self):
        self.__lados=7

    def Ladosf(self):
        return self.__lados
    def NumeroLados(self):
        print(f"Tiene {self.__lados} Lados")

class heptagono(siete_lados):
    def Figura(self):
        print("Es un heptagono")

class ocho_lados(figuras):
    def __init__(self):
        self.__lados=8

    def Ladosf(self):
        return self.__lados
    def NumeroLados(self):
        print(f"Tiene {self.__lados} Lados")

class octagono(ocho_lados):
    def Figura(self):
        print("Es un octagono")

class nueve_lados(figuras):
    def __init__(self):
        self.__lados=9

    def Ladosf(self):
        return self.__lados
    def NumeroLados(self):
        print(f"Tiene {self.__lados} Lados")

class eneagono(nueve_lados):
    def Figura(self):
        print("Es un eneagono")

class diez_lados(figuras):
    def __init__(self):
        self.__lados=10

    def Ladosf(self):
        return self.__lados
    def NumeroLados(self):
        print(f"Tiene {self.__lados} Lados")

class decagono(diez_lados):
    def Figura(self):
        print("Es un decagono")
