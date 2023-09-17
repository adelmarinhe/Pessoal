package br.ufpe.cin.residencia.banco;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class DebitarActivity extends AppCompatActivity {
    BancoViewModel viewModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_operacoes);

        // Inicializar o ViewModel para acesso aos dados do banco
        viewModel = new ViewModelProvider(this).get(BancoViewModel.class);

        // Obter referências para os elementos da interface
        TextView tipoOperacao = findViewById(R.id.tipoOperacao);
        EditText numeroContaOrigem = findViewById(R.id.numeroContaOrigem);
        TextView labelContaDestino = findViewById(R.id.labelContaDestino);
        EditText numeroContaDestino = findViewById(R.id.numeroContaDestino);
        EditText valorOperacao = findViewById(R.id.valor);
        Button btnOperacao = findViewById(R.id.btnOperacao);

        // Esconder o campo da conta de destino, pois é uma operação de débito
        labelContaDestino.setVisibility(View.GONE);
        numeroContaDestino.setVisibility(View.GONE);

        // Personalizar a interface para uma operação de débito
        valorOperacao.setHint(valorOperacao.getHint() + " debitado");
        tipoOperacao.setText("DEBITAR");
        btnOperacao.setText("Debitar");

        // Definir um ouvinte para o botão de operação
        btnOperacao.setOnClickListener(v -> {
            try {
                // realiza a operação de débito
                String numConta = numeroContaOrigem.getText().toString();
                double valor = Double.valueOf(valorOperacao.getText().toString());
                viewModel.debitar(numConta, valor);
                finish();
            } catch (Exception e) {
                // Exibir mensagens de erro nos campos inválidos
                numeroContaOrigem.setError("Campo inválido");
                numeroContaOrigem.requestFocus();
                valorOperacao.setError("Campo inválido");
                valorOperacao.requestFocus();
            }
        });
    }
}
