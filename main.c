// Online C compiler to run C program online
#include <stdio.h>
#include <stdlib.h>

typedef struct no{
    int valor;
    struct no *prox;
} No;

void exibir(No *lista){
    No *aux = lista;
    while(aux){
        printf("\tEndereco: %p\nValor: %d\nProximo: %p\n\n", (void *)aux, aux->valor, aux->prox);
        aux = aux->prox;
    }
}

void criarNo(No **lista, int valor){
    No *novoNo = (No *)malloc(sizeof(No));
    if(!novoNo){
        *lista = NULL;
        return;
    }
    novoNo->valor = valor;
    novoNo->prox = NULL;
    *lista = novoNo;
}

void inserirInicio(No **lista, int valor){
    No *novoNo;
    criarNo(&novoNo, valor);
    if(!(*lista)){
        *lista = novoNo;
        return;
    }
    novoNo->prox = *lista;
    *lista = novoNo;
}

void *inserirFim(No **lista, int valor){
    No *novoNo;
    criarNo(&novoNo, valor);
    if(!(*lista)){
        *lista = novoNo;
    }else{
        No *aux = *lista;
        
    }
}

int main() {
    No *lista = NULL;
    inserirInicio(&lista, 4);
    inserirInicio(&lista, 3);
    inserirInicio(&lista, 2);
    inserirInicio(&lista, 1);

    exibir(lista);
    
    return 0;
}
