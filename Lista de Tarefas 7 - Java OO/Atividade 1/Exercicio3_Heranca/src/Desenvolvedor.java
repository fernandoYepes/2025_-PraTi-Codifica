import java.math.BigDecimal;

public class Desenvolvedor extends Funcionario {

    // Construtor que "chama" o construtor da classe mãe (Funcionario)
    public Desenvolvedor(String nome, BigDecimal salario) {
        super(nome, salario); // Passa os valores para o construtor do Funcionario
    }

    // 2. Sobrescrita obrigatória do método abstrato
    @Override
    public BigDecimal calcularBonus() {
        // Regra do Desenvolvedor: 10% do salário
        return this.salario.multiply(new BigDecimal("0.10"));
    }
}