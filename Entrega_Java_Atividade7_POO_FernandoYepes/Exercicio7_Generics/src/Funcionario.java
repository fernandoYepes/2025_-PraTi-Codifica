// Entidade Funcionario (usando record).
// Implementa Identificavel com um ID do tipo String (CPF).
public record Funcionario(String cpf, String nome) implements Identificavel<String> {

    @Override
    public String getId() {
        return this.cpf;
    }
}