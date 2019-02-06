# encoding=utf8
import sys
from xml.dom import minidom

reload(sys)
sys.setdefaultencoding('utf8')


class Parser:

    def __init__(self):
        self.xmldoc = minidom.parse('start/cnpq.xml')
        self.response = {}

    def parse_xml(self):
        """Método que faz a análise do documento xml."""
        # encontra as tags que serão utilizadas
        id = self.xmldoc.getElementsByTagName('CURRICULO-VITAE')
        dados = self.xmldoc.getElementsByTagName('DADOS-GERAIS')
        resumo = self.xmldoc.getElementsByTagName('RESUMO-CV')
        idiomas = self.xmldoc.getElementsByTagName('IDIOMAS')[0].getElementsByTagName('IDIOMA')
        artigos = self.xmldoc.getElementsByTagName('ARTIGOS-PUBLICADOS')[0].getElementsByTagName('ARTIGO-PUBLICADO')
        # adiciona os elementos necessarios no dict de resposta
        self.response['id'] = id[0].attributes['NUMERO-IDENTIFICADOR'].value
        self.response['nome'] = dados[0].attributes['NOME-COMPLETO'].value
        self.response['resumo'] = resumo[0].attributes['TEXTO-RESUMO-CV-RH'].value.encode('utf-8')
        self.response['artigos'] = len(artigos)
        self.response['idiomas'] = len(idiomas)
        # retorno o dict response
        return self.response

    def create_xml(self):
        """Método que cria output."""
        cnpq = self.parse_xml()
        # cria arquivo saida.xml
        output = open('saida.xml', 'w')
        # popula output e fecha
        output.write(
            '<add>\n'\
            '\t<doc>\n'\
            '\t\t<field name="NUMERO-IDENTIFICADOR">'+cnpq["id"]+'</field>\n'\
            '\t\t<field name="NOME-COMPLETO">'+cnpq["nome"]+'</field>\n'\
            '\t\t<field name="TEXTO-RESUMO-CV-RH">'+cnpq["resumo"]+'</field>\n'\
            '\t\t<field name="numero_artigos">'+str(cnpq["artigos"])+'</field>\n'\
            '\t\t<field name="numero_idiomas">'+str(cnpq["idiomas"])+'</field>\n'\
            '\t<doc>\n'\
            '<add>'
        )
        output.close
        return '\033[1;31mATENÇÃO:\033[0;0m O arquivo saida.json foi criado na pasta raíz.'



x = Parser()
print(x.create_xml())
