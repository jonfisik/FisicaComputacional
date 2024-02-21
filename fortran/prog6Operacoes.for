!! Jonatan P. Paschoals
!! 04 de fev de 2024.
!! Operações básicas aritiméticas
!!-----------------------------------------
	PROGRAM operacoes_basicas
	IMPLICIT NONE
	
	INTEGER :: num1, num2, resultado
	
	WRITE(*,*) '-------------------------------------'
	WRITE(*,*) 'Para as operções digite, '
	WRITE(*,*) 'O primeiro número >>> '
	READ(*,*) num1
	WRITE(*,*) 'O segundo número >>> '
	READ(*,*) num2
	
	WRITE(*,*) '-------------------------------------'
	
	resultado = num1+num2
	WRITE(*,*) 'Soma >>> ', resultado
	
	resultado = num1-num2
	WRITE(*,*) 'Subtração >>> ', resultado
	
	resultado = num1*num2
	WRITE(*,*) 'Multiplicação >>> ', resultado
	
	resultado = num1/num2
	WRITE(*,*) 'Divisão >>> ', resultado
	
	WRITE(*,*) 'Divisão REAL >>> ', num1/REAL(num2)
	
	resultado = num1**num2
	WRITE(*,*) 'Exponenciação >>> ', resultado
	
	WRITE(*,*) 'Expressão >>> ', num1+num2*num1-num2**num1/2.0
	WRITE(*,*) 'Expressão >>> ', (num1+num2)*num1-num2**num1/2.0	
	
	WRITE(*,*) 'Resto da divisão inteira >>> ', MOD(num1,num2)
	
	WRITE(*,*) '-------------------------------------'
	
	END PROGRAM operacoes_basicas
