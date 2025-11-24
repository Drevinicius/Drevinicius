#include <stdio.h>
#include <stdlib.h>

// Para o uso do system() nos OS compativeis
#ifdef _WIN32
    #define CLEAR "cls"
    #define PAUSE "pause"
#else
    #define CLEAR "clear"
    #define PAUSE "read -p 'Pressione Enter...' var"
#endif

typedef struct no{
    int valor;
    struct no *prox;
} No;

// metodos de exibicao de apenas valores e completo
void exibirValores(No *lista){
    No *aux = lista;
    while(aux){
        printf("[%d] ", aux->valor);
        aux = aux->prox;
    }
    printf("\n");
    system(PAUSE);
}

void exibirCompleto(No *lista){
    No *aux = lista;
    while(aux){
        printf("\tEndereco: %p\nValor: %d\nProximo: %p\n\n", (void *)aux, aux->valor, aux->prox);
        aux = aux->prox;
    }
    system(PAUSE);
}
// Fim dos metodos de exibicao

// Alocacao dinamica de memoria
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

// Metodo de insercao no inicio da lista
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

// Metodo de insercao no fim da lista
void inserirFim(No **lista, int valor){
    No *novoNo;
    criarNo(&novoNo, valor);
    
    if(!(*lista)){
        *lista = novoNo;
        return;
    }
    
    No *aux = *lista;
    while(aux->prox){
        aux = aux->prox;
    }
    aux->prox = novoNo;
}
// Metodo de insercao em uma posicao
void inserirPos(No **lista, int valor, int pos){
    if(!(*lista)){
        No *novoNo;
        criarNo(&novoNo, valor);
        *lista = novoNo;
        return;
    }
    if(pos == 1){
        inserirInicio(&(*lista), valor);
        return;
    }
    int var = 2;
    No *aux = *lista;
    No *ant = *lista;
    
    aux = aux->prox;
    
    while(var < pos && aux->prox){
        aux = aux->prox;
        ant = ant->prox;
        var++;
    }
    if(aux->prox == NULL){
        inserirFim(&(*lista), valor);
    }else{
        No *novoNo;
        criarNo(&novoNo, valor);
        
        novoNo->prox = aux;
        ant->prox = novoNo;
    }
}

// Mini sistema de gestao de lista encadeada
int main() {
    No *lista = NULL;
    system(CLEAR);
    int op;
    int controlador = 1;
    
    while(controlador == 1){
        
        system(CLEAR);
        
        printf("=============================\n");
        printf("\tBem-vindo!\n");
        printf("=============================\n");
        printf("1 - Inserir no inicio\n2 - Inserir no fim\n3 - Inserir numa posicao\n4 - Exibir lista completa\n5 - Exibir valores\n0 - Sair\n");
        printf("Escolha uma opção: ");
        scanf("%d", &op);
        
        system(CLEAR);
        
        switch (op){
            case 1:
                int valor;
                printf("Digite o valor: ");
                scanf("%d", &valor);
                system(CLEAR);
                inserirInicio(&lista, valor);
                break;
            case 2:
                int valor1;
                printf("Digite o valor: ");
                scanf("%d", &valor1);
                system(CLEAR);
                inserirFim(&lista, valor1);
                break;
            case 3:
                int valor2, pos;
                printf("Digite o valor: ");
                scanf("%d", &valor2);
                
                printf("Digite a posicao: ");
                scanf("%d", &pos);
                
                system(CLEAR);
                inserirPos(&lista, valor2, pos);
                break;
            case 4:
                exibirCompleto(lista);
                break;
            case 5:
                exibirValores(lista);
                break;
            case 0:
                controlador++;
                break;
            default:
                printf("Opcao invalida!\n");
                system(PAUSE);
                break;
        }
    }
    
    return 0;
}
