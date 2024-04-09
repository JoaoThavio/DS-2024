programa {
	funcao inicio() {
		real numero_1
		real numero_2
		real numero_3
		real soma 
		real resultado

		escreva("digite a nota do aluno: ")
		leia(numero_1)

		escreva("digite a nota do aluno: ")
		leia(numero_2)

		escreva("digite a nota do aluno: ")
		leia(numero_3)

		soma = numero_1 + numero_2 + numero_3

		resultado = soma / 3

          se(resultado >= 7){
          	escreva("APROVADO")
          }senao se(resultado >= 3){
          	escreva("RECUPERAÇÃO")
          }senao{
          	escreva("REPROVADO")
          }
		escreva("\na soma das notas é: ", soma," a media é: ", resultado)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 275; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */