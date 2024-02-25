! Autor: Jonatan Paschoal
! Data: 01 - mar - 2023
! Teorema de pitágoras (Dado - b e c, a = ?; a²=b²+c²)
       program pitagoras
       implicit none
       real a,b,c ! ou real:: a,b,c
       b=6.
       c=8.
       a=b*b+c*c ! a=b**2.+c**2.
!       a=a**(0.5)! a =sqrt(a) ou a=sqrt(b**2.+c**2.)
       a =sqrt(a)       
       write(*,*)">>>", a
       end program pitagoras
