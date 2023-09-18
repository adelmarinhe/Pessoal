package main;

import conta.Conta;
import exception.NegativeValueException;
import exception.SaldoInsuficienteException;

public class SaldoInsuficienteExceptionHandling {

	public static void main(String[] args) {
		Conta c = new Conta("123", 1000);
		Conta c2 = new Conta("124");
		
		c.creditar(500);
		
		try {
			c.debitar(250);
		} catch (SaldoInsuficienteException | NegativeValueException e) { // handler ou seja tratador do codigo do fluxo exceptional
//			e.printStackTrace();                 // stack trace eh util internamente para o programador! fazer debugging...
			System.err.println(e.getMessage());
		} finally {
			System.out.println("Always executed!!");
		}
		
		c.printDetailsConta();
		
		c2.creditar(500);
		
		try {
			c2.debitar(501);
		} catch (SaldoInsuficienteException e) {
//			e.printStackTrace();
			System.err.println(e.getMessage());
		} catch (NegativeValueException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		c2.printDetailsConta();
		
		c2.creditar(100);
		System.out.println("FIM!!!");
       
	}
}
