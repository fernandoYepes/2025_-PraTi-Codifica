import java.math.BigDecimal;

public class Boleto extends FormaPagamento {

    private String codigoBarras;

    public Boleto(String codigoBarras) {
        this.codigoBarras = codigoBarras;
    }

    @Override
    protected void validarPagamento() throws PagamentoInvalidoException {
        System.out.println("Validando Boleto...");

        if (codigoBarras == null || codigoBarras.trim().isEmpty()) {
            throw new PagamentoInvalidoException("Código de barras não pode ser nulo ou vazio.");
        }

        // Validação simples: checa o tamanho padrão (sem checar dígitos)
        String codigoLimpo = codigoBarras.replaceAll("[\\s\\.]", ""); // Remove espaços e pontos

        if (codigoLimpo.length() != 44) {
            throw new PagamentoInvalidoException("Código de barras do boleto é inválido (deve ter 44 dígitos).");
        }

        System.out.println("Boleto válido.");
    }

    @Override
    protected String getTipo() {
        return "Boleto";
    }
}