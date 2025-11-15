import java.math.BigDecimal;

public class Pac implements ICalculoFrete {

    @Override
    public BigDecimal calcular(Pedido pedido) throws CepInvalidoException {
        // Validação PAC
        validarCep(pedido.getCepDestino());

        // Lógica
        return new BigDecimal("18.00");
    }

    private void validarCep(String cep) throws CepInvalidoException {
        String cepLimpo = cep.replaceAll("[^0-9]", "");
        if (cepLimpo.length() != 8) {
            throw new CepInvalidoException("CEP inválido para PAC (deve ter 8 dígitos): " + cep);
        }
    }
}