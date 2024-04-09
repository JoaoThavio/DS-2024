programa {
	funcao inicio() {
		real numero_1
		real numero_2
		real resultado
		real soma

		escreva("informe sua altura em metros: ")
		leia(numero_1)

		escreva("informe seu peso em kg: ")
		leia(numero_2)

		soma = numero_1 * numero_1

		resultado = numero_2/ soma 

		se(resultado >= 30){
			escreva("Cuidado com a saude")
		}senao{
			escreva("Tudo OK")
		}

		escreva("\no seu IMC é igual a: ", resultado)
		escreva("\naltura informada: ", numero_1)
		escreva("\npeso informado: ", numero_2)
	}
}


/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 506; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */