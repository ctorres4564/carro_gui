import tkinter as tk
from tkinter import messagebox

class Carro:
    def __init__(self, marca, modelo, ano, cor, tipo_combustivel, capacidade_tanque, consumo_km_l):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.tipo_combustivel = tipo_combustivel
        self.capacidade_tanque = capacidade_tanque
        self.consumo_km_l = consumo_km_l
        self.nivel_combustivel = 0
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            return f"{self.modelo} ligado."
        return f"{self.modelo} já está ligado."

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            return f"{self.modelo} desligado."
        return f"{self.modelo} já está desligado."

    def abastecer(self, litros):
        if self.nivel_combustivel + litros <= self.capacidade_tanque:
            self.nivel_combustivel += litros
            return f"Abastecido com {litros}L. Nível atual: {self.nivel_combustivel:.1f}L"
        return "Capacidade do tanque excedida."

    def acelerar(self, km):
        if not self.ligado:
            return "Ligue o carro primeiro!"
        consumo = km / self.consumo_km_l
        if consumo <= self.nivel_combustivel:
            self.nivel_combustivel -= consumo
            self.velocidade += 10
            return f"Acelerando! Velocidade: {self.velocidade}km/h | Combustível: {self.nivel_combustivel:.1f}L"
        return "Combustível insuficiente."

    def frear(self):
        if self.ligado and self.velocidade > 0:
            self.velocidade -= 10
            return f"Freando... Velocidade: {self.velocidade}km/h"
        return "O carro já está parado."

    def buzinar(self):
        return "BEEP BEEP!"

    def status(self):
        return (
            f"Marca: {self.marca}\n"
            f"Modelo: {self.modelo}\n"
            f"Ano: {self.ano}\n"
            f"Cor: {self.cor}\n"
            f"Combustível: {self.nivel_combustivel:.1f}L / {self.capacidade_tanque}L\n"
            f"Velocidade: {self.velocidade}km/h\n"
            f"Ligado: {'Sim' if self.ligado else 'Não'}"
        )

# Interface com Tkinter
def atualizar_status():
    status_text.set(carro.status())

def acao(funcao, *args):
    resultado = funcao(*args)
    messagebox.showinfo("Resultado", resultado)
    atualizar_status()

# Criar o objeto carro
carro = Carro("Toyota", "Corolla", 2020, "Prata", "Gasolina", 50, 12)

# Criando a janela
janela = tk.Tk()
janela.title("Simulador de Carro")

# Status
status_text = tk.StringVar()
status_label = tk.Label(janela, textvariable=status_text, justify="left", font=("Arial", 10), bg="white", relief="sunken", width=50, height=7)
status_label.pack(pady=10)
atualizar_status()

# Botões
botoes = [
    ("Ligar", lambda: acao(carro.ligar)),
    ("Desligar", lambda: acao(carro.desligar)),
    ("Abastecer 20L", lambda: acao(carro.abastecer, 20)),
    ("Acelerar 60km", lambda: acao(carro.acelerar, 60)),
    ("Frear", lambda: acao(carro.frear)),
    ("Buzinar", lambda: acao(carro.buzinar)),
]

for nome, comando in botoes:
    tk.Button(janela, text=nome, command=comando, width=20).pack(pady=2)

janela.mainloop()
