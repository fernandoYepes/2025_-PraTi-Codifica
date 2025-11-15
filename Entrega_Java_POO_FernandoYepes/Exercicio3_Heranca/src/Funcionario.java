import java.math.BigDecimal;

// Classe base ABSTRATA. Não podemos criar um "new Funcionario()"
public abstract class Funcionario {

    protected String nome;
    protected BigDecimal salario;

    public Funcionario(String nome, BigDecimal salario) {
        // Validação: Garante que salários sejam positivos
        // Compara o salário com ZERO. Se for 0 ou menor, lança a exceção.
        if (salario == null || salario.compareTo(BigDecimal.ZERO) <= 0) {
            throw new IllegalArgumentException("O salário deve ser um valor positivo.");
        }

        this.nome = nome;
        this.salario = salario;
    }

    // Getters
    public String getNome() {
        return nome;
    }

    public BigDecimal getSalario() {
        return salario;
    }

    /**
     * Método abstrato para o cálculo do bônus.
     * Classes filhas (Gerente, Desenvolvedor) SÃO OBRIGADAS a implementar (sobrescrever) este método.
     */
    public abstract BigDecimal calcularBonus();
}