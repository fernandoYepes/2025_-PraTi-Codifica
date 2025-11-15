import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

public class InMemoryRepository<T extends Identificavel<ID>, ID> implements IRepository<T, ID> {

    // banco
    private final Map<ID, T> storage = new HashMap<>();

    @Override
    public void salvar(T entidade) {
        if (entidade == null) {
            throw new IllegalArgumentException("Entidade não pode ser nula.");
        }
        // O método getId() vem da interface Identificavel
        storage.put(entidade.getId(), entidade);
        System.out.println("Entidade salva: " + entidade.getId());
    }

    @Override
    public Optional<T> buscarPorId(ID id) {
        // Optional.ofNullable() já cria um Optional.empty() se o get(id)
        // retornar null. É o método perfeito para isso.
        return Optional.ofNullable(storage.get(id));
    }

    @Override
    public List<T> listarTodos() {
        // List.copyOf() retorna uma cópia IMUTÁVEL da coleção de valores
        return List.copyOf(storage.values());
    }

    @Override
    public void remover(ID id) {
        if (!storage.containsKey(id)) {
            throw new EntidadeNaoEncontradaException("Falha ao remover: Entidade com ID " + id + " não encontrada.");
        }

        // Se existe, remove
        storage.remove(id);
        System.out.println("Entidade removida: " + id);
    }
}