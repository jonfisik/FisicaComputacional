!! Jonatan P. Paschoals
!! 04 de fev de 2024.
!! Função WRITE(unid,formato) lista-de-intens
!! Descritores de formato - (,), (tipo_dados,formatacao)
!! Ex.) WRITE(*,'(A,F12.5,1X,E12.5)') 'Valor >>> ', X,Y
!! Ex.) WRITE(tela,label "endereço") valor --> WRITE(*,10)
!! 10 FORMAT('O número é ', I3) --> I, inteiro 3, casas decimais 
!! Programa Formatação de dados Fortran
!!-----------------------------------------
	PROGRAM formatacao
	IMPLICIT NONE
	
		INTEGER :: polegada, n
		REAL    :: centimetro
		REAL, PARAMETER :: cent_polegada = 2.54
		
		WRITE(*,*) 'write(*,*) Tela, Fomato livre', NEW_LINE('A') !! Tela, tamanho avaliado pelo fortran
		WRITE(*,'(A)') 'Quanto vale uma polegada?' !! Descritor de caracter
		!! A-caracter, 1X-um espaço em branco, F4.2-ponto flutuante, 1X-um espaço em branco, A-caracter, /-quebra de linha
		WRITE(*,'(A, 1X, F4.2, 1X, A, /)') 'Uma polegada vale', cent_polegada, 'centimetros'
		WRITE(*, '(A)') 'Convensão de polegadas em centímetros'
		DO polegada = 1, 10
			centimetro = polegada * cent_polegada
			WRITE(*,110) polegada, centimetro
		END DO
		110 FORMAT(I3, ' polegada = ', F6.2, ' centimetros.')
		
		WRITE(*, '(A)') '-------------------------------------------------'
		
		WRITE(*, '(A)') 'Convensão de polegadas em cm com entrada de dados'
		WRITE(*, '(A)') 'Digite quantos valores deseja converter?'
		READ (*,*) n
		DO polegada = 1, n
			centimetro = polegada * cent_polegada
			WRITE(*,120) polegada, centimetro
		END DO
		
		120 FORMAT(I3, ' polegada = ', F6.2, ' centimetros.')
		
		WRITE(*, '(A)') '-------------------------------------------------'
		
	END PROGRAM formatacao
