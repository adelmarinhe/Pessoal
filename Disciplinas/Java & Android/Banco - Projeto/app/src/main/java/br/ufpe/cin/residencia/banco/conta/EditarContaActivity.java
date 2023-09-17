package br.ufpe.cin.residencia.banco.conta;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;

import br.ufpe.cin.residencia.banco.R;

public class EditarContaActivity extends AppCompatActivity {

    public static final String KEY_NUMERO_CONTA = "numeroDaConta";
    public static final String KEY_CPF_CONTA = "CPFDaConta";
    public static final String KEY_NOME_CONTA = "NomeDaConta";
    public static final String KEY_SALDO_CONTA = "SaldoDaConta";
    ContaViewModel viewModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_adicionar_conta);
        viewModel = new ViewModelProvider(this).get(ContaViewModel.class);

        Button btnAtualizar = findViewById(R.id.btnAtualizar);
        Button btnRemover = findViewById(R.id.btnRemover);
        EditText campoNome = findViewById(R.id.nome);
        EditText campoNumero = findViewById(R.id.numero);
        EditText campoCPF = findViewById(R.id.cpf);
        EditText campoSaldo = findViewById(R.id.saldo);
        campoNumero.setEnabled(false);

        Intent i = getIntent();
        String numeroConta = i.getStringExtra(KEY_NUMERO_CONTA);
        String cpfConta = i.getStringExtra(KEY_CPF_CONTA);
        String nomeConta = i.getStringExtra(KEY_NOME_CONTA);
        String saldoConta = i.getStringExtra(KEY_SALDO_CONTA);

        campoNumero.setText(numeroConta);
        campoNome.setText(nomeConta);
        campoSaldo.setText(saldoConta);
        campoCPF.setText(cpfConta);

        btnAtualizar.setText("Editar");
        btnAtualizar.setOnClickListener(
                v -> {
                    String nomeCliente = campoNome.getText().toString();
                    String cpfCliente = campoCPF.getText().toString();
                    String saldoContaStr = campoSaldo.getText().toString();
                    try {
                        Conta c = new Conta(numeroConta, Double.valueOf(saldoContaStr), nomeCliente, cpfCliente);
                        viewModel.atualizar(c);
                    } catch (Exception e) {
                        campoCPF.setError("Campo inválido");
                        campoCPF.requestFocus();

                        campoNome.setError("Campo inválido");
                        campoNome.requestFocus();

                        campoSaldo.setError("Campo inválido");
                        campoSaldo.requestFocus();
                    }
                }
        );

        btnRemover.setOnClickListener(v -> {
            String nomeCliente = campoNome.getText().toString();
            String cpfCliente = campoCPF.getText().toString();
            String saldoContaStr = campoSaldo.getText().toString();

            try {
                Conta c = new Conta(numeroConta, Double.valueOf(saldoContaStr), nomeCliente, cpfCliente);
                viewModel.remover(c);
            } catch (Exception e) {
                campoCPF.setError("Campo inválido");
                campoCPF.requestFocus();

                campoNome.setError("Campo inválido");
                campoNome.requestFocus();

                campoSaldo.setError("Campo inválido");
                campoSaldo.requestFocus();
            }
        });
    }
}
