# Carregando a biblioteca nnet
library(nnet)

# Definindo uma lista de valores possíveis para o número de neurônios na camada oculta
num_neurons <- c(1, 2 , 3, 4, 5, 6, 7, 8)

# Criando vetores para armazenar os resultados de acurácia média
accuracy_results <- numeric(length(num_neurons))

# Definindo o número de iterações para cálculo da acurácia média
num_iterations <- 10

# set.seed(123) # Definindo uma semente para reprodutibilidade

# Realizando o treinamento e cálculo da acurácia média para cada valor de número de neurônios
for (i in 1:length(num_neurons)) {
  # Separando conjunto de treino e validação
  
  ind_train <- sample(1:nrow(diabetes), 500) # Amostra aleatória para treino
  ind_val <- setdiff(1:nrow(diabetes), ind_train) # Conjunto de validação
  
  dados_train <- diabetes[ind_train, ]
  dados_val <- diabetes[ind_val, ]
  
  acc <- numeric(num_iterations) # Vetor para armazenar as acurácias
  
  for (j in 1:num_iterations) {
    # Treinando a rede neural
    nn <- nnet(class ~ ., data = dados_train, size = num_neurons[i], maxit = 500)
    
    # Fazendo previsões no conjunto de validação
    preds <- predict(nn, dados_val, type = "class")
    
    # Calculando a acurácia
    acc[j] <- sum(preds == dados_val$class) / length(preds)
  }
  
  # Calculando a média da acurácia para o número de neurônios atual
  accuracy_results[i] <- mean(acc)
}

# Encontrando o melhor resultado em termos de acurácia média
best_accuracy <- max(accuracy_results)
best_num_neurons <- num_neurons[which.max(accuracy_results)]

#resultados
cat(accuracy_results, "\n")

# Imprimindo o resultado
cat("Melhor número de neurônios na camada oculta:", best_num_neurons, "\n")
cat("Acurácia média correspondente:", best_accuracy, "\n")