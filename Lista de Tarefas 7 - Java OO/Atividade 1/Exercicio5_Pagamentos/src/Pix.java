// Arquivo: Pix.java
import java.math.BigDecimal;

public class Pix extends FormaPagamento {

    private String chavePix;

    public Pix(String chavePix) {
        this.chavePix = chavePix;
    }

    @Override
    protected void validarPagamento() throws PagamentoInvalidoException {
        System.out.println("Validando Chave Pix...");

        // Validação simples: apenas checa se não está vazia
        if (chavePix == null || chavePix.trim().isEmpty()) {
            throw new PagamentoInvalidoException("A Chave Pix não pode ser nula ou vazia.");
        }

        // (Uma validação real checaria se é um CPF, CNPJ, e-mail ou UUID)

        System.out.println("Chave Pix válida.");
    }

    @Override
    protected String getTipo() {
        return "PIX";
    }
}