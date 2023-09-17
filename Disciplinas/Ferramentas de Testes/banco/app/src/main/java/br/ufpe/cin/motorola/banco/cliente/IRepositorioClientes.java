package br.ufpe.cin.motorola.banco.cliente;

import br.ufpe.cin.motorola.banco.excecoes.ClienteInexistenteException;

import java.util.List;

public interface IRepositorioClientes {

	void atualizar(Cliente c) throws ClienteInexistenteException;

	boolean existe(String cpf);

	void inserir(Cliente c);

	Cliente procurar(String cpf) throws ClienteInexistenteException;

	void remover(String cpf) throws ClienteInexistenteException;

	List<Cliente> listar();

}