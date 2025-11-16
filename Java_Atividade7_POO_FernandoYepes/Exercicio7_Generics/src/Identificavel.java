/**
 * Interface para entidades que possuem um Identificador (ID).
 * @param <ID> O tipo do identificador (ex: Long, Integer, String)
 */
public interface Identificavel<ID> {

    ID getId();

}