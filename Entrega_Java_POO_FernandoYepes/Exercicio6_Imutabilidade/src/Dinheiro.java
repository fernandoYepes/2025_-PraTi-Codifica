import java.math.BigDecimal;
import java.math.RoundingMode;

public record Dinheiro(BigDecimal valor, Moeda moeda) {

    // Construtor compacto para validação
    public Dinheiro {
        // Validação: Proíbe valores nulos ou negativos
        if (valor == null || valor.compareTo(BigDecimal.ZERO) < 0) {
            throw new IllegalArgumentException("Valor monetário não pode ser nulo ou negativo.");
        }
        if (moeda == null) {
            throw new IllegalArgumentException("Moeda não pode ser nula.");
        }

        // Garante 2 casas decimais com arredondamento bancário
        // Isso padroniza todos os objetos Dinheiro
        valor = valor.setScale(2, RoundingMode.HALF_EVEN);
    }

    // Método auxiliar imutável (retorna um NOVO objeto Dinheiro)
    public Dinheiro add(Dinheiro outro) {
        if (!this.moeda.equals(outro.moeda)) {
            throw new IllegalArgumentException("Não é possível somar moedas diferentes.");
        }
        // Retorna uma nova instância
        return new Dinheiro(this.valor.add(outro.valor), this.moeda);
    }
}