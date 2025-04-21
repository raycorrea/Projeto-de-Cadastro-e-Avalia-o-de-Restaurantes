from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Rayan', 9)
restaurante_praca.receber_avaliacao('Lívia', 10)
restaurante_praca.receber_avaliacao('Emy', 2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()