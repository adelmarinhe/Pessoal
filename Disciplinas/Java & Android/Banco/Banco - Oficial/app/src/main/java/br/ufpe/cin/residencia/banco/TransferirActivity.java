package br.ufpe.cin.residencia.banco;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class TransferirActivity extends AppCompatActivity {

    BancoViewModel viewModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_operacoes);
        viewModel = new ViewModelProvider(this).get(BancoViewModel.class);

        // Obter referências para os elementos da interface
        TextView tipoOperacao = findViewById(R.id.tipoOperacao);
        EditText numeroContaOrigem = findViewById(R.id.numeroContaOrigem);
        EditText numeroContaDestino = findViewById(R.id.numeroContaDestino);
        EditText valorOperacao = findViewById(R.id.valor);
        Button btnOperacao = findViewById(R.id.btnOperacao);

        // Personalizar a interface para uma operação de transferência
        valorOperacao.setHint(valorOperacao.getHint() + " transferido");
        tipoOperacao.setText("TRANSFERIR");
        btnOperacao.setText("Transferir");

        // Definir um ouvinte para o botão de operação
        btnOperacao.setOnClickListener(v -> {
            try {
                // Realiza a operação de transferência entre contas
                String numOrigem = numeroContaOrigem.getText().toString();
                String numDestino = numeroContaDestino.getText().toString();
                double valor = Double.valueOf(valorOperacao.getText().toString());
                viewModel.transferir(numOrigem, numDestino, valor);
                finish();
            } catch (Exception e) {
                // Exibir mensagens de erro nos campos inválidos
                numeroContaOrigem.setError("Campo inválido");
                numeroContaOrigem.requestFocus();
                numeroContaDestino.setError("Campo inválido");
                numeroContaDestino.requestFocus();
                valorOperacao.setError("Campo inválido");
                valorOperacao.requestFocus();
            }

        });
    }
}
