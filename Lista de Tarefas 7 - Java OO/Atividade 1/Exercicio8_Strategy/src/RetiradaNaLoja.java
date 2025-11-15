import java.math.BigDecimal;

public class RetiradaNaLoja implements ICalculoFrete {

    @Override
    public BigDecimal calcular(Pedido pedido) {
        // Não valida CEP de destino e o custo é sempre zero.
        return BigDecimal.ZERO;
    }
}