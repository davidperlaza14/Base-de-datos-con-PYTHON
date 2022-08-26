from cities import Countries

paises = Countries()

menu='''\n****************************
*       MENU PAISES        *
****************************
*                          *
*  i) Insertar País        *
*  e) Eliminar País        *
*  m) Modificar País       *
*  p) Imprimir Paises      *
*  x) Salir                *
*                          *
****************************'''

def main():
    opcion = '0'
    while opcion != 'X':
        print(menu)
        opcion = input("Que opcion deseas?").upper()
        print()
        if opcion == 'I':
            print("*****  Insertar Paises  *****")
            ISO3 = input("Introduce la clave ISO3 del nuevo País: ")
            CountryName = input("Introduce el nombre del nuevo País: ")
            Capital = input("Introduce la capital del nuevo País: ")
            CurrencyCode = input("Introduce el código de su moneda: ")
            r = paises.inserta_ciudad(ISO3,CountryName,Capital,CurrencyCode)
            if (r==0):
                print("El pais no se pudo insertar.")
            else:
                print("El pais se inserto correctamente.")

        elif opcion == 'E':
            print("*****  Eliminar País  *****")
            Id = int(input("Introduce el Id del país que desea eliminar: "))
            r = paises.eliminar_ciudad(Id)
            if (r==0):
                print("El pais no existe")
            else:
                print("El pais se elimino.")
        elif opcion == 'M':
            print("*****  Modificar País  *****")
            Id = int(input("Introduce el Id del país que desea modificar: "))
            pais = paises.buscar_pais(Id)
            if pais == None:
                print("->  El pais no existe.")
            else:
                print("*** Pais a modificar: ")
                print(pais)
                ISO3 = input("Introduce la nueva clave ISO3 del nuevo País: ")
                CountryName = input("Introduce el nuevo nombre del nuevo País: ")
                Capital = input("Introduce la nueva capital del nuevo País: ")
                CurrencyCode = input("Introduce el nuevo código de su moneda: ")
                paises.modificar_pais(Id,ISO3,CountryName,Capital,CurrencyCode)

        elif opcion == 'P':
            print("*****  Imprimir País  *****")
            print(paises)
        elif opcion == 'X':
            print("*****  Salir  *****")
        else:
            print("-> Opcion no valida")



if __name__ == "__main__":
    main()

            
            


