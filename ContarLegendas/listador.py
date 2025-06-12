import os
import re
from collections import defaultdict

pasta_zips = r'C:\Users\Leoman\Desktop\Legendas\Legendas'
regex_ano = re.compile(r'\b(19\d{2}|20\d{2})\b')

ano_min = int(input("Digite o ano mínimo: "))
ano_max = int(input("Digite o ano máximo: "))

arquivos_por_ano = defaultdict(list)

for nome_zip in os.listdir(pasta_zips):
    if nome_zip.lower().endswith('.zip'):
        match_ano = regex_ano.search(nome_zip)
        if match_ano:
            ano = int(match_ano.group(1))
            if ano_min <= ano <= ano_max:
                # Extrai o nome até o final do ano (posição do fim da correspondência)
                fim_ano_index = match_ano.end()
                nome_limpo = nome_zip[:fim_ano_index].strip()
                arquivos_por_ano[ano].append(nome_limpo)
        else:
            print(f"⚠️ Ano não encontrado no nome: {nome_zip}")

# Juntar todos os nomes limpos em uma lista única
todos_os_arquivos = []
for ano in sorted(arquivos_por_ano):
    todos_os_arquivos.extend(arquivos_por_ano[ano])

# Mostrar todos os nomes dos arquivos em sequência
print(f"\n🗂️ Arquivos entre {ano_min} e {ano_max}:")
for nome in todos_os_arquivos:
    print(nome)

print(f"\n🧮 Total de arquivos: {len(todos_os_arquivos)}")
