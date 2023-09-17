package br.ufpe.cin.residencia.banco.conta;

import androidx.annotation.WorkerThread;
import androidx.lifecycle.LiveData;
import java.util.List;


public class ContaRepository {
    private ContaDAO dao;
    private LiveData<List<Conta>> contas;

    public ContaRepository(ContaDAO dao) {
        this.dao = dao;
        this.contas = dao.contas();
    }

    //Obtém a lista de contas como LiveData
    public LiveData<List<Conta>> getContas() {
        return contas;
    }

    //Insere uma nova conta no banco de dados
    @WorkerThread
    public void inserir(Conta c) {
        dao.adicionar(c);
    }

    //Atualiza os dados de uma conta existente no banco de dados
    @WorkerThread
    public void atualizar(Conta c) {
        dao.upDateConta(c);
    }

    //Remove uma conta do banco de dados
    @WorkerThread
    public void remover(Conta c) {
        dao.deleteConta(c);
    }

    //Busca uma lista de contas pelo nome do cliente
    @WorkerThread
    public List<Conta> buscarPeloNome(String nomeCliente) {
        return dao.findListBynomeCliente(nomeCliente);
    }

    //Busca uma lista de contas pelo CPF do cliente
    @WorkerThread
    public List<Conta> buscarPeloCPF(String cpfCliente) {
        return  dao.findListBycpfCliente(cpfCliente);
    }

    //Busca uma lista de contas pelo número da conta
    @WorkerThread
    public List<Conta> buscarPeloNumero(String numeroConta) {
        return  dao.findListByNumero(numeroConta);
    }

    //Obtém o saldo total de todas as contas
    @WorkerThread
    public Double getSaldo() {
        return  dao.saldoTotal();
    }
}
