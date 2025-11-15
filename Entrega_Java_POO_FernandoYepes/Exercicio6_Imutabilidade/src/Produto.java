// Objeto de Valor IMUTÁVEL que representa um Produto.

public record Produto(String sku, String nome, Dinheiro preco) {

    // Construtor compacto para validação
    public Produto {
        if (sku == null || sku.isBlank()) {
            throw new IllegalArgumentException("SKU não pode ser nulo ou vazio.");
        }
        if (nome == null || nome.isBlank()) {
            throw new IllegalArgumentException("Nome do produto não pode ser nulo ou vazio.");
        }
        if (preco == null) {
            throw new IllegalArgumentException("Preço não pode ser nulo.");
        }
    }
}