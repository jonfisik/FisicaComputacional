!! jonatan paschoal
!! 03 de fev de   2025
!! Dividir dois números inteiros - aritmetica de modo misto
!! Não é recomendável essa operação

program divisaoInteiro

!! Declaracao variaveis

	integer :: num1, num2
	real :: x

!! Abertura de arquivo
	
	!! Cria arquivo de saida
	open(unit=3, file="saida_divide.txt")
	
!! Entrada de dados

	write(*,*)"Digite dois numeros inteiros (separdos por virgula) >> "
	write(*,*)" "
	read(*,*) num1,num2
	
!! Resultado

	x = num1/num2
	
	write(*,*) " "
	write(*,*)"Quociente de ",num1," por ",num2," = ", x
	write(3,*)"Quociente de ",num1," por ",num2," = ", x !! Escreve resultado no arquivo esterno
	
!! Parada

end program divisaoInteiro
