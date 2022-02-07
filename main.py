#Jogo do Par ou impar
from random import randint

class ParOuImpar:
    def __init__(self):
        self.jogar = True


    def Iniciar(self):
        while self.jogar == True:
            resposta = int(input('Digite [1] para Par e [2] para ímpar [3] para Sair'))
            self.NumeroComputador()
            if resposta == 1:
                self.NumeroJogador()
                print(f"Você escolheu PAR e jogou {self.Jogador} e o computador jogou {self.Computador}")
                if self.tipo_numero_jogador == 0 and self.tipo_numero_computador == 0:
                    print("Você venceu, deu PAR!")
                elif self.tipo_numero_jogador == 0 and self.tipo_numero_computador == 1:
                    print("Você perdeu, deu IMPAR!")
                elif self.tipo_numero_jogador == 1 and self.tipo_numero_computador == 1:
                    print("Você venceu, deu PAR!")
                elif self.tipo_numero_jogador == 1 and self.tipo_numero_computador == 0:
                    print("Você perdeu, deu IMPAR!")
            elif resposta == 2:
                    self.NumeroJogador()
                    print(f"Você escolhaue ÍMPAR e jogou {self.Jogador} e o computador jogou {self.Computador}")
                    if self.tipo_numero_jogador == 0 and self.tipo_numero_computador == 0:
                        print("Você perdeu, deu PAR!")
                    elif self.tipo_numero_jogador == 0 and self.tipo_numero_computador == 1:
                        print("Você venceu, deu IMPAR!")
                    elif self.tipo_numero_jogador == 1 and self.tipo_numero_computador == 1:
                        print("Você perdeu, deu PAR!")
                    elif self.tipo_numero_jogador == 1 and self.tipo_numero_computador == 0:
                        print("Você venceu, deu IMPAR!")
            elif resposta == 3:
                self.jogar = False
            else:
                print("\033[31mEscolha apenas [1] para Par ou [2] para Impar!!\033[m")

    def NumeroJogador(self):
        self.Jogador = int(input('Digite um número'))
        self.tipo_numero_jogador = self.Jogador % 2

    def NumeroComputador(self):
        self.GerarNumeroComputador()
        self.tipo_numero_computador = self.Computador % 2

    def GerarNumeroComputador(self):
        self.Computador = randint(1,20)






jogo = ParOuImpar()
jogo.Iniciar()