package br.ufpe.cin.residencia.banco.conta;

import androidx.lifecycle.LiveData;
import androidx.room.Dao;
import androidx.room.Delete;
import androidx.room.Insert;
import androidx.room.OnConflictStrategy;
import androidx.room.Query;
import androidx.room.Update;
import java.util.List;

@Dao
public interface ContaDAO {
    //Inserir uma conta no banco de dados
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    void adicionar(Conta c);

    //Atualizar uma conta no banco de dados
    @Update
    void upDateConta(Conta c);

    //Remover uma conta no banco de dados
    @Delete
    void deleteConta(Conta c);

    //Buscar uma lista liveData de contas no banco de dados
    @Query("SELECT * FROM contas ORDER BY numero ASC")
    LiveData<List<Conta>> contas();

    //Buscar uma lista de contas no banco de dados
    @Query("SELECT * FROM contas ORDER BY numero ASC")
    List<Conta> getALlcontas();

    //Buscar as contas que tem o mesmo numero no banco de dados
    @Query("SELECT * FROM contas WHERE numero LIKE :numero")
    List<Conta> findListByNumero(String numero);

    //Buscar as contas que tem o mesmo cpf do cliente no banco de dados
    @Query("SELECT * FROM contas WHERE cpfCliente LIKE :cpfCliente")
    List<Conta> findListBycpfCliente(String cpfCliente);

    //Buscar as contas que tem o mesmo nome do cliente no banco de dados
    @Query("SELECT * FROM contas WHERE nomeCliente LIKE :nomeCliente")
    List<Conta> findListBynomeCliente(String nomeCliente);

    //Soma o saldo total do banco
    @Query("SELECT SUM(saldo) FROM contas")
    Double saldoTotal();

    //Buscar uma conta pelo numero da conta no banco de dados
    @Query("SELECT * FROM contas WHERE numero LIKE :numero LIMIT 1")
    Conta findByNumero(String numero);

}
