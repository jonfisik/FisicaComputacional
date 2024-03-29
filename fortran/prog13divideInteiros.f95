!! Jonatan P. Paschoal
!! 23 de fev de 2024.
!! Programa: Dividir números inteiros, 
!! informados pelo teclado. Com saída de dados.
!! É proibido a aritmética de modo mista de variáveis.
!!-----------------------------------------
	PROGRAM divideInt
	IMPLICIT NONE

	INTEGER :: i, j !! entrada
	REAL :: x !! resultado divisão
	
	OPEN(unit=3, file="divideInt.txt")
	
	WRITE(*,*) '--------------------------------------------------------'
	WRITE(*,*) '- Digite valores inteiros i e j, separados por vírgula -'
	WRITE(*,*) ' '

	READ(*,*) i, j
	
	x = i/j !! Execução
	
	WRITE(*,*) ' '
	WRITE(*,*) 'Quociente de ', i,' por ', j, ' >>> ', x
	WRITE(3,*) 'Quociente de ', i,' por ', j, ' >>> ', x
	
	WRITE(*,*) '--------------------------------------------------------'
	
	! Stop !! Opcional
			
	END PROGRAM divideInt
