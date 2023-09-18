package br.ufpe.cin.residencia.banco;

import android.app.Application;
import android.util.Log;

import androidx.annotation.NonNull;
import androidx.lifecycle.AndroidViewModel;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;

import java.util.ArrayList;
import java.util.List;

import br.ufpe.cin.residencia.banco.conta.Conta;
import br.ufpe.cin.residencia.banco.conta.ContaRepository;

//Ver anotações TODO no código
public class BancoViewModel extends AndroidViewModel {
    private ContaRepository repository;
    Double saldoTotal = 0.0;
    List<Conta> listConta;


    public BancoViewModel(@NonNull Application application) {
        super(application);
        this.repository = new ContaRepository(BancoDB.getDB(application).contaDAO());
    }

    //Usando o metodo transferir da classe Conta é feita a transferencia de saldo
    //E usando o metodo atualizar da classe ContaRepository é feita a atualização
    //de dados no banco de dados
    void transferir(String numeroContaOrigem, String numeroContaDestino, double valor) {
        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                Conta contaOrigem = BancoDB.getDB(getApplication()).contaDAO().findByNumero(numeroContaOrigem);
                Conta contaDestino = BancoDB.getDB(getApplication()).contaDAO().findByNumero(numeroContaDestino);

                contaOrigem.transferir(contaDestino, valor);
                new Thread(() -> repository.atualizar(contaOrigem)).start();
                new Thread(() -> repository.atualizar(contaDestino)).start();
            }
        });
        thread.start();
    }

    //Usando o metodo creditar da classe Conta é feita a adição do saldo
    //E usando o metodo atualizar da classe ContaRepository é feita a atualização
    //do saldo da conta no banco de dados
    void creditar(String numeroConta, double valor) {
        //TODO implementar creditar em conta (lembrar de salvar no BD o objeto Conta modificado)
        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                Conta c = BancoDB.getDB(getApplication()).contaDAO().findByNumero(numeroConta);
                c.creditar(valor);
                new Thread(() -> repository.atualizar(c)).start();
            }
        });
        thread.start();
    }


    //Usando o metodo debitar da classe Conta é feita a dedução do saldo
    //E usando o metodo atualizar da classe ContaRepository é feita a atualização
    //do saldo da conta no banco de dados
    void debitar(String numeroConta, double valor) {
        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                Conta c = BancoDB.getDB(getApplication()).contaDAO().findByNumero(numeroConta);
                c.debitar(valor);
                new Thread(() -> repository.atualizar(c)).start();
            }
        });
        thread.start();
    }

    //Usando o metodo buscarPeloNome na classe contaRepository uma conta com o parametro requisitado
    // é retornada

    void buscarPeloNome(String nomeCLiente) {
        new Thread(() -> repository.buscarPeloNome(nomeCLiente)).start();
    }

    //Usando o metodo buscarPeloCpf na classe contaRepositoryuma conta com o parametro requisitado
    // é retornada
    void buscarPeloCPF(String cpfCliente) {
        new Thread(() -> repository.buscarPeloCPF(cpfCliente)).start();
    }

    //Usando o metodo buscarPeloNumero na classe contaRepository uma conta com o parametro requisitado
    // é retornada
    void buscarPeloNumero(String numeroConta) {
        new Thread(() -> repository.buscarPeloNumero(numeroConta)).start();
    }

    //Usando uma Thread é retornado o valor da soma de valores do banco
    void saldoTotal() {
        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                saldoTotal = BancoDB.getDB(getApplication()).contaDAO().saldoTotal();
            }
        });
        thread.start();
    }

    //Retorna o saldo total do banco
    public Double getSaldoTotal() {
        saldoTotal();
        return saldoTotal;
    }

}
