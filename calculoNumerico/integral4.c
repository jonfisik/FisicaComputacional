// Autor - Jonatan P. Paschoal
// Data 25-fev-2024
// Integral dupla numerica
// I_retangulo ~ (b-a)*f[(a+b)/2] -- Retangulos
// I_trapezio ~ (b-a)*[(f(a)+f(b))/2] -- Trapezios
// I_simpson ~ (b-a)*[(f(a)+4f[(a+b)/2]f(b))/6] -- Media ponderada

#include<stdio.h>
#include<math.h>

int main(){
        double x,dx,y,dy;
        double IE,IN;
        double r1;
        
        dx=dy=5e-4;
        IN=0.;
                
        // f(x)=x²y³ --> ID = I(x²)I(y³)dxdy|^1_0
        
        for(x=0.;x<=(1.-dx);x=x+dx){ //for1

        	for(y=0.;y<=(1.-dy);y=y+dy){ //for2

        // Regra do trapezio
                	r1=(pow(x,2.))*(pow(y,3.))+(pow(x,2.))*(pow(y+dy,3.))+
                		(pow(x+dx,2.))*(pow(y,3.))+(pow(x+dx,2.))*(pow(y+dy,3.));
                	
                	r1=r1*dx*dy*0.25;
                
                	IN=IN+r1;
                
                printf("%20.10g \n", IN); // Integrais
                
        	} // fim for2        
        	
        } // fim for1
        
        // Integral exata
        IE=1./12.;
        printf("\n");
        printf("%20.10g %20.10g \n", IN,IE); // Integrais
        printf("\n");
        printf("%20.10g \n", fabs(IE-IN)); // Diferenca

        return 0;
}

