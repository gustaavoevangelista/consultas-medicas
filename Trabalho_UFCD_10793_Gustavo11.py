#-------------------------------------------------------------------------------
# Name:        Clínica Médica
# Purpose:     Marcação de consultas e procedimentos relacionados a uma clinica médica
#
# Author:      GUSTAVO EVANGELISTA
#
# Created:     16/05/2022
# Copyright:   (c) GUSTAVO 2022
#-------------------------------------------------------------------------------

# -*- coding: UTF-8 -*-
import time
import os
import valores
import math

os.system("color F2") #letra com cor verde e fundo branco


def valor_especialidade(preco): #funcao para aumentar o valor da consulta com especialista
    return preco + 80


def consulta(): #funcao para reunir detalhes da consulta
    escolha = input("Pretende ter atendimento com um clinico geral ou com especialista? ")
    print("\n")

    if ((escolha == "Clínico geral") or (escolha == "clínico geral") or (escolha == "Clinico geral") or (escolha == "clinico geral")):

        medico = ["Miguel Duarte", "Gonçalo Ribeiro", "Joaquim Nascimento"]

        x=len(medico)
        print("Lista de médicos:\n")
        for x in medico:
            print("\t-" , x)

        medico = input("Por favor, escolha um dos médicos...")

        data = input("Insira a data pretendida: ")

        global valor
        valor = valores.valor_clinico() # valor fornecido a partir da biblioteca "valores"
        global resultado
        resultado = valor_total(valor)

        print("\nResumo da marcação:\n\tMédico:" , medico, "\n\tData:", data, "\n\tValor da consulta:", valor)


    elif((escolha == "Especialista") or (escolha == "especialista")):  #caso o usuário escolha um especialista, o valor da consulta é aumentado

        especialidade = input("Escolha a especialidade: ")
        medico = input("Insira o nome do médico que pretende ter a consulta: ")
        data = input("Insira a data pretendida: ")

        valor = math.sqrt(6400.0) # funcao raiz quadrada importada da biblioteca padrão "math"
        print(valor_especialidade(valor))

        resultado = valor_total(valor)

        print("\nResumo da marcação:\n\tMédico:" , medico, "\n\tData:", data, "\n\tValor da consulta:", valor_especialidade(valor))


    else:
        print("Opção inválida... escolha novamente.")


def analises(): #funcao para marcar analises
    enfermeiro = "Letícia Evangelista"
    data = input("Insira a data pretendida: ")

    global valor
    valor = valores.valor_analise() # valor fornecido a partir da biblioteca "valores"
    global resultado
    resultado = valor_total(valor)

    print("\nResumo da marcação:\n\tEnfemeiro:" , enfermeiro, "\n\tData:", data, "\n\tValor das análises:", valor)


def ressonancia(): #funcao para marcar ressonancia
    tecnico = "Lucas Fernandes"
    data = input("Insira a data pretendida: ")

    global valor
    valor = valores.valor_ressonancia() # valor fornecido a partir da biblioteca "valores"
    global resultado
    resultado = valor_total(valor)
    print("\nResumo da marcação:\n\tTécnico:" , tecnico, "\n\tData:", data, "\n\tValor da ressonância:", valor)


def menu (): # função para imprimir o menu no ecrã
    print("Lista de serviços:")
    time.sleep(1)
    print("\n1- Marcar consulta")
    print("2- Análises de sangue")
    print("3- Ressonância")
    print("4- Sair do programa")
    global opcao

    opcao = int(input("\nSelecione umas das opções: "))


def valor_total(valor): #funcao para acumular o valor total das marcacoes
    global total
    if (total == "a"):
        total = 0
        total =total + valor
        return total

    else:

        total =total + valor
        return total


def iniciando(n):  # funcao recursiva de contagem regressiva para iniciar o programa
    if n < 2:
        return "1"
    else:
        print (n)
        time.sleep(1)
        return iniciando(n-1)

#aqui começa o programa
total = "a"
print("\tYOUR BEST LIFE CLÍNICA MÉDICA")
print("-"*40)
print("\n")

n=3
print("Aguarde enquanto iniciamos o programa, demora apenas 3 segundos :) ")
print(iniciando(n))

print("Bem vindo(a)\n")
menu()

continuar = "s"
m= 0
counter = 0

while (True):   #ficar em ciclo até o utilizador não querer fazer mais marcações

    if m == 1:
        menu()

    m = 1

    if (opcao == 1):
        consulta()
        counter = counter + 1   #contando o numero de marcações


    elif (opcao == 2):
        analises()
        counter = counter + 1   #contando o numero de marcações


    elif (opcao == 3):
        ressonancia()
        counter = counter + 1   #contando o numero de marcações


    elif(opcao == 4):
        print("Obrigado pela preferência. Volte sempre!")
        break


    else: #volta para o menu e escolhe novamente uma opção
        print("Opção inválida... escolha novamente.")
        menu()
        opcao = int(input("\nSelecione umas das opções: "))
        print("\n")
        continue


    continuar = input ("\nDeseja fazer outra marcação? (sim | nao) \n")

    if (continuar == "s" or continuar == "S" or continuar == "Sim" or continuar == "sim"):
        m=1

    else:

        print("\nVocê fez",counter,"marcação(ões) com um total de",resultado,"euros.")
        print("\nNos vemos em breve, até logo!")

        break
