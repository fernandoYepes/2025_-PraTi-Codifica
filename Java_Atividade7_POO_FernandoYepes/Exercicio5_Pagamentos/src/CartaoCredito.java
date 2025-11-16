import java.math.BigDecimal;

public class CartaoCredito extends FormaPagamento {

    private String numeroCartao;

    public CartaoCredito(String numeroCartao) {
        this.numeroCartao = numeroCartao;
    }

    @Override
    protected void validarPagamento() throws PagamentoInvalidoException {
        System.out.println("Validando Cartão de Crédito...");

        if (numeroCartao == null || numeroCartao.trim().isEmpty()) {
            throw new PagamentoInvalidoException("Número do cartão não pode ser NULO ou VAZIO.");
        }

        // Remove espaços para fazer a contagem
        String numeroLimpo = numeroCartao.replaceAll("\\s+", "");

        // Validação simples: apenas checa o tamanho
        if (numeroLimpo.length() != 16) {
            throw new PagamentoInvalidoException("Número do cartão de crédito é inválido (deve ter 16 dígitos).");
        }

        System.out.println("Cartão de Crédito válido.");
    }

    @Override
    protected String getTipo() {
        return "Cartão de Crédito";
    }
}