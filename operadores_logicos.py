idade = 15
altura = 1.75

resultado = (idade >= 18) and (altura >= 1.70)
msg = 'Pode participar do evento ? ' + str(resultado)

print(msg)

# Programa de disparo de alarme:
porta = 'aberta'
janela = 'fechada'

alarme = (porta == 'aberta') or (janela == 'aberta')
msg = 'Alarme disparou ? ' + str(alarme)
print(msg)

# Fazer compra

tem_dinheiro = True
tem_dinheiro = not tem_dinheiro
msg = 'Tem dinheiro? ' + str(tem_dinheiro)
print(msg)