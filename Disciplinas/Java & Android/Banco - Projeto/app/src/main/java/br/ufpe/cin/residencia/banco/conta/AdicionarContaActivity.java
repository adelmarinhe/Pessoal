package br.ufpe.cin.residencia.banco.conta;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class AdicionarContaActivity extends AppCompatActivity {
    ContaViewModel viewModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_adicionar_conta);
        viewModel = new ViewModelProvider(this).get(ContaViewModel.class);

        // Obter referências para os elementos da interface
        Button btnAtualizar = findViewById(R.id.btnAtualizar);
        Button btnRemover = findViewById(R.id.btnRemover);
        EditText campoNome = findViewById(R.id.nome);
        EditText campoNumero = findViewById(R.id.numero);
        EditText campoCPF = findViewById(R.id.cpf);
        EditText campoSaldo = findViewById(R.id.saldo);

        // Configurar a interface para adicionar uma nova conta
        btnAtualizar.setText("Inserir");
        btnRemover.setVisibility(View.GONE);

        // Definir um ouvinte para o botão de atualização
        btnAtualizar.setOnClickListener(v -> {
            String nomeCliente = campoNome.getText().toString();
            String cpfCliente = campoCPF.getText().toString();
            String numeroConta = campoNumero.getText().toString();
            String saldoConta = campoSaldo.getText().toString();

            try {
                // Cria e insere um objeto Conta com os dados fornecidos
                Conta c = new Conta(numeroConta, Double.valueOf(saldoConta), nomeCliente, cpfCliente);
                viewModel.inserir(c);
            } catch (Exception e){
                // Exibir mensagens de erro nos campos inválidos
                campoNome.setError("Campo inválido");
                campoNome.requestFocus();
                campoCPF.setError("Campo inválido");
                campoCPF.requestFocus();
                campoNumero.setError("Campo inválido");
                campoNumero.requestFocus();
                campoSaldo.setError("Campo inválido");
                campoSaldo.requestFocus();
            }
            finish();
        });
    }
}
