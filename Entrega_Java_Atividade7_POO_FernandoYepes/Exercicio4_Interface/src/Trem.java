public class Trem implements IMeioTransporte {

    private int velocidadeAtual;
    private final int velocidadeMaxima;

    public Trem(int velocidadeMaxima) {
        this.velocidadeAtual = 0;
        this.velocidadeMaxima = velocidadeMaxima;
    }

    @Override
    public void acelerar() {
        if (velocidadeAtual == velocidadeMaxima) {
            throw new IllegalStateException("O Trem já está na velocidade máxima de " + velocidadeMaxima + "km/h!");
        }

        this.velocidadeAtual += 50; // Trem acelera de 50 em 50
        if(this.velocidadeAtual > velocidadeMaxima) {
            this.velocidadeAtual = velocidadeMaxima;
        }

        System.out.println("Trem acelerou para: " + this.velocidadeAtual + "km/h");
    }

    @Override
    public void frear() {
        if (velocidadeAtual == 0) {
            throw new IllegalStateException("O Trem já está parado!");
        }

        this.velocidadeAtual -= 20; // Trem freia de 20 em 20 (mais lento)
        if(this.velocidadeAtual < 0) {
            this.velocidadeAtual = 0;
        }

        System.out.println("Trem freou para: " + this.velocidadeAtual + "km/h");
    }
}