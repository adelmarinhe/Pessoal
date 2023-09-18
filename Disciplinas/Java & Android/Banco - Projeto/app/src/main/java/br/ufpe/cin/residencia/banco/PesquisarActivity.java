package br.ufpe.cin.residencia.banco;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;
import android.os.Handler;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioGroup;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import br.ufpe.cin.residencia.banco.conta.Conta;
import br.ufpe.cin.residencia.banco.conta.ContaAdapter;

public class PesquisarActivity extends AppCompatActivity {
    ContaAdapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_pesquisar);
        Button btnPesquisar = findViewById(R.id.btn_Pesquisar);
        RadioGroup tipoPesquisa = findViewById(R.id.tipoPesquisa);
        RecyclerView rvResultado = findViewById(R.id.rvResultado);
        adapter = new ContaAdapter(getLayoutInflater());
        rvResultado.setLayoutManager(new LinearLayoutManager(this));
        rvResultado.setAdapter(adapter);

        // Definir um ouvinte para o botão de pesquisa
        btnPesquisar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int selectedId = tipoPesquisa.getCheckedRadioButtonId();
                EditText aPesquisar = findViewById(R.id.pesquisa);
                String oQueFoiDigitado = aPesquisar.getText().toString();
                contentlist(oQueFoiDigitado, selectedId);
            }
        });

        // Exibir todas as contas inicialmente
        contentAllContas();
    }

    // Função para exibir todas as contas a cada 20 segundos
    // Assumindo que a função de pesquisa é executada em 20 segundos
    // Não consegui implementar de forma diferente
    public void contentAllContas() {
        getAllContas(20000);
    }

    // Função para exibir uma lista de contas baseado na pesquisa e tipo selecionados
    public void contentlist(String pesquisa, int tipo) {
        getListContas(1000, pesquisa, tipo);
    }

    // Função para obter todas as contas a cada 'miliseconds' em milissegundos
    public void getAllContas(int miliseconds) {
        final Handler handler = new Handler();

        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                List<Conta> conta = BancoDB.getDB(getApplicationContext()).contaDAO().getALlcontas();
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        adapter.submitList(conta);
                    }
                });
            }
        });
        thread.start();

        // Agendar a função de obter todas as contas novamente após 'miliseconds' milissegundos
        final Runnable runnable = new Runnable() {
            @Override
            public void run() {
                contentAllContas();
            }
        };
        handler.postDelayed(runnable, miliseconds);
    }

    //Obtém uma lista de contas com base nos parâmetros de pesquisa e tipo especificados
    public void getListContas(int miliseconds, String pesquisa, int tipo) {
        final Handler handler = new Handler();

        Map<Integer, Runnable> actionsMap = new HashMap<>();
        actionsMap.put(R.id.peloNomeCliente, () -> {
            List<Conta> conta = BancoDB.getDB(getApplicationContext()).contaDAO().findListBynomeCliente(pesquisa);
            runOnUiThread(() -> adapter.submitList(conta));
        });
        actionsMap.put(R.id.peloCPFcliente, () -> {
            List<Conta> conta = BancoDB.getDB(getApplicationContext()).contaDAO().findListBycpfCliente(pesquisa);
            runOnUiThread(() -> adapter.submitList(conta));
        });
        actionsMap.put(R.id.peloNumeroConta, () -> {
            List<Conta> conta = BancoDB.getDB(getApplicationContext()).contaDAO().findListByNumero(pesquisa);
            runOnUiThread(() -> adapter.submitList(conta));
        });
        actionsMap.put(0, () -> {
            List<Conta> conta = BancoDB.getDB(getApplicationContext()).contaDAO().getALlcontas();
            runOnUiThread(() -> adapter.submitList(conta));
        });

        Thread thread = new Thread(() -> {
            Runnable action = null;
            if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.N) {
                action = actionsMap.getOrDefault(tipo, actionsMap.get(0));
            }
            action.run();
        });
        thread.start();

        final Runnable runnable = () -> getListContas(miliseconds, pesquisa, tipo);
        handler.postDelayed(runnable, miliseconds);
        handler.removeCallbacks(runnable);
    }

}