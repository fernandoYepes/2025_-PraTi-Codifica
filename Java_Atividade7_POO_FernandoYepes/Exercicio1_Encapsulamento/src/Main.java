 public static void main(String[] args) {

        System.out.println("### Demonstração de Encapsulamento - Classe Produto ###");

        // Criando instâncias válidas
        System.out.println("\n--- 1. Testes Válidos ---");
        Produto p1 = null;
        try {
            p1 = new Produto("Notebook", 4500.00, 10);
            System.out.println("Produto criado: " + p1);
        } catch (IllegalArgumentException e) {
            System.out.println("Erro inesperado ao criar p1: " + e.getMessage());
        }

        // Alterando valores com dados válidos
        if (p1 != null) {
            try {
                p1.setPreco(4350.50);
                p1.setQuantidadeEmEstoque(8);
                System.out.println("Produto alterado: " + p1);
            } catch (IllegalArgumentException e) {
                System.out.println("Erro inesperado ao alterar p1: " + e.getMessage());
            }
        }

        // Usamos blocos try-catch para "capturar" as exceções e
        // impedir que o programa pare de executar.

        System.out.println("\n--- 2. Testes Inválidos (Esperando Exceções) ---");

        // Nome nulo
        try {
            Produto pInvalido1 = new Produto(null, 10.0, 5);
            System.out.println("ERRO NO TESTE: Produto com nome nulo foi criado." + pInvalido1);
        } catch (IllegalArgumentException e) {
            System.out.println("Sucesso (Nome Nulo): " + e.getMessage());
        }

        // Nome vazio
        try {
            Produto pInvalido2 = new Produto("   ", 20.0, 15); // Nome apenas com espaços
            System.out.println("ERRO NO TESTE: Produto com nome vazio foi criado." + pInvalido2);
        } catch (IllegalArgumentException e) {
            System.out.println("Sucesso (Nome Vazio): " + e.getMessage());
        }

        // Preço negativo
        try {
            Produto pInvalido3 = new Produto("Teclado", -99.90, 30);
            System.out.println("ERRO NO TESTE: Produto com preço negativo foi criado." + pInvalido3);
        } catch (IllegalArgumentException e) {
            System.out.println("Sucesso (Preço Negativo): " + e.getMessage());
        }

        // Teste: Quantidade negativa (usando um setter)
        try {
            p1.setQuantidadeEmEstoque(-5); // Usando o produto p1 já criado
            System.out.println("ERRO NO TESTE: Quantidade negativa foi definida.");
        } catch (IllegalArgumentException e) {
            System.out.println("Sucesso (Quantidade Negativa): " + e.getMessage());
        }

        System.out.println("\n--- Fim dos Testes ---");
    }
