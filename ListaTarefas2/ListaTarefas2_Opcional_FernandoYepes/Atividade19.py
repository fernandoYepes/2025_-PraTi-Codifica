"""
19. Escrever um programa para ler 5 horários. Validar cada horário fornecendo através de
repetição. Escrever cada um deles no formato HH.MM.SS.
"""

print("--- Leitor e Validador de Horários ---")

horarios_validados = []
TOTAL_HORARIOS = 5

print(f"Por favor, digite {TOTAL_HORARIOS} horários válidos (HH, MM, SS).")

for i in range(TOTAL_HORARIOS):
    print(f"\n--- Horário {i + 1} de {TOTAL_HORARIOS} ---")

    while True:
        try:
            h = int(input(f"Digite as HORAS (0-23) para o {i+1}º horário: "))
            if 0 <= h <= 23:
                break
            else:
                print("Erro: Hora inválida. O valor deve ser entre 0 e 23.")
        except ValueError:
            print("Erro: Entrada inválida. Digite um número inteiro.")

    while True:
        try:
            m = int(input(f"Digite os MINUTOS (0-59) para o {i+1}º horário: "))
            if 0 <= m <= 59:
                break
            else:
                print("Erro: Minuto inválido. O valor deve ser entre 0 e 59.")
        except ValueError:
            print("Erro: Entrada inválida. Digite um número inteiro.")

    while True:
        try:
            s = int(input(f"Digite os SEGUNDOS (0-59) para o {i+1}º horário: "))
            if 0 <= s <= 59:
                break
            else:
                print("Erro: Segundo inválido. O valor deve ser entre 0 e 59.")
        except ValueError:
            print("Erro: Entrada inválida. Digite um número inteiro.")

    horario_formatado = f"{h:02d}.{m:02d}.{s:02d}"
    horarios_validados.append(horario_formatado)
    print(f"Horário {horario_formatado} validado e armazenado.")


print("\n" + "=" * 30)
print(f"--- Os {TOTAL_HORARIOS} Horários Armazenados ---")
print("=" * 30)

for horario in horarios_validados:
    print(horario)