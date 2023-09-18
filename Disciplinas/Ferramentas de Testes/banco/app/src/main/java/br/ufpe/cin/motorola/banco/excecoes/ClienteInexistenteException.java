package br.ufpe.cin.motorola.banco.excecoes;
public class ClienteInexistenteException extends BancoException {
	public ClienteInexistenteException() {
		super("Cliente inexistente!");
	}
	private double saldo;
	//...
}
