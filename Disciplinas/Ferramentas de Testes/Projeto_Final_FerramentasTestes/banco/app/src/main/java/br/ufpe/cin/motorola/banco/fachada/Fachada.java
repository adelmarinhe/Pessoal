package br.ufpe.cin.motorola.banco.fachada;

import br.ufpe.cin.motorola.banco.cliente.*;
import br.ufpe.cin.motorola.banco.conta.*;
import br.ufpe.cin.motorola.banco.excecoes.*;

public class Fachada {

	private static Fachada instancia;

	private CadastroContas contas;

	private CadastroClientes clientes;

	private Fachada() {
		initCadastros();
	}

	private void initCadastros() {
		IRepositorioContas rep = new RepositorioContasArray();
		contas = new CadastroContas(rep);
		IRepositorioClientes repClientes = new RepositorioClientesArray();
		clientes = new CadastroClientes(repClientes);
	}

	public static Fachada obterInstancia() {
		if (instancia == null) {
			instancia = new Fachada();
		}
		return instancia;
	}

	public void atualizar(Cliente c) throws ClienteInexistenteException {
		clientes.atualizar(c);
	}

	public Cliente procurarCliente(String cpf) throws ClienteInexistenteException {
		return clientes.procurar(cpf);
	}

	public void cadastrar(Cliente c) throws ClienteExistenteException {
		clientes.cadastrar(c);
	}

	public void descadastrarCliente(String cpf) throws ClienteInexistenteException {
		clientes.descadastrar(cpf);
	}

	public void atualizar(ContaAbstrata c) throws ContaInexistenteException {
		contas.atualizar(c);
	}

	public ContaAbstrata procurarConta(String n) throws ContaInexistenteException {
		return contas.procurar(n);
	}

	public void cadastrar(ContaAbstrata c) throws ContaExistenteException, ClienteInexistenteException, ClienteInvalidoException {
		Cliente cli = c.getCliente();
		if (cli != null) {
			clientes.procurar(cli.getCpf());
			//inseri o contas que nao estava sendo chamada aqui abaixo
			contas.cadastrar(c);
		} else {
			throw new ClienteInvalidoException();
		}
	}

	public void descadastrarConta(String n) throws ContaInexistenteException {
		contas.remover(n);
	}

	public void creditar(String n, double v) throws ContaInexistenteException {
		contas.creditar(n, v);
	}

	public void debitar(String n, double v) throws ContaInexistenteException, SaldoInsuficienteException {
		contas.debitar(n, v);
	}

	public void transferir(String origem, String destino, double val) throws ContaInexistenteException, SaldoInsuficienteException {
		contas.transferir(origem, destino, val);
	}
}