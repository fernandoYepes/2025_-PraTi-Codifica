/**
 * Entidade de Produto (usando record).
 * Implementa Identificavel com um ID do tipo Long.
 */
public record Produto(Long id, String nome) implements Identificavel<Long> {

    @Override
    public Long getId() {
        return this.id;
    }
}