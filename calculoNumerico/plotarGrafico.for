! Autor: Jonatan Paschoal
! Data: 01 - mar - 2023
! Plotando Gráfico (y = x + 1)

       program grafico
       implicit none

       integer x,y ! ou integer:: x,y
       open(3,file="grafico.dat")
       
       do x=0,20,1 !(início,fim,passo)
       
       y=x+1
	   
       write(3,*) x,y
       write(*,*) x,y       
       enddo    
	   
       end program grafico
