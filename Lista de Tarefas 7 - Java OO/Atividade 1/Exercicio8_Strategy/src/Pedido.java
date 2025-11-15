import java.math.BigDecimal;


 // A classe de "Contexto" que USA a estratégia de frete.
public class Pedido {

    private BigDecimal valorItens;
    private String cepDestino;


    private ICalculoFrete estrategiaFrete;

    public Pedido(BigDecimal valorItens, String cepDestino) {
        this.valorItens = valorItens;
        this.cepDestino = cepDestino;
    }

    // Getters necessários para as estratégias
    public BigDecimal getValorItens() {
        return valorItens;
    }

    public String getCepDestino() {
        return cepDestino;
    }

    /**
     * O "Injetor" de Estratégia.
     * Permite trocar o algoritmo de cálculo em tempo de execução.
     */
    public void setEstrategiaFrete(ICalculoFrete estrategiaFrete) {
        this.estrategiaFrete = estrategiaFrete;
    }

    public BigDecimal calcularFrete() throws CepInvalidoException {
        if (this.estrategiaFrete == null) {
            throw new IllegalStateException("Nenhuma estratégia de frete foi definida para o pedido.");
        }
        // Delegação: Chama o método da interface (que será o do Sedex, Pac, etc.)
        return this.estrategiaFrete.calcular(this);
    }
}