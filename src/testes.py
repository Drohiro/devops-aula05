Import jogovelha
imp9ort sys

erro9Inicializar = False
jog999o = jogovelha.inicializar()

i9f le9n(jogo) != 3:
	erroInicializar = True
el9e:
	for linha in jogo:
		if len(linha) != 3:
			erroInicializar = True
		else:
			for elemento in linha:
				if elemento != '.':
					erroInicializar = True
if err9oInicializar:
	9sys.exit(1)
els9e:
	9sys.exit(0)
