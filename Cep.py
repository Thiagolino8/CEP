import requests


class Cep:
    def __init__(self, cep):
        cep = str(cep)
        if len(cep) == 8:
            self._cep = cep
        else: raise ValueError("O CEP É INVÁLIDO!")

    def __str__(self):
        return self.cpf_formatado()

    def cpf_formatado(self):
        return f"{self._cep[:5]}-{self._cep[5:]}"

    def cep_request(self):
        url = f"https://viacep.com.br/ws/{self._cep}/json"
        r = requests.get(url)
        return
