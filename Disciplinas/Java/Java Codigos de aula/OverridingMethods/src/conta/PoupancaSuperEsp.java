package conta;

public class PoupancaSuperEsp extends Poupanca {
	
	public PoupancaSuperEsp(String numero, double saldoInicial) {
		super(numero, saldoInicial);
	}
	
	public PoupancaSuperEsp(String numero) {
		super(numero);
	}

	@Override
	public void renderJuros(double taxa) {
		double juros = (this.getSaldo() * (taxa + 0.10));
		this.creditar(juros);
	}
	
	@Override
	public String toString() {
		return this.getClass().getName()+"[numero = "+this.getNumero()+", saldo = "+this.getSaldo()+"]";
	}
}
