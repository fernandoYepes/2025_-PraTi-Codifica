/*
50. Desenvolva um pequeno sistema de reserva de hotéis usando JavaScript. O sistema
deverá ser capaz de interagir com o usuário através do console do navegador e manter
um registro das reservas e hotéis disponíveis. Utilize objetos e arrays para gerenciar as
informações. Não é necessário interface gráfica, apenas funcionalidade lógica.
1. Estrutura de Dados:
○ Hotel: Cada hotel deve ser um objeto com propriedades para id, nome,
cidade, quartos totais e quartos disponiveis.
○ Reservas: Cada reserva deve ser um objeto contendo idReserva, idHotel, e
nomeCliente.
2. Funcionalidades:
○ Adicionar hotéis: Permitir que o usuário adicione novos hotéis ao sistema.
○ Buscar hotéis por cidade: Permitir que o usuário liste todos os hotéis
disponíveis em uma cidade específica.
○ Fazer reserva: Permitir que um usuário faça uma reserva em um hotel. Isso
deve diminuir o número de quartos disponiveis do hotel.
○ Cancelar reserva: Permitir que um usuário cancele uma reserva. Isso deve
aumentar o número de quartos disponiveis no hotel correspondente.
○ Listar reservas: Mostrar todas as reservas, incluindo detalhes do hotel e do
cliente.
3. Regras de Negócio:
○ Um hotel só pode aceitar reservas se houver quartos disponíveis.
○ As reservas devem ser identificadas por um ID único e associadas a um
único hotel.

4. Desafios Adicionais (Opcionais):
○ Implementar uma função de check-in e check-out que atualize a
disponibilidade de quartos.
○ Gerar relatórios de ocupação para um hotel.
○ Permitir que o usuário avalie o hotel após a estadia, e armazenar essas
avaliações dentro do objeto do hotel.
 */

const sistemaReservas = {
    hoteis: [],
    reservas: [],
    proximoIdHotel: 1,
    proximoIdReserva: 1,

    // --- FUNÇÕES AUXILIARES ---
    encontrarHotelPorId(id) {
        return this.hoteis.find(hotel => hotel.id === id);
    },

    // --- 1. ESTRUTURA DE DADOS E FUNCIONALIDADES ---
    adicionarHotel(nome, cidade, quartosTotais) {
        if (quartosTotais <= 0) {
            console.error("Erro: O número de quartos totais deve ser positivo.");
            return;
        }

        const novoHotel = {
            id: this.proximoIdHotel,
            nome: nome,
            cidade: cidade,
            quartosTotais: quartosTotais,
            quartosDisponiveis: quartosTotais
        };

        this.hoteis.push(novoHotel);
        this.proximoIdHotel++;
        console.log(`Hotel "${nome}" (ID: ${novoHotel.id}) em ${cidade} adicionado com sucesso!`);
    },

    buscarHoteisPorCidade(cidade) {
        const cidadeBusca = cidade.toLowerCase();
        const hoteisEncontrados = this.hoteis.filter(
            hotel => hotel.cidade.toLowerCase() === cidadeBusca
        );

        if (hoteisEncontrados.length === 0) {
            console.log(`Nenhum hotel encontrado em "${cidade}".`);
            return;
        }

        console.log(`--- Hotéis disponíveis em ${cidade} ---`);
        hoteisEncontrados.forEach(hotel => {
            console.log(`ID: ${hotel.id} | Nome: ${hotel.nome} | Disponíveis: ${hotel.quartosDisponiveis}/${hotel.quartosTotais}`);
        });
        console.log("---------------------------------------");
    },

    fazerReserva(idHotel, nomeCliente) {
        const hotel = this.encontrarHotelPorId(idHotel);

        if (!hotel) {
            console.error(`Erro: Hotel com ID ${idHotel} não encontrado.`);
            return;
        }

        if (hotel.quartosDisponiveis <= 0) {
            console.warn(`Reserva falhou: O hotel "${hotel.nome}" não possui quartos disponíveis.`);
            return;
        }

        hotel.quartosDisponiveis--;

        const novaReserva = {
            idReserva: this.proximoIdReserva,
            idHotel: idHotel,
            nomeCliente: nomeCliente
        };

        this.reservas.push(novaReserva);
        this.proximoIdReserva++;

        console.log(`Reserva ID ${novaReserva.idReserva} para ${nomeCliente} no hotel "${hotel.nome}" confirmada.`);
        console.log(`Quartos restantes em "${hotel.nome}": ${hotel.quartosDisponiveis}`);
    },

    cancelarReserva(idReserva) {
        const indexReserva = this.reservas.findIndex(r => r.idReserva === idReserva);

        if (indexReserva === -1) {
            console.error(`Erro: Reserva com ID ${idReserva} não encontrada.`);
            return;
        }

        const reservaCancelada = this.reservas[indexReserva];
        const hotel = this.encontrarHotelPorId(reservaCancelada.idHotel);

        if (hotel) {
            hotel.quartosDisponiveis++;
            // Log ajustado (sem CSS)
            console.log(`Reserva ${idReserva} cancelada. Quarto liberado no hotel "${hotel.nome}".`);
            console.log(`Quartos restantes em "${hotel.nome}": ${hotel.quartosDisponiveis}`);
        } else {
             console.warn(`Aviso: O hotel (ID ${reservaCancelada.idHotel}) associado à reserva ${idReserva} não foi encontrado, mas a reserva será removida.`);
        }

        this.reservas.splice(indexReserva, 1);
    },

    listarReservas() {
        if (this.reservas.length === 0) {
            console.log("Nenhuma reserva ativa no sistema.");
            return;
        }

        console.log("--- Lista de Todas as Reservas Ativas ---");
        this.reservas.forEach(reserva => {
            const hotel = this.encontrarHotelPorId(reserva.idHotel);
            const nomeHotel = hotel ? hotel.nome : "Hotel Excluído";
            const cidadeHotel = hotel ? hotel.cidade : "N/A";
            
            console.log(`[Reserva ID: ${reserva.idReserva}] Cliente: ${reserva.nomeCliente} | Hotel: ${nomeHotel} (${cidadeHotel})`);
        });
        console.log("-----------------------------------------");
    }
};


