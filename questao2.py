import requests

def obter_municipios(uf):
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        municipios = resposta.json()
        return [municipio['nome'] for municipio in municipios]
    else:
        print("Erro ao obter dados da API.")
        return []

if __name__ == "__main__":
    uf = input("Digite o código do estado (ex: 33 para RJ): ")
    municipios = obter_municipios(uf)
    
    if municipios:
        print("Municípios encontrados:")
        for nome in municipios:
            print(f"- {nome}")
    else:
        print("Nenhum município encontrado.")