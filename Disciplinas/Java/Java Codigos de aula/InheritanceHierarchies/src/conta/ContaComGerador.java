package conta;

public class ContaComGerador {
	
	private int numero;
	private double saldo;
	private static int proximo;
	
	private static int x;
	
	public static void inc() {
		ContaComGerador.x++;
	}
	
	public static int getX() {
		return ContaComGerador.x;
	}

	public ContaComGerador() {
		this(0.0);
	}
	
	public ContaComGerador(double valorInicial) {
		this.numero = ContaComGerador.getProximo();
		this.saldo = valorInicial;
	}
	
	// helper method
	private static int getProximo() {
		return ++ContaComGerador.proximo;
	}

	public void creditar(double valor) {
		this.saldo = this.saldo + valor;
	}
	
	public void debitar(double valor) {
		this.saldo -= valor;
	}

	public double getSaldo() {
		return saldo;
	}
	
	public void printSaldo() {
		System.out.println("************************");
		System.out.println("Conta [ref] = "+this);
		System.out.println("numero = "+this.numero);
		System.out.println("saldo = "+this.saldo);
		System.out.println("************************");
	}
}
