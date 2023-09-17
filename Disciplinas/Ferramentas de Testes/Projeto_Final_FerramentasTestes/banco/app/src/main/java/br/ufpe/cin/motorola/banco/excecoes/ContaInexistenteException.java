package br.ufpe.cin.motorola.banco.excecoes;
public class ContaInexistenteException extends BancoException {
	public ContaInexistenteException() {
		super("Conta Inexistente!");
	}
	private double saldo;
	//...
}
