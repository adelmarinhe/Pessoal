package exception;

public class SaldoInsuficienteException extends Exception {

	public SaldoInsuficienteException(String msg, double saldo, double valor) {
		super(msg+" [saldo = "+saldo+"]"+"[valor da tentativa do debito = "+valor+"]");
	}

}
