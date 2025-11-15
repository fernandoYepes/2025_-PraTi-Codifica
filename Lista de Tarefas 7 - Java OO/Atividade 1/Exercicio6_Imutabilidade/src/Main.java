import java.math.BigDecimal;

public class Main {
    public static void main(String[] args) {

        System.out.println("### Demonstração de Carrinho Imutável ###");

        // --- 1. Setup (Criação dos Produtos) ---
        Produto p1 = new Produto("NB-001", "Notebook Pro", new Dinheiro(new BigDecimal("7500.00"), Moeda.BRL));
        Produto p2 = new Produto("MS-002", "Mouse Sem Fio", new Dinheiro(new BigDecimal("150.55"), Moeda.BRL));
        Produto p3 = new Produto("KB-003", "Teclado Mecânico", new Dinheiro(new BigDecimal("499.90"), Moeda.BRL));

        // --- 2. Criação dos Itens ---
        ItemCarrinho item1 = new ItemCarrinho(p1, 1); // 1 Notebook
        ItemCarrinho item2 = new ItemCarrinho(p2, 2); // 2 Mouses

        // --- 3. Demonstração do Fluxo Imutável ---

        System.out.println("\n--- Fluxo de Compra ---");

        // Estado Inicial
        Carrinho c1 = new Carrinho();
        System.out.println("C1 (Vazio):     " + c1); // Total: 0.00

        Carrinho c2 = c1.adicionarItem(item1);
        System.out.println("C2 (c/ Notebook): " + c2); // Total: 7500.00

        Carrinho c3 = c2.adicionarItem(item2);
        System.out.println("C3 (c/ N+M):     " + c3); // Subtotal: 7500.00 + 301.10 = 7801.10

        Carrinho c4 = c3.aplicarCupom(new BigDecimal("10.0")); // 10%
        System.out.println("C4 (c/ Cupom 10%):" + c4); // Total: 7801.10 * 0.9 = 7020.99

        Carrinho c5 = c4.removerItem(item1);
        System.out.println("C5 (s/ Notebook):" + c5); // Total: 301.10 * 0.9 = 270.99

        // Verificação da Imutabilidade
        System.out.println("\n--- Verificando Imutabilidade (c1 e c2) ---");
        System.out.println("C1 (Original):  " + c1); // Deve estar VAZIO
        System.out.println("C2 (Original):  " + c2); // Deve ter SÓ o Notebook
        System.out.println("C3 (Original):  " + c3); // Deve ter N+M, SEM cupom

        // Teste de Validação (Exceções) ---
        System.out.println("\n--- Testando Validações (Exceções) ---");

        // Teste: Cupom Inválido (> 30%)
        try {
            c3.aplicarCupom(new BigDecimal("35.0"));
        } catch (IllegalArgumentException e) {
            System.out.println("Sucesso (Cupom Inválido): " + e.getMessage());
        }

        // Teste: Quantidade Inválida (<= 0)
        try {
            ItemCarrinho itemInvalido = new ItemCarrinho(p3, 0);
        } catch (IllegalArgumentException e) {
            System.out.println("Sucesso (Qtd Inválida): " + e.getMessage());
        }

        // Teste: Valor Negativo
        try {
            Dinheiro dinheiroInvalido = new Dinheiro(new BigDecimal("-100"), Moeda.BRL);
        } catch (IllegalArgumentException e) {
            System.out.println("Sucesso (Valor Negativo): " + e.getMessage());
        }
    }
}