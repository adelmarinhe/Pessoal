package br.ufpe.cin.motorola.banco.excecoes;
public class ClienteInvalidoException extends BancoException {
	public ClienteInvalidoException() {
		super("Cliente invalido!");
	}
	private double saldo;
	//...
}
