# 2) Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente,
# ignorando espaços e pontuação). Se o resultado é True, responda "sim", se o resultado for False, responda "Não".


def eh_palindromo(texto):
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
    
    if texto_limpo == texto_limpo[::-1]:
        return "sim"
    else:
        return "Não"

print(eh_palindromo("Ame a ema"))