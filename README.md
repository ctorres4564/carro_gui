
# 🚗 Simulador de Carro com Interface Gráfica (Tkinter)

Este projeto é um simulador interativo de carro feito em Python com interface gráfica usando `tkinter`. O usuário pode ligar e desligar o carro, abastecer, acelerar, frear, buzinar e visualizar o status em tempo real.

## 🎯 Objetivo

Simular as funcionalidades básicas de um carro real de forma didática, usando os conceitos de **Programação Orientada a Objetos (POO)** em Python.

---

## 🖥️ Interface

A interface foi construída com `tkinter` e apresenta:

- Caixa de status com informações atualizadas do carro
- Botões para:
  - **Ligar**
  - **Desligar**
  - **Abastecer**
  - **Acelerar**
  - **Frear**
  - **Buzinar**

---

## 📦 Requisitos

- Python 3.7+
- Biblioteca padrão `tkinter` (já vem com o Python)

---

## 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/simulador-carro.git
   cd simulador-carro
   ```

2. Execute o script:
   ```bash
   python carro_gui.py
   ```

---

## 🧊 Como gerar o executável (.exe)

Caso deseje criar um arquivo executável:

1. Instale o PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Gere o `.exe`:
   ```bash
   pyinstaller --noconfirm --onefile --windowed carro_gui.py
   ```

3. O executável estará na pasta `dist/`.

---

## 🧠 Conceitos abordados

- Programação Orientada a Objetos (POO)
- Encapsulamento de atributos e métodos
- Interface gráfica com tkinter
- Simulação de comportamento real

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT.

---

## ✨ Autor

Desenvolvido por [Claudio Torres](https://github.com/ctorres4564)
