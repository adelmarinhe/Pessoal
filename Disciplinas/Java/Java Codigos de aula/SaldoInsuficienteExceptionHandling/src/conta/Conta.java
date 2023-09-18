	package conta;

import exception.NegativeValueException;
import exception.SaldoInsuficienteException;

public class Conta {
	
	private String numero;
	private double saldo;
	
	public Conta(String numero, double saldo) {
		this.numero = numero;
		this.saldo = saldo;
	}
	
//	public Conta(String numero) {
//		this.numero = numero;
//		this.saldo = 0; nao eh necessario pq o valor default ja faz isso [ou seja = 0]
//	}

	public Conta(String numero) {
		this(numero, 0.0); // chama o construtor Conta(String, double);
	}

	public void creditar(double valor) {
		this.saldo = this.saldo + valor;
	}
	
	public void debitar(double valor) throws SaldoInsuficienteException, NegativeValueException {
		if(valor < 0) {
			throw new NegativeValueException("valor = "+valor+" cannot be negative!!");
		}
		if(this.saldo >= valor) {
			this.saldo -= valor;
		}
		else {
			throw new SaldoInsuficienteException("Saldo Insuficiente!", this.saldo, valor);
		}
	}

	public String getNumero() {
		return numero;
	}

	public double getSaldo() {
		return saldo;
	}
	
	public void printDetailsConta() {
		System.out.println("*********************************************");
		System.out.println("Conta = "+this);
		System.out.println("*********************************************");
	}
	
	@Override
	public String toString() {
		return "Conta[numero = "+this.numero+", saldo = "+this.saldo+"]";
	}
}
