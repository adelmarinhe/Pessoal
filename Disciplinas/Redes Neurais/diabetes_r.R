# Set the file path of your CSV file
file_path <- "C:/Users/jams/Documents/Disciplinas/Redes Neurais/diabetes.csv"

# Read the CSV file
diabetes <- read.csv(file_path)

X = as.matrix(diabetes[.1:8])

Y = diabetes$class

Y = as.numeric(factor(Y)) - 1

# TREINAMENTO DO MODELO DURANTE 100 CICLOS E TAXA DE 0.2

T = 10
alpha = 0.2

# FUNCAO PARA TREINAMENTO DO MODELO DURANTE T ITERACOES

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
      
      # CALCULO DA SAIDA DO PECEPTRON COM FUN??O DE ATIVA??O SIGMOID  
      fj = 1/(1+exp(-s))  
      
      # CALCULO DO ERRO
      ej = fj - yj  
      
      all_erros = cbind(all_erros,ej)
      
      # REGRA DELTA
      wt = wt - as.numeric(alpha*ej) * xj   
      
    } # TERMINO DO CICLO
    
    sse_t = sum(all_erros^2)
    writeLines(sprintf("Iteracao: %d. Erro: %.2f.",t,sse_t))
    
    
    list_sse = cbind(list_sse,sse_t)  # SOMA ERROs QUADRADOS BNA ITERACAO t
    
  }  # TERMINO DO APRENDIZADO
  
  return(list(modelo = wt, erros = list_sse, sse = list_sse[T]))
  
}  

modelos = list()
erros = list()

for (t in 1:20){
  modelo = perceptron(X,Y,T,alpha)
  modelos[[t]] = modelo$modelos
  erros = cbind(erros, modelo$SSE)
}
  
# PLOT DOS ERROS POR ITERACAO 
plot(1:T,modelo$erros,type = "l",xlab = "Iteration",ylab = "Sum of Square Errors")

View(erros)


