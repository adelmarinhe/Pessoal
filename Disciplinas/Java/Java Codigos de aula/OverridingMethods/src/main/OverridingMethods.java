package main;

import conta.Conta;
import conta.Poupanca;
import conta.PoupancaSuperEsp;

public class OverridingMethods {

	public static void main(String[] args) {
		Conta c1 = new Conta("123-x", 1000);
		Conta c2 = new Conta("124-x", 1000);
		c1.debitar(500);
		c2.debitar(250);
		c1.printDetailsConta();
		c2.printDetailsConta();
//		System.out.println(c1);
//		System.out.println(c1.toString());
//		System.out.println(c2);
//		System.out.println(c2.toString());
		
		Poupanca p1 = new Poupanca("125-x", 1000);
		Poupanca p2 = new Poupanca("126-x", 1000);
		p1.renderJuros(0.01);
		p2.renderJuros(0.01);
		p1.printDetailsConta();
		p2.printDetailsConta();
//		System.out.println(p1);
//		System.out.println(p1.toString());
//		System.out.println(p2);
//		System.out.println(p2.toString());
		
		PoupancaSuperEsp pe1 = new PoupancaSuperEsp("127-x", 1000);
		PoupancaSuperEsp pe2 = new PoupancaSuperEsp("128-x", 1000);
		pe1.renderJuros(0.01);
		pe2.renderJuros(0.01);
		pe1.printDetailsConta();
		pe2.printDetailsConta();
//		System.out.println(pe1);
//		System.out.println(pe1.toString());
//		System.out.println(pe2);
//		System.out.println(pe2.toString());
	}
}
