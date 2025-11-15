import java.util.List;
import java.util.Optional;

public class Main {
    public static void main(String[] args) {

        System.out.println("### Testando Repositório Genérico com Produtos (ID: Long) ###");

        IRepository<Produto, Long> repoProdutos = new InMemoryRepository<>();

        // Salvando
        repoProdutos.salvar(new Produto(1L, "Notebook"));
        repoProdutos.salvar(new Produto(2L, "Mouse"));

        // Listando
        List<Produto> produtos = repoProdutos.listarTodos();
        System.out.println("Listagem de produtos: " + produtos);

        // Buscando
        Optional<Produto> p1 = repoProdutos.buscarPorId(1L);
        p1.ifPresent(p -> System.out.println("Produto 1 encontrado: " + p.nome()));

        // Removendo
        try {
            repoProdutos.remover(2L); // Remove o Mouse
            System.out.println("Listagem após remoção: " + repoProdutos.listarTodos());
        } catch (EntidadeNaoEncontradaException e) {
            System.out.println(e.getMessage());
        }

        // Removendo (com falha)
        try {
            repoProdutos.remover(99L); // ID 99 não existe
        } catch (EntidadeNaoEncontradaException e) {
            System.out.println("Sucesso (Exceção capturada): " + e.getMessage());
        }

        // Teste de Imutabilidade da Lista
        try {
            produtos.add(new Produto(3L, "Monitor")); // Tenta adicionar na lista
        } catch (UnsupportedOperationException e) {
            System.out.println("Sucesso (Imutabilidade): A lista retornada por listarTodos() é imutável.");
        }

        System.out.println("\n### Testando com Funcionários (ID: String) ###");

        IRepository<Funcionario, String> repoFuncionarios = new InMemoryRepository<>();

        // Salvando
        repoFuncionarios.salvar(new Funcionario("123.456.789-00", "Ana Silva"));

        // Buscando
        Optional<Funcionario> f1 = repoFuncionarios.buscarPorId("123.456.789-00");
        f1.ifPresent(f -> System.out.println("Funcionária encontrada: " + f.nome()));
    }
}