package br.ufpe.cin.motorola.banco.cliente;

public class Cliente {

	private String cpf;

	private String nome;

	private TipoCliente tipo;

	public Cliente(String newCpf, String newNome, TipoCliente newTipo) {
		this.cpf = newCpf;
		this.nome = newNome;
		this.tipo = newTipo;
	}

	public String getCpf() {
		return cpf;
	}

	public String getNome() {
		return nome;
	}

	public TipoCliente getTipo() {
		return tipo;
	}

	public boolean setCpf(String newCpf) {
		cpf = newCpf;
		return true;
	}

	public boolean setNome(String newNome) {
		nome = newNome;
		return true;
	}

	public boolean setTipo(TipoCliente newtipo) {
		this.tipo = newtipo;
		return true;
	}
}