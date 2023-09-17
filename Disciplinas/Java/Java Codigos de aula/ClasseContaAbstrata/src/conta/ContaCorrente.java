package conta;

public class ContaCorrente extends Conta{
	
	public static final double taxa = 12.00;

	public ContaCorrente(String numero) {
		super(numero);
	}
	
	public ContaCorrente(String numero, double saldo) {
		super(numero, saldo);
	}
	
	@Override
	public String toString() {
		return "ContaCorrente[numero = "+this.getNumero()+", saldo = "+this.getSaldo()+"]";
	}
}
