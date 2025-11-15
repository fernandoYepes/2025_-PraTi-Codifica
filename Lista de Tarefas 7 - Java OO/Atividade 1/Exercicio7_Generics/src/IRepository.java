import java.util.List;
import java.util.Optional;

/**
 * @param <T> O tipo da entidade, que deve ser Identificavel
 * @param <ID> O tipo do ID dessa entidade
 */
public interface IRepository<T extends Identificavel<ID>, ID> {

    // Salva (cria ou atualiza) uma entidade.
    void salvar(T entidade);

    /**
     * Busca uma entidade pelo seu ID.
     * @return um Optional contendo a entidade se encontrada, 
     * ou Optional.empty() se não.
     */
    Optional<T> buscarPorId(ID id);

    List<T> listarTodos();

    /**
     * Remove uma entidade pelo seu ID.
     * @throws EntidadeNaoEncontradaException se o ID não for encontrado.
     */
    void remover(ID id);

}