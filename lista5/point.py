# 41. Considerando a classe Point definida a seguir, crie um método reflect_x que retorno um novo objeto
# Point que é a reflexão do ponto no eixo x. Por exemplo, Point(3,5).reflectX() retorno o ponto $3,-5).

# 42. Ainda considerando a classe Point, implemente os seguintes métodos: slope_from_origin(): retorna a inclinação
# da linha que liga o ponto à origem

# 43. Seja y=ax+b a equação de uma reta. Escreva um método na classe Point que recebe outra instância de
# Point e calcula a equação da reta entre esses dois pontos. O método deve retornar os dois coeficientes
# na forma de uma tupla com dois valores, correspondentes aos coeficientes da equação.

class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def reflect_x(self):
        return self.x, -self.y

    def slope_from_origin(self):
        if self.x == 0:
            return None
        else:
            return self.y / self.x

    def calcula_reta(self, target):
        a = (self.y - target.y) / (self.x - target.x)
        b = self.y - a*self.x
        return (a, b)
