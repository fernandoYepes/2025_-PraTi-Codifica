import java.math.BigDecimal;

public class Gerente extends Funcionario {

    // 1. Construtor que "chama" o construtor da classe mãe (Funcionario)
    public Gerente(String nome, BigDecimal salario) {
        super(nome, salario); // Passa os valores para o construtor do Funcionario
    }

    // 2. Sobrescrita obrigatória do método abstrato
    @Override
    public BigDecimal calcularBonus() {
        // Regra do Gerente: 20% do salário
        // Usamos "this.salario" (que veio da classe mãe)
        // Para multiplicar BigDecimal, usamos .multiply() e new BigDecimal("valor_string")
        return this.salario.multiply(new BigDecimal("0.20"));
    }
}