console.log("Bem-vindo ao Sistema de Reservas de Hotel!");

// Adicionando hotéis
sistemaReservas.adicionarHotel("Hotel Palace", "São Paulo", 50);
sistemaReservas.adicionarHotel("Hotel Praia", "Rio de Janeiro", 80);
sistemaReservas.adicionarHotel("Hotel Central", "São Paulo", 30);
sistemaReservas.adicionarHotel("Hotel Vista", "Salvador", 40);

// Buscando hotéis por cidade
console.log("\n--- Buscando hotéis em 'São Paulo' ---");
sistemaReservas.buscarHoteisPorCidade("São Paulo");

console.log("\n--- Buscando hotéis em 'Recife' (sem resultados) ---");
sistemaReservas.buscarHoteisPorCidade("Recife");

// Fazendo reservas
console.log("\n--- Fazendo Reservas ---");
sistemaReservas.fazerReserva(1, "Ana Silva"); // Reserva no Hotel Palace (ID 1)
sistemaReservas.fazerReserva(2, "Bruno Costa"); // Reserva no Hotel Praia (ID 2)
sistemaReservas.fazerReserva(1, "Carlos Dias"); // Outra reserva no Hotel Palace (ID 1)

// Listando reservas ativas
console.log("\n--- Listando Reservas Atuais ---");
sistemaReservas.listarReservas();

// Tentando reservar em hotel lotado (Vamos simular um hotel com 1 quarto)
console.log("\n--- Simulando Hotel Lotado ---");
sistemaReservas.adicionarHotel("Hotel Pousada", "Campos do Jordão", 1);
sistemaReservas.fazerReserva(5, "Daniela Lima"); // Reserva ID 4 no Hotel Pousada (ID 5)
sistemaReservas.fazerReserva(5, "Eduardo Moreira"); // Tentativa de reservar hotel lotado

// Verificando a busca por cidade após as reservas
console.log("\n--- Buscando hotéis em 'São Paulo' (disponibilidade atualizada) ---");
sistemaReservas.buscarHoteisPorCidade("São Paulo");

// Cancelando uma reserva
console.log("\n--- Cancelando Reserva ---");
sistemaReservas.cancelarReserva(1); // Cancelando a reserva de Ana Silva (ID 1)

// Verificando a lista de reservas e a disponibilidade do hotel
console.log("\n--- Listando Reservas (Após Cancelamento) ---");
sistemaReservas.listarReservas();

console.log("\n--- Verificando disponibilidade do Hotel Palace (ID 1) ---");
sistemaReservas.buscarHoteisPorCidade("São Paulo");