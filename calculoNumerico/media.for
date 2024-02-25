! Autor: Jonatan Paschoal
! Data: 27 - fev - 2023
! Calculo de média simples - "M = (A+B)/2"
       program media
       implicit none

       real:: A,B,M

       A=15. ! ou 15.0
       B=10. ! ou 10.0

       M=(A+B)/2

       write(*,*)"Media >>> ", M

       end program media
