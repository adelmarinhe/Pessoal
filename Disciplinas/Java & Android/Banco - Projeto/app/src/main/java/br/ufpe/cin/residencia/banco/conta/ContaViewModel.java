package br.ufpe.cin.residencia.banco.conta;

import android.app.Application;

import androidx.annotation.NonNull;
import androidx.lifecycle.AndroidViewModel;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;

import java.util.List;

import br.ufpe.cin.residencia.banco.BancoDB;

public class ContaViewModel extends AndroidViewModel {
    private ContaRepository repository;
    public LiveData<List<Conta>> contas;
    private MutableLiveData<Conta> _contaAtual = new MutableLiveData<>();
    public LiveData<Conta> contaAtual = _contaAtual;

    public ContaViewModel(@NonNull Application application) {
        super(application);
        this.repository = new ContaRepository(BancoDB.getDB(application).contaDAO());
        this.contas = repository.getContas();
    }

    // Insere uma conta no banco de dados de forma assíncrona
    void inserir(Conta c) {
        new Thread(() -> repository.inserir(c)).start();
    }

    // Atualiza uma conta no banco de dados de forma assíncrona
    void atualizar(Conta c) {
        new Thread(() -> repository.atualizar(c)).start();
    }

    // Remove uma conta do banco de dados de forma assíncrona
    void remover(Conta c) {
        new Thread(() -> repository.remover(c)).start();
    }

    // Busca uma conta pelo número de conta no banco de dados de forma assíncrona
    public void buscarPeloNumero(String numeroConta) {
        new Thread(() -> repository.buscarPeloNumero(numeroConta)).start();
    }
}
