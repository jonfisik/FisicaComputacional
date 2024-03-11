!! Jonatan P. Paschoal
!! 11 de mar de 2024.
!! Programa: eq. 2 grau -- ax**2+b*x+c=0
!! 
!!-----------------------------------------
	PROGRAM segundoGrau
		IMPLICIT NONE
		!! a,b,c - coefieciente da eq.
		!! discr - discriminante
		!! raiz1, raiz2 - raizes
		
		!! Declaracao variaveis
		real :: a,b,c,discr,raiz1,raiz2
		
		!! Entrada dos coefieciente da eq.
		write(*,*)"Digite os coefieciente da equacao >>> "
		read(*,*) a,b,c
		
		!! Calculo do discriminante
		discr=b**2-4.0*a*c
		
		!! Seleciona solucao a partir do discriminante
		
		!! discriminante > 0, 2 raizes reais 
		if(discr>0.0) then
			raiz1=(-b+sqrt(discr))/(2.0*a)
			raiz1=(-b-sqrt(discr))/(2.0*a)
			
			WRITE(*,*) '----------------------------'
			PRINT*, "Eq. posssui duas raizes reais."
			PRINT*, "x1 = ", raiz1
			PRINT*, "x2 = ", raiz2
			WRITE(*,*) '----------------------------'
		
		!! discriminante < 0, 2 raizes complexas
		else if(discr<0) then
			raiz1=-b/(2.0*a)
			raiz2=sqrt(abs(discr))/(2.0*a)
			
			WRITE(*,*) '-------------------------------'
			PRINT*, "Eq. posssui duas raizes complexas."
			PRINT*, "x1 = ", raiz1,"+i",raiz2
			PRINT*, "x2 = ", raiz1,"-i",raiz2
			WRITE(*,*) '-------------------------------'
			
		!! discriminante == 0
		else
			raiz1=-b/(2.0*a)
			
			WRITE(*,*) '-------------------------------'
			PRINT*, "Eq. posssui duas raizes iguais."
			PRINT*, "x1 = x2 = ",raiz1
			WRITE(*,*) '-------------------------------'
			
		end if
	END PROGRAM  segundoGrau