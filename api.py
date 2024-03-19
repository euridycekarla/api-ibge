import requests

estados_brasileiros = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

while True:
    estado = input('Digite a sigla do estado (exemplo: PB para Paraíba):')
    if estado in estados_brasileiros:
        url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{estado}/municipios"
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()
            for cidade in dados:
                print(cidade['nome'])
            break
        else:
            print("Ocorreu um erro ao tentar obter os dados. Por favor, tente novamente.")
    else:
        print("A sigla inserida não corresponde a um estado brasileiro válido. Por favor, tente novamente.")
