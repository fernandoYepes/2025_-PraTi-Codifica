// Exceção (unchecked) lançada quando uma entidade não é
// encontrada no repositório.
public class EntidadeNaoEncontradaException extends RuntimeException {

    public EntidadeNaoEncontradaException(String mensagem) {
        super(mensagem);
    }
}