import java.math.BigDecimal;

public class Main {
    public static void main(String[] args) {

        System.out.println("### Demonstração do Padrão Strategy ###");

        // Pedido de R$ 250,00 para um CEP válido
        Pedido pedido = new Pedido(new BigDecimal("250.00"), "90110-001");

        // (Classes)
        ICalculoFrete estrategiaSedex = new Sedex();
        ICalculoFrete estrategiaPac = new Pac();
        ICalculoFrete estrategiaRetirada = new RetiradaNaLoja();

        // "Frete Grátis acima de R$ 200, senão, R$ 10"

        ICalculoFrete estrategiaPromocional = (p) -> { // 'p' é o Pedido
            // A Lambda também DEVE validar
            String cepLimpo = p.getCepDestino().replaceAll("[^0-9]", "");
            if (cepLimpo.length() != 8) {
                throw new CepInvalidoException("CEP inválido para promoção.");
            }

            // promocional
            if (p.getValorItens().compareTo(new BigDecimal("200.00")) > 0) {
                System.out.println("Promoção: Frete Grátis Aplicado!");
                return BigDecimal.ZERO; // Frete Grátis
            } else {
                return new BigDecimal("10.00"); // Taxa fixa promocional
            }
        };

        // (Usamos try-catch por causa da CepInvalidoException)
        try {
            // Sedex
            pedido.setEstrategiaFrete(estrategiaSedex);
            System.out.println("Frete (Sedex): R$ " + pedido.calcularFrete());

            // PAC (Trocando em tempo de execução)
            pedido.setEstrategiaFrete(estrategiaPac);
            System.out.println("Frete (PAC): R$ " + pedido.calcularFrete());

            // Retirada
            pedido.setEstrategiaFrete(estrategiaRetirada);
            System.out.println("Frete (Retirada): R$ " + pedido.calcularFrete());

            // Lambda (Pedido > 200)
            pedido.setEstrategiaFrete(estrategiaPromocional);
            System.out.println("Frete (Promoção): R$ " + pedido.calcularFrete());

            // Lambda (Pedido < 200)
            Pedido pedidoPequeno = new Pedido(new BigDecimal("50.00"), "90110-001");
            pedidoPequeno.setEstrategiaFrete(estrategiaPromocional);
            System.out.println("Frete (Promoção Pedido Pequeno): R$ " + pedidoPequeno.calcularFrete());


            // Demonstração da Exceção
            System.out.println("\n--- Teste de Exceção (CEP Inválido) ---");
            Pedido pedidoInvalido = new Pedido(new BigDecimal("100.00"), "CEP-ERRADO");
            pedidoInvalido.setEstrategiaFrete(estrategiaSedex);
            pedidoInvalido.calcularFrete(); // Esta linha deve falhar

        } catch (CepInvalidoException | IllegalStateException e) {
            System.out.println("ERRO: " + e.getMessage());
        }
    }
}