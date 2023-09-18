package br.ufpe.cin.residencia.banco.conta;

import android.content.Context;
import android.content.Intent;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.text.NumberFormat;

public class ContaViewHolder extends RecyclerView.ViewHolder {
    TextView nomeCliente = null;
    TextView infoConta = null;
    ImageView icone = null;

    public ContaViewHolder(@NonNull View linha) {
        super(linha);
        this.nomeCliente = linha.findViewById(R.id.nomeCliente);
        this.infoConta = linha.findViewById(R.id.infoConta);
        this.icone = linha.findViewById(R.id.icone);
    }

    //Associa os dados de uma conta aos elementos da visualização do item
    void bindTo(Conta conta) {
        this.nomeCliente.setText(conta.nomeCliente);
        String info = conta.numero + " | Saldo atual: R$" + NumberFormat.getCurrencyInstance().format(conta.saldo);
        this.infoConta.setText(info);
        this.addListener(conta.numero, conta.cpfCliente, conta.nomeCliente, conta.saldo);
    }

    // Adiciona um listener de clique ao item do RecyclerView
    // Quando o item é clicado, inicia a atividade EditarContaActivity com os detalhes da conta
    public void addListener(String numeroConta, String cpfConta, String nomeConta, Double saldoConta) {
        this.itemView.setOnClickListener(
                v -> {
                    Context context = this.itemView.getContext();
                    Intent intent = new Intent(context, EditarContaActivity.class);
                    intent.putExtra("numeroDaConta", numeroConta);
                    intent.putExtra("CPFDaConta", cpfConta);
                    intent.putExtra("NomeDaConta", nomeConta);
                    intent.putExtra("SaldoDaConta", saldoConta.toString());
                    context.startActivity(intent);
                }
        );
    }
}
