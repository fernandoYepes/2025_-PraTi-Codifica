// Arquivo: PagamentoInvalidoException.java

/**
 * Exceção customizada para erros de validação de pagamento.
 * Herda de 'Exception', o que a torna uma "checked exception"
 * (obriga o programador a tratá-la com try-catch).
 */
public class PagamentoInvalidoException extends Exception {

    public PagamentoInvalidoException(String mensagem) {
        // Passa a mensagem para o construtor da classe "mãe" (Exception)
        super(mensagem);
    }
}