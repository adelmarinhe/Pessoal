package main;

import java.util.ArrayList;
import java.util.Iterator;

import conta.Conta;
import conta.Poupanca;
import conta.PoupancaEsp;

public class Polymorphism {

	public static void main(String[] args) {
		Conta c1 = new Conta("123-x", 1000);
		Conta c2 = new Conta("124-x", 1000);
		ArrayList<Conta> list = new ArrayList<>();
		
		Poupanca p1 = new Poupanca("125-x", 1000);
		Poupanca p2 = new Poupanca("126-x", 1000);
		
		Conta c3 = new Poupanca("127-x", 1000);
//		c3.creditar(100);
//		System.out.println("c3 = "+c3.toString()); // execucao do metodo sempre esta associado 
		                                           // ao objeto! ou seja tipo dinamico!
//		((Poupanca)c3).renderJuros(0.01);
		
		PoupancaEsp pe1 = new PoupancaEsp("127-x", 1000);
		
		// Array of contas
		Conta [] contas = {c1, c2, p1, p2, c3, pe1};
		Polymorphism.printDetailsAllContas(contas);
		System.out.println();
		System.out.println();
		Polymorphism.renderJuros(contas);
		System.out.println(">>>>>>>>>>Rendeu Juros!<<<<<<<<<<");
		System.out.println();
		System.out.println();
		Polymorphism.printDetailsAllContas(contas);
		System.out.println("### Saldo Total Banco = "+Polymorphism.getSaldoBanco(contas));
	}
	
	// polymorphic method
	public static void printDetailsAllContas(Conta [] contas) {
		for (int i = 0; i < contas.length; i++) {
			contas[i].printDetailsConta();
		}
	}
	
	// polymorphic method
	public static void renderJuros(Conta [] contas) {
		for (int i = 0; i < contas.length; i++) {
			if(contas[i] instanceof Poupanca) {
				((Poupanca)contas[i]).renderJuros(0.01);
			}
		}
	}
	
	// polymorphic method
	public static double getSaldoBanco(Conta [] contas) { // reuso por polimorfismo!
		double sum = 0;
		for (int i = 0; i < contas.length; i++) {
			sum += contas[i].getSaldo();
		}
		return sum;
	}

}
