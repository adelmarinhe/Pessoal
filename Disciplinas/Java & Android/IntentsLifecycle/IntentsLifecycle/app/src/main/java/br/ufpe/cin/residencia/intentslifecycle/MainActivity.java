package br.ufpe.cin.residencia.intentslifecycle;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //todos os elementos da UI
        final Button btnIntentExplicitoLifecycle = findViewById(R.id.btnIntentExplicito);
        final Button btnIntentImplicitoWeb = findViewById(R.id.btnIntentImplicitoWeb);
        final Button btnIntentImplicitoMapa = findViewById(R.id.btnIntentImplicitoMapa);
        final Button btnImplicitoMsg = findViewById(R.id.btnImplicitoMsg);
        final Button btnExplicitoMsg = findViewById(R.id.btnExplicitoMsg);
        final EditText mensagem = findViewById(R.id.mensagem);

        btnIntentExplicitoLifecycle.setOnClickListener(
                v -> {
                    //ir para a LifecycleActivity
                    //Intent Explícito - estamos definindo qual componente vai ser executado
                    Intent i = new Intent(
                            getApplicationContext(),
                            LifecycleActivity.class
                    );
                    startActivity(i);
                }
        );

        btnIntentImplicitoWeb.setOnClickListener(
                v -> {
                    Intent i = new Intent(Intent.ACTION_VIEW);
                    i.setData(Uri.parse("https://www.cin.ufpe.br"));
                    startActivity(i);
                }
        );

        btnIntentImplicitoMapa.setOnClickListener(
                v -> {
                    Intent i = new Intent(Intent.ACTION_VIEW);
                    i.setData(Uri.parse("geo:0,0?q=Av. Agamenon Magalhães"));
                    startActivity(i);
                }
        );

        btnExplicitoMsg.setOnClickListener(
                v->{
                    String oQueFoiDigitado = mensagem.getText().toString();
                    Intent intent = new Intent(
                            this,
                            MsgActivity.class
                    );
                    intent.putExtra(
                            getString(R.string.keyMensagem),
                            oQueFoiDigitado
                    );
                    startActivity(intent);
                }
        );

        btnImplicitoMsg.setOnClickListener(
                v -> {
                    String oQueFoiDigitado = mensagem.getText().toString();
                    Intent i = new Intent(Intent.ACTION_SEND);
                    i.setType("text/plain");
                    i.putExtra(getString(R.string.keyMensagem),oQueFoiDigitado);
                    startActivity(i);
                }
        );
    }
}