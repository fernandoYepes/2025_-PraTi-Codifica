import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {

        System.out.println("### Demonstração de Herança e Polimorfismo ###");

        // A lista é do tipo "Funcionario" (tipo base)
        List<Funcionario> funcionarios = new ArrayList<>();

        // Adicionamos objetos dos tipos filhos (Gerente, Desenvolvedor)
        try {
            funcionarios.add(new Gerente("Ana Costa", new BigDecimal("12000.00")));
            funcionarios.add(new Desenvolvedor("Bruno Silva", new BigDecimal("7500.00")));
            funcionarios.add(new Desenvolvedor("Carla Dias", new BigDecimal("8200.00")));
            funcionarios.add(new Gerente("David Martins", new BigDecimal("15000.00")));

        } catch (IllegalArgumentException e) {
            System.out.println("Erro ao cadastrar funcionário: " + e.getMessage());
        }


        System.out.println("\n--- Cálculo de Bônus (Polimorfismo) ---");


        for (Funcionario f : funcionarios) {
            // f.getClass().getSimpleName() -> Pega o nome da classe (Gerente ou Desenvolvedor)
            System.out.printf("Funcionário: %s (%s) \n", f.getNome(), f.getClass().getSimpleName());

            System.out.printf("Salário: R$ %.2f \n", f.getSalario());

            // f.calcularBonus() -> POLIMORFISMO EM AÇÃO
            System.out.printf("Bônus: R$ %.2f \n", f.calcularBonus());
            System.out.println("--------------------");
        }

        System.out.println("\n--- Teste de Validação (Salário Inválido) ---");
        try {
            Funcionario invalido = new Gerente("Sr. Negativo", new BigDecimal("-1000.00"));
            System.out.println("ERRO NO TESTE: Funcionário com salário negativo foi criado.");
        } catch (IllegalArgumentException e) {
            System.out.println("Sucesso (Exceção capturada): " + e.getMessage());
        }
    }
}