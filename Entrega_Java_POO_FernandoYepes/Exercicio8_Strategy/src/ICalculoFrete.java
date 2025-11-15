import java.math.BigDecimal;

/**
 * A interface (Strategy) para todos os algoritmos de cálculo de frete.
 * É uma @FunctionalInterface, permitindo o uso de Lambdas.
 */
@FunctionalInterface
public interface ICalculoFrete {

    /**
     * Calcula o valor do frete para um pedido.
     * @param pedido O pedido (Contexto) contendo os dados (valor, CEP).
     * @return O valor do frete.
     * @throws CepInvalidoException Se o CEP for inválido para esta estratégia.
     */
    BigDecimal calcular(Pedido pedido) throws CepInvalidoException;
}