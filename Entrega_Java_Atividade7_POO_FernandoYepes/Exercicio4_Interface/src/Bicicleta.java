public class Bicicleta implements IMeioTransporte {

    private int velocidadeAtual;
    // A velocidade máxima da bicicleta é fixa (constante)
    private static final int VELOCIDADE_MAXIMA = 30;

    public Bicicleta() {
        this.velocidadeAtual = 0;
    }

    @Override
    public void acelerar() {
        if (velocidadeAtual == VELOCIDADE_MAXIMA) {
            throw new IllegalStateException("A Bicicleta já está na velocidade máxima de " + VELOCIDADE_MAXIMA + "km/h!");
        }

        this.velocidadeAtual += 2; // Bicicleta acelera de 2 em 2
        if(this.velocidadeAtual > VELOCIDADE_MAXIMA) {
            this.velocidadeAtual = VELOCIDADE_MAXIMA;
        }

        System.out.println("Bicicleta acelerou para: " + this.velocidadeAtual + "km/h");
    }

    @Override
    public void frear() {
        if (velocidadeAtual == 0) {
            throw new IllegalStateException("A Bicicleta já está parada!");
        }

        this.velocidadeAtual -= 2; // Bicicleta freia de 2 em 2
        if(this.velocidadeAtual < 0) {
            this.velocidadeAtual = 0;
        }

        System.out.println("Bicicleta freou para: " + this.velocidadeAtual + "km/h");
    }
}