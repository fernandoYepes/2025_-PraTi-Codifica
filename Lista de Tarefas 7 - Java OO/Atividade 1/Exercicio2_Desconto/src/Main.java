public class Main {

    public static void main(String[] args) {

        System.out.println("### Demonstração de Encapsulamento - Desconto (Ex 2) ###");

        // --- 1. Teste de Desconto Válido (10%) ---
        System.out.println("\n--- Teste 1: Desconto Válido (10%) ---");
        try {
            // Criamos um produto base para o teste
            Produto tv = new Produto("Smart TV 50\"", 3000.00, 5);
            System.out.println("Preço Original: " + tv.getPreco());

            // Ação: Aplicando 10% de desconto
            tv.aplicarDesconto(10.0);

            // Verificação: Esperado 2700.0
            System.out.println("Preço com 10% de desconto: " + tv.getPreco());

        } catch (IllegalArgumentException e) {
            System.out.println("ERRO INESPERADO no teste válido: " + e.getMessage());
        }

        // --- 2. Teste de Desconto Inválido (Acima de 50%) ---
        System.out.println("\n--- Teste 2: Desconto Inválido (> 50%) ---");
        try {
            Produto fone = new Produto("Fone Bluetooth", 500.00, 20);
            System.out.println("Preço Original: " + fone.getPreco());

            // Ação: Tentando aplicar 50.1% (Inválido)
            fone.aplicarDesconto(50.1);

            // Se o código chegar aqui, o teste falhou
            System.out.println("ERRO NO TESTE: Desconto inválido (50.1%) foi aplicado.");
        } catch (IllegalArgumentException e) {
            // Verificação: Exceção foi capturada com sucesso
            System.out.println("Sucesso (Exceção capturada): " + e.getMessage());
        }

        // --- 3. Teste de Desconto Inválido (Negativo) ---
        System.out.println("\n--- Teste 3: Desconto Inválido (Negativo) ---");
        try {
            Produto mouse = new Produto("Mouse Gamer", 250.00, 15);
            System.out.println("Preço Original: " + mouse.getPreco());

            // Ação: Tentando aplicar -10% (Inválido)
            mouse.aplicarDesconto(-10.0);

            // Se o código chegar aqui, o teste falhou
            System.out.println("ERRO NO TESTE: Desconto negativo (-10.0) foi aplicado.");
        } catch (IllegalArgumentException e) {
            // Verificação: Exceção foi capturada com sucesso
            System.out.println("Sucesso (Exceção capturada): " + e.getMessage());
        }

        System.out.println("\n--- Fim dos Testes (Ex 2) ---");
    }
}