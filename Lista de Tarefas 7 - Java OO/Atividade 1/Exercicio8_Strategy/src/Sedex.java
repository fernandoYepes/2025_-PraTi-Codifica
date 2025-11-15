
import java.math.BigDecimal;

public class Sedex implements ICalculoFrete {

    @Override
    public BigDecimal calcular(Pedido pedido) throws CepInvalidoException {
        // Validação Específica do Sedex
        validarCep(pedido.getCepDestino());

        // Lógica de Cálculo (ex: taxa fixa alta)
        return new BigDecimal("35.50");
    }

    // Método de validação privado
    private void validarCep(String cep) throws CepInvalidoException {
        // Validação simples
        String cepLimpo = cep.replaceAll("[^0-9]", "");
        if (cepLimpo.length() != 8) {
            throw new CepInvalidoException("CEP inválido para Sedex (deve ter 8 dígitos): " + cep);
        }
        if (cepLimpo.startsWith("99")) {
            throw new CepInvalidoException("Sedex indisponível para a região 99XXX.");
        }
    }
}