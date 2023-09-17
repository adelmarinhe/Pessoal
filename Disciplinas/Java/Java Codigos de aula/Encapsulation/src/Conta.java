	
public class Conta {
	
	private String numero;
	double saldo;
	private boolean isChequeEspecial;
	
	public Conta(String numero, double saldo) {
		this.numero = numero;
		this.saldo = saldo;
	}

	public Conta(String numero) {
		this(numero, 0.0); // chama o construtor Conta(String, double);
	}

	public void creditar(double valor) {
		if(valor >= 0) {
			this.saldo = this.saldo + valor;
		}
		else {
			System.out.println("Valor a ser creditado negativo!");
		}
	}
	
	public void debitar(double valor) { 
		if(this.isChequeEspecial()) {
			if(valor <= this.getSaldo()+2000) {
				this.saldo -= valor;
			}
			else {
				System.out.println("Saldo insuficiente! [ultrapassou limite do cheque especial que eh: R$2.000,00]");
			}
		}
		else {
			if(valor <= this.getSaldo()) {
				this.saldo -= valor;
			}
			else {
				System.out.println("Saldo insuficiente!");
			}
		}
	}

	public String getNumero() {
		return numero;
	}

	public double getSaldo() {
		return saldo;
	}
	
	public boolean isChequeEspecial() {
		return isChequeEspecial;
	}

	public void setChequeEspecial(boolean isChequeEspecial) {
		this.isChequeEspecial = isChequeEspecial;
	}

	public void printSaldo() {
		System.out.println("numero = "+this.numero);
		System.out.println("saldo = "+this.saldo);
	}
	
	@Override
	public String toString() {
		return "Conta[numero = "+this.numero+", saldo = "+this.saldo+"]";
	}
}
