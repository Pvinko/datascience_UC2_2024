# Biblioteca SpaCy
# Biblioteca para Processamento de linguagem natural
# pip istall spacy
# doanload do modelo de linguagem PT_BR
# pyhton -m spacy download pt_core_news_sm

import spacy
import spacy.displacy

# carregando o modelo de linguagem
# nlp ou pln
spacyPT = spacy.load('pt_core_news_sm')

# processamento de texto
frase = spacyPT('Eu vi o menino com o telescópio')
frase1 = spacyPT('Eu vi o menino que carregava o telescópio')
frase2 = spacyPT('Luiz bebeu água, porém continua feio')
print(frase)

# Cada frase é uma sequência de tokens,
# token é cada classe da palavra
# e nós podemos itera sobre cada token
# TOKENIZAR
for token in frase:
    print(token)

# Exibir as categorias morfossintáticas de cada token
# pos_ -> Part of speech
for token in frase:
    print(f'{token.text}:{token.pos_}')

# Visualizar as dependências das categorias morfossintáticas
spacy.displacy.serve([frase,frase1,frase2], style='dep')

