/**
 * Interface que define o contrato para um meio de transporte.
 * Qualquer classe que implementar esta interface DEVE
 * fornecer implementações para acelerar() e frear().
 */
public interface IMeioTransporte {

    /**
     * Aumenta a velocidade do veículo de acordo com sua regra específica.
     * @throws IllegalStateException se o veículo já estiver na velocidade máxima.
     */
    void acelerar();

    /**
     * Reduz a velocidade do veículo de acordo com sua regra específica.
     * @throws IllegalStateException se o veículo já estiver parado.
     */
    void frear();
}