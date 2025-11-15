import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;
import java.util.List;

 // Todas as operações de "modificação" retornam uma NOVA instância do Carrinho.

public final class Carrinho { // previne herança

    // A lista de itens é IMUTÁVEL
    private final List<ItemCarrinho> itens;
    // O cupom aplicado (em porcentagem, ex: 10.5 para 10.5%)
    private final BigDecimal cupomDesconto;

    public Carrinho() {
        // Inicia, lista vazia e sem cupom
        this.itens = List.of();
        this.cupomDesconto = BigDecimal.ZERO;
    }


     // Construtor privado usado internamente para criar as NOVAS instâncias.
    private Carrinho(List<ItemCarrinho> itens, BigDecimal cupomDesconto) {
        // List.copyOf() cria uma cópia defensiva imutável.
        this.itens = List.copyOf(itens);
        this.cupomDesconto = cupomDesconto;
    }

    // Adiciona um item e retorna um NOVO carrinho com o item.
    public Carrinho adicionarItem(ItemCarrinho novoItem) {
        List<ItemCarrinho> novosItens = new ArrayList<>(this.itens);
        novosItens.add(novoItem);
        return new Carrinho(novosItens, this.cupomDesconto);
    }

    // Remove um item e retorna um NOVO carrinho sem o item.
    public Carrinho removerItem(ItemCarrinho itemParaRemover) {
        List<ItemCarrinho> novosItens = new ArrayList<>(this.itens);
        novosItens.remove(itemParaRemover); // Funciona bem pois ItemCarrinho é um 'record' (com equals/hashCode)
        return new Carrinho(novosItens, this.cupomDesconto);
    }


     // Aplica um cupom e retorna um NOVO carrinho com o desconto.
    public Carrinho aplicarCupom(BigDecimal porcentagem) {
        // Validação: Cupom entre 0 e 30%
        if (porcentagem.compareTo(BigDecimal.ZERO) < 0 ||
                porcentagem.compareTo(new BigDecimal("30.0")) > 0) {
            throw new IllegalArgumentException("Cupom deve ser entre 0% e 30%.");
        }
        // Retorna um NOVO carrinho com os mesmos itens, mas com o cupom novo
        return new Carrinho(this.itens, porcentagem);
    }


     // Calcula o Subtotal (soma de todos os itens, sem desconto).

    public Dinheiro getSubtotal() {
        // Padrão BRL
        Moeda moeda = this.itens.isEmpty() ? Moeda.BRL : this.itens.get(0).produto().preco().moeda();

        Dinheiro subtotal = new Dinheiro(BigDecimal.ZERO, moeda);
        for (ItemCarrinho item : this.itens) {
            subtotal = subtotal.add(item.getSubtotal());
        }
        return subtotal;
    }

     // Subtotal - Desconto do Cupom).
    public Dinheiro getTotalFinal() {
        Dinheiro subtotal = this.getSubtotal();

        // Se não há desconto, retorna o subtotal
        if (this.cupomDesconto.compareTo(BigDecimal.ZERO) == 0) {
            return subtotal;
        }

        BigDecimal fatorDesconto = BigDecimal.ONE.subtract(
                this.cupomDesconto.divide(new BigDecimal("100"))
        );

        BigDecimal valorFinal = subtotal.valor().multiply(fatorDesconto);

        // Aplica Arredondamento Bancário
        valorFinal = valorFinal.setScale(2, RoundingMode.HALF_EVEN);

        return new Dinheiro(valorFinal, subtotal.moeda());
    }

    // Método auxiliar para exibição
    @Override
    public String toString() {
        return "Carrinho{" +
                "itens=" + itens.size() +
                ", cupom=" + cupomDesconto + "%" +
                ", totalFinal=" + getTotalFinal() +
                '}';
    }
}