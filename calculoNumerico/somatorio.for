! Autor: Jonatan Paschoal
! Data: 01 - mar - 2023
! Somatorio (S = x1 + x2 + x3 + x4; S = xi, i=1,2,3,4...)
       program somatorio
       implicit none

       integer:: i,S
       S=0 
       do i=1,4
          S=S + i  
		  
		  write(*,*) S
		  
       enddo  
       
       write(*,*)"Soma", S

       end program somatorio
