import java.math.BigDecimal;


 // Objeto de Valor IMUTÁVEL que representa um item no carrinho.

public record ItemCarrinho(Produto produto, int quantidade) {

    // Construtor compacto para validação
    public ItemCarrinho {
        if (produto == null) {
            throw new IllegalArgumentException("Produto não pode ser nulo.");
        }
        // Validação: Quantidade deve ser positiva
        if (quantidade <= 0) {
            throw new IllegalArgumentException("Quantidade deve ser maior que zero.");
        }
    }

     // @return um NOVO objeto Dinheiro com o subtotal.
    public Dinheiro getSubtotal() {
        BigDecimal subtotalValor = produto.preco().valor()
                .multiply(new BigDecimal(quantidade));

        return new Dinheiro(subtotalValor, produto.preco().moeda());
    }
}