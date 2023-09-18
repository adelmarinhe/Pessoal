package main;

import conta.ContaComGerador;

public class InstanceXStaticMembers {

	public static void main(String[] args) {			
		ContaComGerador c1 = new ContaComGerador(500);
		c1.creditar(500);
        c1.printSaldo();
                        
        ContaComGerador c2 = new ContaComGerador();
        double valor = 1000;
        c2.creditar(valor);
        c2.printSaldo();
        
        ContaComGerador c3 = new ContaComGerador();
        c3.printSaldo();        
        
        c1.x++;
        System.out.println(c2.x);
        
        ContaComGerador.x++;
        System.out.println(ContaComGerador.x);
        
        c1.y++;
        System.out.println(c1.y);
        System.out.println(c2.y);
	}
}
