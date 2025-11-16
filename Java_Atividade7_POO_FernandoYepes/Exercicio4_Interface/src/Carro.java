public class Carro implements IMeioTransporte {

    private int velocidadeAtual;
    private final int velocidadeMaxima; // 'final' = o valor não muda após o construtor
    private final int incremento = 10;
    private final int decremento = 10;

    public Carro(int velocidadeMaxima) {
        this.velocidadeAtual = 0;
        this.velocidadeMaxima = velocidadeMaxima;
    }

    @Override
    public void acelerar() {
        if (velocidadeAtual == velocidadeMaxima) {
            // Lança uma exceção se tentar acelerar já estando no máximo
            throw new IllegalStateException("O Carro já está na velocidade máxima de " + velocidadeMaxima + "km/h!");
        }

        // Calcula a nova velocidade, garantindo que não passe do máximo
        this.velocidadeAtual = Math.min(this.velocidadeAtual + incremento, this.velocidadeMaxima);
        System.out.println("Carro acelerou para: " + this.velocidadeAtual + "km/h");
    }

    @Override
    public void frear() {
        if (velocidadeAtual == 0) {
            // Lança uma exceção se tentar frear já estando parado
            throw new IllegalStateException("O Carro já está parado!");
        }

        // Calcula a nova velocidade, garantindo que não fique negativa
        this.velocidadeAtual = Math.max(this.velocidadeAtual - decremento, 0);
        System.out.println("Carro freou para: " + this.velocidadeAtual + "km/h");
    }
}