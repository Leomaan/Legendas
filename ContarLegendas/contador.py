import os
import re
from collections import defaultdict

pasta_zips = r'C:\Users\Leoman\Desktop\Legendas\Legendas'

regex_ano = re.compile(r'\b(19\d{2}|20\d{2})\b')

ano_min = 1970
ano_max = 2020

arquivos_por_ano = defaultdict(list)

for nome_zip in os.listdir(pasta_zips):
    if nome_zip.lower().endswith('.zip'):
        match_ano = regex_ano.search(nome_zip)
        if match_ano:
            ano = int(match_ano.group(1))
            if ano_min <= ano <= ano_max:
                arquivos_por_ano[ano].append(nome_zip)
        else:
            print(f"⚠️ Ano não encontrado no nome: {nome_zip}")

# Mostrar resultados
for ano in sorted(arquivos_por_ano):
    print(f"\n📁 Ano {ano} - {len(arquivos_por_ano[ano])} arquivos:")
    for arquivo in arquivos_por_ano[ano]:
        print(f"  {arquivo}")

print(f"\n🧮 Total de arquivos entre {ano_min} e {ano_max}: {sum(len(v) for v in arquivos_por_ano.values())}")