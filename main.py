# Define um caso com sintomas e diagnóstico
class Caso:
    def __init__(self, sintomas, diagnostico):
        self.sintomas = sintomas
        self.diagnostico = diagnostico

# Base de Casos: armazena todos os casos conhecidos
class BaseDeCasos:
    def __init__(self):
        self.casos = []

    def adicionar_caso(self, caso):
        self.casos.append(caso)

    def encontrar_mais_semelhante(self, novos_sintomas):
        melhor_caso = None
        maior_similaridade = -1

        for caso in self.casos:
            similaridade = self.calcular_similaridade(caso.sintomas, novos_sintomas)
            if similaridade > maior_similaridade:
                maior_similaridade = similaridade
                melhor_caso = caso

        return melhor_caso

    def calcular_similaridade(self, sintomas1, sintomas2):
        """
        Similaridade simples: +10 para cada sintoma que coincide.
        Para temperatura, quanto menor a diferença, maior a pontuação.
        """
        pontuacao = 0

        for chave in sintomas1:
            if chave not in sintomas2:
                continue

            valor1 = sintomas1[chave]
            valor2 = sintomas2[chave]

            if isinstance(valor1, (int, float)) and isinstance(valor2, (int, float)):
                # Similaridade inversamente proporcional à diferença de temperatura
                pontuacao += max(0, 10 - abs(valor1 - valor2))
            elif valor1 == valor2:
                pontuacao += 10  # Sintomas categóricos iguais

        return pontuacao

# Raciocínio Baseado em Casos
class RBC:
    def __init__(self):
        self.base = BaseDeCasos()

    def adicionar_caso(self, sintomas, diagnostico):
        caso = Caso(sintomas, diagnostico)
        self.base.adicionar_caso(caso)

    def diagnosticar(self, novos_sintomas):
        caso_semelhante = self.base.encontrar_mais_semelhante(novos_sintomas)
        if caso_semelhante:
            print("Caso mais semelhante encontrado:", caso_semelhante.sintomas)
            print("Diagnóstico sugerido com base no caso semelhante:", caso_semelhante.diagnostico)
            return caso_semelhante.diagnostico
        else:
            print("Nenhum caso semelhante encontrado.")
            return None

# -------------------------------
# Exemplo de uso
# -------------------------------
if __name__ == "__main__":
    sistema = RBC()

    # Preenche a base de casos
    sistema.adicionar_caso({'temperatura': 38.5, 'tosse': 'sim', 'dor_de_cabeca': 'sim', 'espirros': 'nao'}, 'Gripe')
    sistema.adicionar_caso({'temperatura': 37.0, 'tosse': 'nao', 'dor_de_cabeca': 'nao', 'espirros': 'nao'}, 'Saudável')
    sistema.adicionar_caso({'temperatura': 39.0, 'tosse': 'sim', 'dor_de_cabeca': 'nao', 'espirros': 'nao'}, 'COVID-19')
    sistema.adicionar_caso({'temperatura': 36.5, 'tosse': 'nao', 'dor_de_cabeca': 'sim', 'espirros': 'nao'}, 'Enxaqueca')
    sistema.adicionar_caso({'temperatura': 37.5, 'tosse': 'nao', 'dor_de_cabeca': 'nao', 'espirros': 'sim'}, 'Alergia')

    # Novo caso
    novo_paciente = {'temperatura': 37.4, 'tosse': 'nao', 'dor_de_cabeca': 'nao', 'espirros': 'nao'}

    diagnostico = sistema.diagnosticar(novo_paciente)
