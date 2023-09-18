package main;

import java.util.ArrayList;

import conta.Conta;
import conta.ContaCorrente;
import conta.Poupanca;
import conta.PoupancaEsp;

public class ClasseContaAbstrata {

	public static void main(String[] args) {
		ContaCorrente c1 = new ContaCorrente("123-x", 1000);
		ContaCorrente c2 = new ContaCorrente("124-x", 1000);
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
		ClasseContaAbstrata.printDetailsAllContas(contas);
		System.out.println();
		System.out.println();
		ClasseContaAbstrata.renderJuros(contas);
		System.out.println(">>>>>>>>>>Rendeu Juros!<<<<<<<<<<");
		System.out.println();
		System.out.println();
		ClasseContaAbstrata.printDetailsAllContas(contas);
		System.out.println();
		System.out.println();
		System.out.println(">>>>>>>>>>Debitando Taxa Manutencao de Conta!<<<<<<<<<<");
		System.out.println();
		System.out.println();
		ClasseContaAbstrata.debitarTaxaManutencao(contas);
		ClasseContaAbstrata.printDetailsAllContas(contas);
		System.out.println("### Saldo Total Banco = "+ClasseContaAbstrata.getSaldoBanco(contas));
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
		public static void debitarTaxaManutencao(Conta [] contas) {
			for (int i = 0; i < contas.length; i++) {
				if(contas[i] instanceof ContaCorrente) {
					contas[i].debitar(ContaCorrente.taxa);
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
