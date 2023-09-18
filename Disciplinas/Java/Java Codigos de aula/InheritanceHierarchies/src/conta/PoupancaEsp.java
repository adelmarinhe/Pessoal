package conta;

public class PoupancaEsp extends Poupanca {
	
	public PoupancaEsp(String numero, double saldoInicial) {
		super(numero, saldoInicial);
	}
	
	public PoupancaEsp(String numero) {
		super(numero);
	}

	@Override
	public void renderJuros(double taxa) {
		double juros = (this.getSaldo() * (taxa + 0.10));
		this.creditar(juros);
	}
	
	public void renderJurosPadrao(double taxa) {
		super.renderJuros(taxa);
	}
}
