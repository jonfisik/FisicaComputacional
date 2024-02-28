subroutine prog16subrotina(a,b,c)
	use prog16modulo, only: dp
	implicit none
	real(dp) :: a,b,c
	
	c=a+b
	a=10
	b=10
	
	return
	
end subroutine prog16subrotina