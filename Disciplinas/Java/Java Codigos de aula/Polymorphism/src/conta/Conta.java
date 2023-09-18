package conta;

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
	
	public void debitar(double valor) {
		this.saldo -= valor;
	}

	public String getNumero() {
		return numero;
	}

	public double getSaldo() {
		return saldo;
	}
	
	public void printDetailsConta() {
		System.out.println("************************");
		System.out.println("Conta = "+this);
		System.out.println("************************");
	}
	
	@Override
	public String toString() {
		return "Conta[numero = "+this.numero+", saldo = "+this.saldo+"]";
	}
}
