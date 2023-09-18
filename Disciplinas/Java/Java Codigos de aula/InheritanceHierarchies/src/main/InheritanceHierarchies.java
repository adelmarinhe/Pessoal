package main;

import java.util.ArrayList;

import conta.Conta;
import conta.Poupanca;
import conta.PoupancaEsp;

public class InheritanceHierarchies {

	public static void main(String[] args) {
		Conta c1 = new Conta("123-x", 1000);
		Conta c2 = new Conta("124-x", 1000);
		c1.debitar(500);
		c2.debitar(250);
		c1.printDetailsConta();
		c2.printDetailsConta();
		System.out.println();
		System.out.println();
		
		Poupanca p1 = new Poupanca("125-x", 1000);
		Poupanca p2 = new Poupanca("126-x", 1000);
		p1.renderJuros(0.01);
		p2.renderJuros(0.01);
		p1.printDetailsConta();
		p2.printDetailsConta();
		System.out.println();
		System.out.println();
		
		PoupancaEsp pe1 = new PoupancaEsp("127-x", 1000);
		Conta pe2 = new PoupancaEsp("128-x", 1000);
		pe1.renderJurosPadrao(0.01);
		((Poupanca)pe2).renderJuros(0.01);
		pe1.printDetailsConta();
		pe2.printDetailsConta();
		
//		ArrayList<Conta> list = new ArrayList<>();
//		list.add(pe1);
	}
}
