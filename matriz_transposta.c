#include <stdio.h>

int main() {
    int matriz_transposta[2][3] = {{1, 2, 3}, {4, 5, 6}};
    printf("Matriz Original:\n");
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", matriz_transposta[i][j]);
        }
        printf("\n");
    }

    printf("\nMatriz Transposta:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 2; j++) {
            printf("%d ", matriz_transposta[j][i]);
        }
        printf("\n");
    }
    return 0;
}