package br.ufpe.cin.residencia.intentslifecycle;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;

public class MsgActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_msg);

        Intent intentUsadoParaChegarAqui = getIntent();
        String mensagem =
                intentUsadoParaChegarAqui
                .getStringExtra(getString(R.string.keyMensagem));

        TextView texto = findViewById(R.id.textoMensagem);
        texto.setText(mensagem);
    }
}