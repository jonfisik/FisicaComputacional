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
	
		REAL(KIND=16)   :: avogadro = 602214000000000000000000.0
		CHARACTER(8) :: av = 'AVOGADRO'
		
		WRITE(*,120) av
		120 FORMAT(10X, A)
		
		WRITE(*,130) avogadro
		130 FORMAT('Número de Avogadro >>> ', ES12.6)
		
	END PROGRAM formatacao
