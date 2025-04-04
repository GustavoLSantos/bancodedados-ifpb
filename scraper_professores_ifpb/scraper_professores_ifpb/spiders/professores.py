# cls ; scrapy runspider .\scraper_professores_ifpb\spiders\professores.py --loglevel=WARNING
import re
import scrapy
import pandas as pd

class Professores(scrapy.Spider):
    name = 'Professores'
    allowed_domains = ['www.ifpb.edu.br']
    start_urls = [
        'https://www.ifpb.edu.br/ppgti/programa/corpo-docente',
    ]

    PROFESSORES = {
        'nome': [],
        'linha_pesquisa': [],
        'lattes': [],
        'email': [],
    }

    def parse(self, response):

        lista_professores = response.css('#parent-fieldname-text')

        self.extrair_professores(lista_professores)
        self.extrair_descricoes(lista_professores)

        df = pd.DataFrame(self.PROFESSORES)

        df.to_csv('professores.csv', index=None)

    def extrair_professores(self, lista_professores):

        professores = lista_professores.css('h4')

        for professor in professores:
            nome = professor.xpath("string(.)").get()

            if len(nome) > 1:
                self.PROFESSORES['nome'].append(str(nome).replace('\xa0', ' ').strip())


    def extrair_descricoes(self, lista_professores):

        descricoes = lista_professores.css('p')

        DESCRICOES = []

        for descricao in descricoes:
            descricao = descricao.xpath('string(.)').get().replace('\xa0', ' ').strip()

            replaces = [
                'Linha de Pesquisa:',
                'Currículo Lattes:',
                'E-mail:',
            ]

            for rep in replaces:
                descricao = descricao.replace(rep, ' <SEP> ')

            descricao = descricao.split('<SEP>')
            descricao = [desc.strip() for desc in descricao if desc.strip()]

            if len(descricao) == 1:
                DESCRICOES[-1].append(descricao[0])
            else:
                DESCRICOES.append(descricao)

        for desc in DESCRICOES:
            self.PROFESSORES['linha_pesquisa'].append(desc[0])
            self.PROFESSORES['lattes'].append(desc[1])
            self.PROFESSORES['email'].append(desc[2])
