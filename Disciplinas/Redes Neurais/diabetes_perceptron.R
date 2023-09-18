#funcao de treino do perceptron em T iteracoes

perceptron <- function(X,Y,T,alpha){
  
  N = nrow(X)  # NUMERO DE EXEMPLOS DE TREINAMENTO
  
  M = ncol(X)   
  
  # TRANSFORMAR DADOS DE TREINAMENTO PARA CONSIDERAR O BIAS COMO UM PESO
  
  X = cbind(X, rep(-1, N))
  
  # INICIALIACAO ALEATORIA DOS PESOS DA REDE COM VALORES ALEATORIOS ENTRE -1 E 1
  
  wt = as.matrix(runif(M+1,-1,1))
  
  list_sse = cbind()
  
  # CICLO DE APRENDIZADO
  
  for (t in 1:T){
    
    all_erros = cbind()
    
    for (j in 1:N){
      
      # EXEMPLO ATUAL 
      
      xj = X[j,]
      
      yj = Y[j]
      
      # CALCULO DA SOMA ACUMULADA DOS PESOS
      
      s = t(wt) %*% xj  
      
      # CALCULO DA SAIDA DO PECEPTRON COM FUNCAO DE ATIVACAO SIGMOID  
      
      fj = 1/(1+exp(-s))  
      
      # CALCULO DO ERRO
      
      ej = fj - yj  
      
      all_erros = cbind(all_erros,ej)
      
      # REGRA DELTA
      wt = wt - as.numeric(alpha*ej) * xj   
      
    } # TERMINO DO CICLO
    
    sse_t = sum(all_erros^2)
    writeLines(sprintf("Iteracao: %d. Erro: %.2f.",t,sse_t))
    
    # SOMA ERROS QUADRADOS BNA ITERACAO t
    
    list_sse = cbind(list_sse,sse_t)  
    
  }
  
  return(list(modelo = wt, erros = list_sse, sse = list_sse[T]))
  
}

# dados de treinamento

X = as.matrix(diabetes[,1:8])

Y = diabetes$class

Y = as.numeric(factor(Y)) - 1

# TREINAMENTO DO MODELO DURANTE 100 CICLOS E TAXA DE 0.2

T = 100
alpha = 0.2

modelos = list()
erros = cbind()

for (t in 1:20){
  #executar modelo
  modelo = perceptron(X,Y,T,alpha)
  #salvar modelo
  modelos[[t]] = modelo$modelo
  erros = c(erros, min(modelo$sse))
}
  
# PLOT DOS ERROS POR ITERACAO 

plot(1:T,modelo$erros,type = "l",
     xlab = "Iteration",
     ylab = "Sum of Square Errors"
     )

# melhor modelo

min_erro = which.min(erros)
melhor_modelo = modelos[(min_erro)]

print("melhor modelo:")
print(melhor_modelo)
print("menor erro:")
print(min_erro)


#classificacoes do perceptron

w = melhor_modelo[[1]]
saidas = cbind()

for(i in 1:nrow(X)){
  x = c(X[i,],-1)
  s = t(w) %*% x
  f = 1/(1+exp(-s))
  saidas = cbind(saidas,f)
}

yp = 1*(saidas > 0.5)

acc = 100*sum(yp == Y)/nrow(X)
acc
