import java.math.BigDecimal;

public abstract class FormaPagamento {

     // Este método é 'final' para que as subclasses não possam sobrescrevê-lo,
     // forçando-as a seguir este fluxo.

    public final void processarPagamento(BigDecimal valor) throws PagamentoInvalidoException {
        this.validarPagamento();

        // Se a validação passou (não lançou exceção), processa.
        System.out.printf("Pagamento APROVADO. Processando R$ %.2f via %s.%n",
                valor, this.getTipo());
    }

    // @throws PagamentoInvalidoException se os dados da forma de pagamento forem inválidos.

    protected abstract void validarPagamento() throws PagamentoInvalidoException;

     // Método auxiliar para os relatórios.
    protected abstract String getTipo();
}