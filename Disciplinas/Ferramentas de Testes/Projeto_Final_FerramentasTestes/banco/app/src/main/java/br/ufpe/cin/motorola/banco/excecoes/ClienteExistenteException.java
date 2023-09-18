package br.ufpe.cin.motorola.banco.excecoes;
public class ClienteExistenteException extends BancoException {
	public ClienteExistenteException() {
		super("Cliente ja existe!");
	}
	private double saldo;
	//...
}
