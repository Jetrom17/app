from kivy.app import App # GUI
from kivy.lang import Builder # Contruir
import requests

GUI = Builder.load_file("tela.kv")


class MeuAplicativo(App):
    def build(self):
        return GUI

    def on_start(self):
        self.root.ids["moeda1"].text = f"Dólar R${self.coin('USD')}"
        self.root.ids["moeda2"].text = f"Euro R${self.coin('EUR')}"
        self.root.ids["moeda3"].text = f"Bitcoin R${self.coin('BTC')}"
        self.root.ids["moeda4"].text = f"Ethereum R${self.coin('ETH')}"

    def coin(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao


MeuAplicativo().run()

# api: https://docs.awesomeapi.com.br/api-de-moedas
