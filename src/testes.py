Import jogovelha
import sys

erroInicializar = False
jogo = jogovelha.inicializar()

if len(jogo) != 3:
	erroInicializar = True
ele:
	for linha in jogo:
		if len(linha) != 3:
			erroInicializar = True
		else:
			for elemento in linha:
				if elemento != '.':
					erroInicializar = True
if erroInicializar:
	sys.exit(1)
els9e:
	sys.exit(0)
