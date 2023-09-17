
 

 # DADOS DE TREINAMENTO PARA  PORTA LÓGICA 'AND'

  X = matrix(0,4,2)

  X[1,] = c(0,0)
  X[2,] = c(0,1)
  X[3,] = c(1,0)
  X[4,] = c(1,1)
  
  Y =  as.matrix(c(0,0,0,1))
  
  # TREINAMENTO DO MODELO DURANTE 50 CICLOS E TAXA DE 0.2
  
  T = 100
  alpha = 0.2
  
  modelo = perceptron(X,Y,T,alpha)  

  # PLOT DOS ERROS POR ITERAÇÃO 
  plot(1:T,modelo$erros,type = "l",xlab = "Iteration",ylab = "Sum of Square Errors")
  
      
  # FUNÇÃO PARA TREINAMENTO DO MODELO DURANTE T ITERAÇÕES
  
  perceptron <- function(X,Y,T,alpha){  
    
  
    N = nrow(X)  # NUMERO DE EXEMPLOS DE TREINAMENTO
    
    M = ncol(X)   
    
    # TRANSFORMAR DADOS DE TREINAMENTO PARA CONSIDERAR O BIAS COMO UM PESO
    
    X = cbind(X, rep(-1, N))
    
    # INICIALIAÇÃO ALEATORIA DOS PESOS DA REDE COM VALORES ALEATÓRIOS ENTRE -1 E 1
    
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
          
          # CALCULO DA SAIDA DO PECEPTRON COM FUNÇÃO DE ATIVAÇÃO SIGMOID  
          fj = 1/(1+exp(-s))  
          
          # CALCULO DO ERRO
          ej = yj - fj   
        
          all_erros = cbind(all_erros,ej)
        
          # REGRA DELTA
          wt = wt + as.numeric(alpha*ej) * xj   
        
      
          
      } # TERMINO DO CICLO
      
      sse_t = sum(all_erros^2)
      writeLines(sprintf("Iteração: %d. Erro: %.2f.",t,sse_t))
      
      
      list_sse = cbind(list_sse,sse_t)  # SOMA ERROs QUADRADOS BNA ITERACAO t
      
    }  # TERMINO DO APRENDIZADO
  
    
    return(list(modelo = wt, erros = list_sse, sse = list_sse[T]))
    
  }  
    

        
        
        