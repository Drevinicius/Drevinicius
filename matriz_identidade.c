#include <stdio.h>

int main(){
    int LINHA, COLUNA;
    printf("Tamnaho da matriz: ");
    scanf("%d", &LINHA);
    COLUNA = LINHA; // Apenas por questões de entendimento, mas não precisa dessa linha

    int matriz_identidade[LINHA][COLUNA];

    for(int L = 0; L < LINHA; L++){
        for(int C = 0; C < COLUNA; C++){
            if(L != C){
                matriz_identidade[L][C] = 0;
            }else{
                matriz_identidade[L][C] = 1;
            }
        }
    }
    printf("\nGERANDO UMA MATRIZ IDENTIDADE %d X %d...\n\n", LINHA, COLUNA); // Apenas por uma questão estetica foi criado variavel para linha e coluna
    for(int L = 0; L < LINHA; L++){
        for(int C = 0; C < COLUNA; C++){
            printf("[%d]", matriz_identidade[L][C]);
        }
        printf("\n");
    }
    return 0;
}