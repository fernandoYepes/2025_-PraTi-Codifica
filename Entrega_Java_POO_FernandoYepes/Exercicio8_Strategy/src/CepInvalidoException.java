 // Exceção "checked" para CEPs que não passam na validação.

public class CepInvalidoException extends Exception {

    public CepInvalidoException(String mensagem) {
        super(mensagem);
    }
}