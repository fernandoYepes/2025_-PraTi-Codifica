import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {

        System.out.println("### Simulação de Sistema de Pagamentos ###");

        // O valor a ser pago
        BigDecimal valor = new BigDecimal("250.75");

        // 1. Criamos a lista de Formas de Pagamento (Polimorfismo)
        List<FormaPagamento> formas = new ArrayList<>();

        // --- Pagamentos VÁLIDOS ---
        formas.add(new CartaoCredito("1234 5678 1234 5678"));
        formas.add(new Pix("meu-email@exemplo.com"));
        formas.add(new Boleto("00190 50295 40144 816019 06809 350314 1 89560000025075"));

        // --- Pagamentos INVÁLIDOS ---
        formas.add(new CartaoCredito("123")); // Número curto
        formas.add(new Pix(null)); // Chave nula
        formas.add(new Boleto("992 588 777")); // Formato errado

        // 2. Processamos todos os pagamentos
        for (FormaPagamento forma : formas) {

            System.out.println("\n-------------------------------------------");
            System.out.println("Tentando pagamento de R$" + valor + " via " + forma.getClass().getSimpleName());

            try {
                // Aqui acontece a "mágica"
                // Chamamos o método da classe base, que por sua vez
                // chama o método validarPagamento() da classe filha.
                forma.processarPagamento(valor);

            } catch (PagamentoInvalidoException e) {
                // Capturamos a exceção específica que criamos
                System.out.println("Pagamento FALHOU: " + e.getMessage());
            } catch (Exception e) {
                // Captura qualquer outro erro inesperado
                System.out.println("Erro inesperado: " + e.getMessage());
            }
        }
        System.out.println("\n-------------------------------------------");
        System.out.println("Simulação concluída.");
    }
}