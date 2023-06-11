typedef struct reg
{
    int conteudo;
    struct reg *prox;

}celula;

void inserirInicio(celula** lista, int valor){
    celula* novaCelula = (celula*)malloc(sizeof(celula));
    novaCelula -> conteudo = valor;
    novaCelula -> prox = *lista;
    *lista = novaCelula; 
}

// Função para imprimir os elementos da lista
void imprimirLista(celula* lista) {
    celula* atual = lista;
    while (atual != NULL) {
        printf("%d ", atual->conteudo);
        atual = atual->prox;
    }
    printf("\n");
}

int main() {
    celula* lista = NULL; // Lista vazia

    // Inserção de elementos na lista
    inserirInicio(&lista, 3);
    inserirInicio(&lista, 5);
    inserirInicio(&lista, 2);

    // Impressão da lista
    printf("Lista: ");
    imprimirLista(lista);

    return 0;
}