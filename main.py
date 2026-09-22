def exibir_menu():
    print("\n--- SISTEMA DE GESTÃO DE PEÇAS E QUALIDADE ---")
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("0. Sair")

# Listas globais para armazenar os dados do sistema
pecas_aprovadas = []
pecas_reprovadas = []
caixas_fechadas = []
caixa_atual = []

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print("\n--- CADASTRO DE NOVA PEÇA ---")
            id_peca = input("Digite o ID da peça: ")
            
            try:
                peso = float(input("Digite o peso da peça (g): "))
                comprimento = float(input("Digite o comprimento da peça (cm): "))
            except ValueError:
                print("Erro: Peso e comprimento devem ser números válidos!")
                continue
                
            cor = input("Digite a cor da peça (ex: azul, verde): ").strip().lower()
            
            # Verificando os critérios de qualidade do trabalho
            motivos_reprovacao = []
            
            if not (95 <= peso <= 105):
                motivos_reprovacao.append(f"Peso inválido ({peso}g - esperado entre 95g e 105g)")
            
            if cor not in ["azul", "verde"]:
                motivos_reprovacao.append(f"Cor inválida ('{cor}' - esperado azul ou verde)")
                
            if not (10 <= comprimento <= 20):
                motivos_reprovacao.append(f"Comprimento inválido ({comprimento}cm - esperado entre 10cm e 20cm)")
            
            # Se a lista estiver vazia, a peça foi Aprovada
            if len(motivos_reprovacao) == 0:
                peca = {"id": id_peca, "peso": peso, "cor": cor, "comprimento": comprimento}
                pecas_aprovadas.append(peca)
                caixa_atual.append(peca)
                print(f"\n[SUCESSO] Peça {id_peca} APROVADA e adicionada à caixa atual!")
                
                # Regra: fechar a caixa se atingir 10 peças
                if len(caixa_atual) == 10:
                    caixas_fechadas.append(caixa_atual.copy())
                    caixa_atual.clear()
                    print("[AVISO] A caixa atingiu o limite de 10 peças e foi fechada! Uma nova caixa foi aberta.")
            else:
                # Se houver motivos, a peça foi Reprovada
                motivo_completo = ", ".join(motivos_reprovacao)
                peca = {"id": id_peca, "peso": peso, "cor": cor, "comprimento": comprimento, "motivo": motivo_completo}
                pecas_reprovadas.append(peca)
                print(f"\n[REPROVADA] Peça {id_peca} reprovada pelos seguintes motivos: {motivo_completo}")

        elif opcao == "2":
            print("\n--- LISTA DE PEÇAS ---")
            print(f"Total de peças aprovadas armazenadas: {len(pecas_aprovadas)}")
            if len(pecas_aprovadas) > 0:
                print("\nPeças Aprovadas:")
                for p in pecas_aprovadas:
                    print(f" - ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comp: {p['comprimento']}cm")
            else:
                print("\nNenhuma peça aprovada no momento.")
                
            print(f"\nTotal de peças reprovadas: {len(pecas_reprovadas)}")
            if len(pecas_reprovadas) > 0:
                print("\nPeças Reprovadas:")
                for p in pecas_reprovadas:
                    print(f" - ID: {p['id']} | Motivo(s): {p['motivo']}")
            else:
                print("Nenhuma peça reprovada no momento.")

        elif opcao == "3":
            print("\n--- REMOVER PEÇA CADASTRADA ---")
            id_remover = input("Digite o ID da peça que deseja remover: ")
            
            removida = False
            
            for p in pecas_aprovadas:
                if p['id'] == id_remover:
                    pecas_aprovadas.remove(p)
                    removida = True
                    break
                    
            if not removida:
                for p in caixa_atual:
                    if p['id'] == id_remover:
                        caixa_atual.remove(p)
                        removida = True
                        break
                        
            if not removida:
                for p in pecas_reprovadas:
                    if p['id'] == id_remover:
                        pecas_reprovadas.remove(p)
                        removida = True
                        break
                        
            if removida:
                print(f"\n[SUCESSO] Peça com ID '{id_remover}' foi removida do sistema.")
            else:
                print(f"\n[ERRO] Nenhuma peça com o ID '{id_remover}' foi encontrada.")

        elif opcao == "4":
            print("\n--- LISTA DE CAIXAS FECHADAS ---")
            print(f"Quantidade de caixas fechadas: {len(caixas_fechadas)}")
            
            if len(caixas_fechadas) > 0:
                for i, caixa in enumerate(caixas_fechadas, 1):
                    print(f"\nCaixa Fechada #{i} (Contém {len(caixa)} peças):")
                    for p in caixa:
                        print(f"   -> Peça ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']}")
            else:
                print("Nenhuma caixa foi fechada ainda (cada caixa precisa de 10 peças aprovadas).")
                
            print(f"\n[Status da Caixa Atual]: Contém {len(caixa_atual)} peça(s) (Aguardando atingir 10).")

        elif opcao == "5":
            print("\n========================================")
            print("       RELATÓRIO CONSOLIDADO FINAL      ")
            print("========================================")
            print(f"Total de peças aprovadas: {len(pecas_aprovadas)}")
            print(f"Total de peças reprovadas: {len(pecas_reprovadas)}")
            print(f"Total de caixas fechadas: {len(caixas_fechadas)}")
            print(f"Peças na caixa atual (em andamento): {len(caixa_atual)}")
            
            if len(pecas_reprovadas) > 0:
                print("\nDetalhamento das Reprovações:")
                for p in pecas_reprovadas:
                    print(f" - Peça ID {p['id']}: {p['motivo']}")
            print("========================================")

        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()