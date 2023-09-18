package br.ufpe.cin.motorola.banco.cliente;

import br.ufpe.cin.motorola.banco.excecoes.ClienteExistenteException;
import br.ufpe.cin.motorola.banco.excecoes.ClienteInexistenteException;

public class CadastroClientes {
	private IRepositorioClientes clientes;

	public CadastroClientes(IRepositorioClientes rep) {
		this.clientes = rep;
	}

	public void atualizar(Cliente c) throws ClienteInexistenteException {
		clientes.atualizar(c);
	}

	public void cadastrar(Cliente c) throws ClienteExistenteException {
		String cpf = c.getCpf();
		if (!clientes.existe(cpf)) {
			clientes.inserir(c);
		} else {
			throw new ClienteExistenteException();
		}
	}

	public void descadastrar(String cpf) throws ClienteInexistenteException {

		clientes.remover(cpf);

	}

	public Cliente procurar(String cpf) throws ClienteInexistenteException {
		return clientes.procurar(cpf);
	}
}