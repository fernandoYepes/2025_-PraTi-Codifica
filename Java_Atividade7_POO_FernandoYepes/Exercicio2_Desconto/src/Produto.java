public class Produto {

    // Atributos (do Ex 1)
    private String nome;
    private double preco;
    private int quantidadeEmEstoque;

    // Construtor (do Ex 1)
    public Produto(String nome, double preco, int quantidadeEmEstoque) {
        this.setNome(nome);
        this.setPreco(preco);
        this.setQuantidadeEmEstoque(quantidadeEmEstoque);
    }

    // Getters e Setters (do Ex 1)
    public String getNome() {
        return nome;
    }

    public double getPreco() {
        return preco;
    }

    public int getQuantidadeEmEstoque() {
        return quantidadeEmEstoque;
    }

    public void setNome(String nome) {
        if (nome == null || nome.trim().isEmpty()) {
            throw new IllegalArgumentException("Nome não pode ser nulo ou vazio.");
        }
        this.nome = nome;
    }

    public void setPreco(double preco) {
        if (preco < 0) {
            throw new IllegalArgumentException("Preço não pode ser negativo.");
        }
        this.preco = preco;
    }

    public void setQuantidadeEmEstoque(int quantidadeEmEstoque) {
        if (quantidadeEmEstoque < 0) {
            throw new IllegalArgumentException("Quantidade em estoque não pode ser negativa.");
        }
        this.quantidadeEmEstoque = quantidadeEmEstoque;
    }

    // Método toString (opcional, mas bom)
    @Override
    public String toString() {
        return "Produto{" +
                "nome='" + nome + '\'' +
                ", preco=" + preco +
                ", quantidadeEmEstoque=" + quantidadeEmEstoque +
                '}';
    }


    // --- MÉTODO DO EXERCÍCIO 2 ---

    /**
     * Aplica um desconto ao preço do produto.
     *
     * @param porcentagem O desconto a ser aplicado (deve estar entre 0.0 e 50.0).
     * @throws IllegalArgumentException Se a porcentagem for inválida.
     */
    public void aplicarDesconto(double porcentagem) {
        // 1. Validação da regra de negócio (entre 0% e 50%)
        if (porcentagem < 0 || porcentagem > 50) {
            throw new IllegalArgumentException(
                    "Porcentagem de desconto inválida. Deve ser um valor entre 0 e 50."
            );
        }

        // 2. Cálculo e aplicação do desconto
        double fatorDesconto = 1.0 - (porcentagem / 100.0);
        this.preco *= fatorDesconto;
    }
}