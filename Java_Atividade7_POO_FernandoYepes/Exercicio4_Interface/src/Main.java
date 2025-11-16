import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {

        System.out.println("### Demonstração de Polimorfismo com Interface ###");

        // 1. A Lista é do tipo da INTERFACE (IMeioTransporte)
        List<IMeioTransporte> veiculos = new ArrayList<>();

        // 2. Adicionamos objetos das CLASSES concretas
        veiculos.add(new Carro(120));
        veiculos.add(new Bicicleta());
        veiculos.add(new Trem(300));

        // 3. Demonstração
        // Percorremos a lista e tratamos todos da mesma forma
        for (IMeioTransporte veiculo : veiculos) {

            // Pega o nome da classe real do objeto (Carro, Bicicleta, etc.)
            System.out.println("\n--- Testando: " + veiculo.getClass().getSimpleName() + " ---");

            try {
                // Acelerando
                veiculo.acelerar(); // Chama o acelerar() do Carro
                veiculo.acelerar(); // Chama o acelerar() da Bicicleta
                veiculo.acelerar(); // Chama o acelerar() do Trem

                // Freando
                veiculo.frear();

                // Forçando uma exceção de "já parado"
                System.out.println("Tentando frear até parar...");
                veiculo.frear();
                veiculo.frear();
                veiculo.frear(); // Esta ou a próxima deve falhar
                veiculo.frear();

            } catch (IllegalStateException e) {
                // 4. Tratando a exceção (operação inválida)
                System.out.println("OPERAÇÃO INVÁLIDA: " + e.getMessage());
            } catch (Exception e) {
                System.out.println("Um erro inesperado ocorreu: " + e.getMessage());
            }
        }

        System.out.println("\n--- Fim da Demonstração ---");
    }
}