package conta;

public class ContaComGerador {
	
	private int numero; // instance field
	private double saldo; // instance field
	private static int proximo; // class field [static]
	
	public static int x = 0; // class field [static]
	public int y = 0; // instance field

	public ContaComGerador() {
		this(0.0);
	}
	
	public ContaComGerador(double valorInicial) {
		this.numero = ContaComGerador.getProximo();
		this.saldo = valorInicial;
	}
	
	// helper method
	private static int getProximo() {
		return ++ContaComGerador.proximo; // ContaComGerador.proximo = ContaComGerador.proximo + 1;
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
