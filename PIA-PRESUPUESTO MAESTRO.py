import matplotlib.pyplot as plt

separador = ('-' * 45)

print('\nBienvenido(a), aqui podras calcular el Presupuesto Maestro, EMPECEMOS!')
print('Este programa, fue programado para calcularlo en 2 semestres con 3 productos\n')
print("Tambien en este programa, se reciclaran datos que una vez se obtengan, no sea necesario volver a ingresar, solo ingrese lo que se pida")

while True:
    print('\n--------- Guardado de datos de los productos ---------')
    PrimerProducto = input("\nIngrese el nombre que le dara al 1er producto\n» Producto ")
    SegundoProducto = input("\nIngrese el nombre que le dara al 2do producto\n» Producto ")
    TercerProducto = input("\nIngrese el nombre que le dara al 3er producto\n» Producto ")
    AñoAnt = input("\nIngrese el año anterior (ej. ####) del que se calculara el Presupuesto Maestro\n» ")
    AñoAct = input("\nIngrese el año actual (ej. ####) del que se calculara el Presupuesto Maestro\n» ")

    print('\n--------- Presupuesto de Operación ---------')
    PreModulo1 = int(input("\nA continuacion se empezara en el Modulo 1.Presupuesto de Ventas. ¿Desea continuar? \n\t[1]Si \n\t[2]No\n» "))

    # Módulo 1
    if PreModulo1 == 1:
        print('\n--------- ENTRANDO AL MODULO 1 ---------')
        print('\n--------- Presupuesto de Ventas ---------')
        print("\nPrimero se ingresará el 1er Semestre\n")
        #  S1P1         S1 : Semestre 1, P1 : Producto 1
        Unidadesavender_S1P1 = float(input(f'Ingrese las unidades a vender del producto {PrimerProducto} 1er. Semestre\n» '))
        Preciodeventa_S1P1 = float(input(f'Ingrese el precio de venta del producto {PrimerProducto} 1er. Semestre\n» $'))
        Importedeventa_S1P1 = (Unidadesavender_S1P1*Preciodeventa_S1P1)
        #  S1P2         S1 : Semestre 1, P2 : Producto 2
        Unidadesavender_S1P2 = float(input(f'Ingrese las unidades a vender del producto {SegundoProducto} 1er. Semestre\n» '))
        Preciodeventa_S1P2 = float(input(f'Ingrese el precio de venta del producto {SegundoProducto} 1er. Semestre\n» $'))
        Importedeventa_S1P2 = (Unidadesavender_S1P2*Preciodeventa_S1P2)
        #  S1P3         S1 : Semestre 1, P3 : Producto 3
        Unidadesavender_S1P3 = float(input(f'Ingrese las unidades a vender del producto {TercerProducto} 1er. Semestre\n» '))
        Preciodeventa_S1P3 = float(input(f'Ingrese el precio de venta del producto {TercerProducto} 1er. Semestre\n» $'))
        Importedeventa_S1P3 = (Unidadesavender_S1P3*Preciodeventa_S1P3)
        Totaldeventas1S = (Importedeventa_S1P1+Importedeventa_S1P2+Importedeventa_S1P3)
        print("\nAhora se ingresará del 2do Semestre\n")
        #  S2P1         S2 : Semestre 2, P1 : Producto 1
        Unidadesavender_S2P1 = float(input(f'Ingrese las unidades a vender del producto {PrimerProducto} 2do. Semestre\n» '))
        Preciodeventa_S2P1 = float(input(f'Ingrese el precio de venta del producto {PrimerProducto} 2do. Semestre\n» $'))
        Importedeventa_S2P1 = (Unidadesavender_S2P1*Preciodeventa_S2P1)
        #  S2P2         S2 : Semestre 2, P2 : Producto 2
        Unidadesavender_S2P2 = float(input(f'Ingrese las unidades a vender del producto {SegundoProducto} 2do. Semestre\n» '))
        Preciodeventa_S2P2 = float(input(f'Ingrese el precio de venta del producto {SegundoProducto} 2do. Semestre\n» $'))
        Importedeventa_S2P2 = (Unidadesavender_S2P2*Preciodeventa_S2P2)
        #  S2P3         S2 : Semestre 2, P3 : Producto 3
        Unidadesavender_S2P3 = float(input(f'Ingrese las unidades a vender del producto {TercerProducto} 2do. Semestre\n» '))
        Preciodeventa_S2P3 = float(input(f'Ingrese el precio de venta del producto {TercerProducto} 2do. Semestre\n» $'))
        Importedeventa_S2P3 = (Unidadesavender_S2P3*Preciodeventa_S2P3)
        Totaldeventas2S = (Importedeventa_S2P1+Importedeventa_S2P2+Importedeventa_S2P3)
        # Ahora se calculara el total del año
        TotaldelImportedeVentaP1 = (Importedeventa_S1P1+Importedeventa_S2P1)
        TotaldelImportedeVentaP2 = (Importedeventa_S1P2+Importedeventa_S2P2)
        TotaldelImportedeVentaP3 = (Importedeventa_S1P3+Importedeventa_S2P3)
        TotaldeVentasdelaño = (Totaldeventas1S+Totaldeventas2S)

        # Mostrar tabla
        fig, ax = plt.subplots(figsize=(13, 6), dpi=100)
        data = [["PRODUCTO " + PrimerProducto, "","",""],
            ["Unidades a vender",str(Unidadesavender_S1P1),str(Unidadesavender_S2P1),""],
            ["Precio de venta","$"+str(Preciodeventa_S1P1),"$"+str(Preciodeventa_S2P1),""],
            ["Importe de venta","$"+str(Importedeventa_S1P1),"$"+str(Importedeventa_S2P1),"$"+str(TotaldelImportedeVentaP1)],
            ["","","",""],
            ["PRODUCTO " + SegundoProducto, "","",""],
            ["Unidades a vender",str(Unidadesavender_S1P2),str(Unidadesavender_S2P2),""],
            ["Precio de venta","$"+str(Preciodeventa_S1P2),"$"+str(Preciodeventa_S2P2),""],
            ["Importe de venta","$"+str(Importedeventa_S1P2),"$"+str(Importedeventa_S2P2),"$"+str(TotaldelImportedeVentaP2)],
            ["","","",""],
            ["PRODUCTO " + TercerProducto, "","",""],
            ["Unidades a vender",str(Unidadesavender_S1P3),str(Unidadesavender_S2P3),""],
            ["Precio de venta","$"+str(Preciodeventa_S1P3),"$"+str(Preciodeventa_S2P3),""],
            ["Importe de venta","$"+str(Importedeventa_S1P3),"$"+str(Importedeventa_S2P3),"$"+str(TotaldelImportedeVentaP3)],
            ["Total de Ventas por Semestre","$"+str(Totaldeventas1S),"$"+str(Totaldeventas2S),"$"+str(TotaldeVentasdelaño)],
            ["","","",""]]
        column_labels = ["", "1er. Semestre", "2do. Semestre", "Total "+AñoAct]
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText = data, colLabels = column_labels, loc="center")
        table.set_fontsize(24)
        table.scale(1.2, 1.6)
        plt.title("1. Presupuesto de Ventas")
        plt.show()

    elif PreModulo1 == 2:
        break

    # Módulo 2
    PreModulo2 = int(input("\nA continuacion sigue el Modulo 2.Determinación del saldo de Clientes y Flujo de Entradas. ¿Desea continuar? \n\t[1]Si \n\t[2]No\n» "))
    if PreModulo2 == 1:
        print('\n\t\t--------- ENTRANDO AL MODULO 2 ---------')
        print('\n--------- Determinación del saldo de Clientes y Flujo de Entradas ---------\n')
        SaldodeClientes = float(input(f"Ingrese el saldo total de clientes del {AñoAnt}\n» $"))
        TotaldeClientes =(SaldodeClientes+TotaldeVentasdelaño)
        print("Entradas de Efectivo ↓")
        CobranzaAñoAnt = float(input(f"Ingrese el importe de cobranza del {AñoAnt}\n» $"))
        CobranzaAñoAct = float(input(f"Ingrese el importe de cobranza del {AñoAct}\n» $"))
        TotaldeEntradas = (CobranzaAñoAnt+CobranzaAñoAct)
        SaldodeClientesAñoAct = (TotaldeClientes-TotaldeEntradas)

        # Mostrar tabla
        fig, ax = plt.subplots(figsize=(13, 6), dpi=100)
        data = [["Saldo de clientes "+str(AñoAnt),"","$"+str(SaldodeClientes)],
            ["Ventas "+str(AñoAct),"","$"+str(TotaldeVentasdelaño)],
            ["Total de Clientes "+str(AñoAct),"","$"+str(TotaldeClientes)],
            ["","",""],
            ["Entradas de Efectivo:","",""],
            ["Por Cobranza del "+str(AñoAnt),"$"+str(CobranzaAñoAnt),""],
            ["Por Cobranza del "+str(AñoAct),"$"+str(CobranzaAñoAct),""],
            ["Total de Entradas "+AñoAct,"","$"+str(TotaldeEntradas)],
            ["","",""],
            ["Saldo de Clientes del "+AñoAct,"","$"+str(SaldodeClientesAñoAct)]]
        column_labels = ["Descripción", "Importe", "Total"]
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText = data, colLabels = column_labels, loc="center")
        table.set_fontsize(24)
        table.scale(1.2, 1.8)
        plt.title("2. Determinación del saldo de Clientes y Flujo de Entradas")
        plt.show()

    elif PreModulo2 == 2:
        break

    # Módulo 3
    PreModulo3 = int(input("\nA continuacion sigue el Modulo 3.Presupuesto de Produccion. ¿Desea continuar? \n\t[1]Si \n\t[2]No\n» "))
    if PreModulo3 == 1:
        print('\n--------- ENTRANDO AL MODULO 3 ---------')
        print('\n--------- Presupuesto de Produccion ---------')
        print("\nPrimero se ingresará el 1er Semestre\n")

        # Productos, ya se registro anteriormente
        # Unidades a vender, se registro en el Modulo 1
        #  S1P1         S1 : Semestre 1, P1 : Producto 1
        InventarioFinalS1P1 = float(input(f"Ingrese el inventario final del producto {PrimerProducto}\n» "))
        TotaldeUnidadesS1P1 = (Unidadesavender_S1P1+InventarioFinalS1P1) ## <<< aqui le movimos
        InventarioInicialS1P1 = float(input(f"Ingrese el inventario inicial del producto {PrimerProducto}\n» "))
        UnidadesaProducirS1P1 = (TotaldeUnidadesS1P1-InventarioInicialS1P1)
        #  S1P2         S1 : Semestre 1, P2 : Producto 2
        InventarioFinalS1P2 = float(input(f"Ingrese el inventario final del producto {SegundoProducto}\n» "))
        TotaldeUnidadesS1P2 = (Unidadesavender_S1P2+InventarioFinalS1P2)
        InventarioInicialS1P2 = float(input(f"Ingrese el inventario inicial del producto {SegundoProducto}\n» "))
        UnidadesaProducirS1P2 = (TotaldeUnidadesS1P2-InventarioInicialS1P2)
        #  S1P3         S1 : Semestre 1, P3 : Producto 3
        InventarioFinalS1P3 = float(input(f"Ingrese el inventario final del producto {TercerProducto}\n» "))
        TotaldeUnidadesS1P3 = (Unidadesavender_S1P3+InventarioFinalS1P3) #InventarioFinalS1P3
        InventarioInicialS1P3 = float(input(f"Ingrese el inventario inicial del producto {TercerProducto}\n» "))
        UnidadesaProducirS1P3 = (TotaldeUnidadesS1P3-InventarioInicialS1P3)
        print("\nAhora se ingresará del 2do Semestre\n")
        #  S2P1         S2 : Semestre 2, P1 : Producto 1
        InventarioFinalS2P1 = float(input(f"Ingrese el inventario final del producto {PrimerProducto}\n» "))
        TotaldeUnidadesS2P1 = (Unidadesavender_S2P1+InventarioFinalS2P1)
        InventarioInicialS2P1 = float(input(f"Ingrese el inventario inicial del producto {PrimerProducto}\n» "))
        UnidadesaProducirS2P1 = (TotaldeUnidadesS2P1-InventarioInicialS2P1)
        #  S2P2         S2 : Semestre 2, P2 : Producto 2
        InventarioFinalS2P2 = float(input(f"Ingrese el inventario final del producto {SegundoProducto}\n» "))
        TotaldeUnidadesS2P2 = (Unidadesavender_S2P2+InventarioFinalS2P2)
        InventarioInicialS2P2 = float(input(f"Ingrese el inventario inicial del producto {SegundoProducto}\n» "))
        UnidadesaProducirS2P2 = (TotaldeUnidadesS2P2-InventarioInicialS2P2)
        #  S2P3         S2 : Semestre 2, P3 : Producto 3
        InventarioFinalS2P3 = float(input(f"Ingrese el inventario final del producto {TercerProducto}\n» "))
        TotaldeUnidadesS2P3 = (Unidadesavender_S2P3+InventarioFinalS2P3)
        InventarioInicialS2P3 = float(input(f"Ingrese el inventario inicial del producto {TercerProducto}\n» "))
        UnidadesaProducirS2P3 = (TotaldeUnidadesS2P3-InventarioInicialS2P3)
        # Ahora se calculara el total del año

        TotalAñoUnidadesAVenderP1 = Unidadesavender_S1P1+Unidadesavender_S2P1
        TotalAñoUnidadesAVenderP2 = Unidadesavender_S1P2+Unidadesavender_S2P2
        TotalAñoUnidadesAVenderP3 = Unidadesavender_S1P3+Unidadesavender_S2P3

        TotalAñoActTotaldeUnidadesP1 = (TotalAñoUnidadesAVenderP1+InventarioFinalS2P1) # posible mal jeje
        TotaldeUnidadesaProducirP1 = (UnidadesaProducirS1P1+UnidadesaProducirS2P1)
        TotalAñoActTotaldeUnidadesP2 = (TotalAñoUnidadesAVenderP2+InventarioFinalS2P2) # mal
        TotaldeUnidadesaProducirP2 = (UnidadesaProducirS1P2+UnidadesaProducirS2P2)
        TotalAñoActTotaldeUnidadesP3 = (TotalAñoUnidadesAVenderP3+InventarioFinalS2P3) # mal
        TotaldeUnidadesaProducirP3 = (UnidadesaProducirS1P3+UnidadesaProducirS2P3)

        # Mostrar tabla
        fig, ax = plt.subplots(figsize=(13, 8), dpi=100)
        data = [["PRODUCTO " + PrimerProducto, "","",""],
            ["Unidades a vender ",Unidadesavender_S1P1, Unidadesavender_S2P1, TotalAñoUnidadesAVenderP1],
            ["(+) Inventario Final",InventarioFinalS1P1,InventarioFinalS2P1, InventarioFinalS2P1],
            ["(=) Total de Unidades ",TotaldeUnidadesS1P1,TotaldeUnidadesS2P1, TotalAñoActTotaldeUnidadesP1],
            ["(-) Inventario Inicial",InventarioInicialS1P1,InventarioInicialS2P1, InventarioInicialS1P1],
            ["(=) Unidades a Producir",UnidadesaProducirS1P1,UnidadesaProducirS2P1,TotaldeUnidadesaProducirP1],
            ["","","",""],
            ["PRODUCTO " + SegundoProducto, "","",""],
            ["Unidades a vender ",Unidadesavender_S1P2, Unidadesavender_S2P2, TotalAñoUnidadesAVenderP2],
            ["(+) Inventario Final",InventarioFinalS1P2,InventarioFinalS2P2, InventarioFinalS2P2],
            ["(=) Total de Unidades ",TotaldeUnidadesS1P2,TotaldeUnidadesS2P2, TotalAñoActTotaldeUnidadesP2],
            ["(-) Inventario Inicial",InventarioInicialS1P2,InventarioInicialS2P2, InventarioInicialS1P2],
            ["(=) Unidades a Producir",UnidadesaProducirS1P2,UnidadesaProducirS2P2,TotaldeUnidadesaProducirP2],
            ["","","",""],
            ["PRODUCTO " + TercerProducto, "","",""],
            ["Unidades a vender ",Unidadesavender_S1P3, Unidadesavender_S2P3, TotalAñoUnidadesAVenderP3],
            ["(+) Inventario Final",InventarioFinalS1P3,InventarioFinalS2P3, InventarioFinalS2P3],
            ["(=) Total de Unidades ",TotaldeUnidadesS1P3,TotaldeUnidadesS2P3, TotalAñoActTotaldeUnidadesP3],
            ["(-) Inventario Inicial",InventarioInicialS1P3,InventarioInicialS2P3, InventarioInicialS1P3],
            ["(=) Unidades a Producir",UnidadesaProducirS1P3,UnidadesaProducirS2P3,TotaldeUnidadesaProducirP3],
            ["","","",""]]
        column_labels = ["", "1er. Semestre", "2do. Semestre","Total "+str(AñoAct)]
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText = data, colLabels = column_labels, loc="center")
        table.set_fontsize(24)
        table.scale(1.2, 1.8)
        #plt.title("3. Presupuesto de Producción")
        plt.show()

    elif PreModulo3 == 2:
        break

    # Módulo 4
    PreModulo4 = int(input("\nA continuacion sigue el Modulo 3.Presupuesto de Requerimento de Materiales. ¿Desea continuar? \n\t[1]Si \n\t[2]No\n» "))
    if PreModulo4 == 1:
        print('\n--------- ENTRANDO AL MODULO 4 ---------')
        print('\n--------- Presupuesto de Requerimento de Materiales ---------')
        print("\nPrimero se ingresará el 1er Semestre\n")

        # Productos, ya se registro anteriormente
        # Unidades a vender, se registro en el Modulo 1
        #  S1P1MA         S1 : Semestre 1, P1 : Producto 1, MA : Material A
        print("------Material A------")
        RequerimentoMaterialS1P1MA = float(input(f"Ingrese el Requerimento de material A del producto {PrimerProducto}\n» "))
        TotalMaterialS1P1MA = (UnidadesaProducirS1P1*RequerimentoMaterialS1P1MA)
        #  S1P1MB         S1 : Semestre 1, P1 : Producto 1, MA : Material B
        print("------Material B------")
        RequerimentoMaterialS1P1MB = float(input(f"Ingrese el Requerimento de material B del producto {PrimerProducto}\n» "))
        TotalMaterialS1P1MB = (UnidadesaProducirS1P1*RequerimentoMaterialS1P1MB)
        #  S1P1MC         S1 : Semestre 1, P1 : Producto 1, MA : Material C
        print("------Material C------")
        RequerimentoMaterialS1P1MC = float(input(f"Ingrese el Requerimento de material C del producto {PrimerProducto}\n» "))
        TotalMaterialS1P1MC = (UnidadesaProducirS1P1*RequerimentoMaterialS1P1MC)
        #  S1P2MA         S1 : Semestre 1, P2 : Producto 2, MA : Material A
        print("------Material A------")
        RequerimentoMaterialS1P2MA = float(input(f"Ingrese el Requerimento de material A del producto {SegundoProducto}\n» "))
        TotalMaterialS1P2MA = (UnidadesaProducirS1P2*RequerimentoMaterialS1P2MA)
        #  S1P2MB         S1 : Semestre 1, P2 : Producto 2, MA : Material B
        print("------Material B------")
        RequerimentoMaterialS1P2MB = float(input(f"Ingrese el Requerimento de material B del producto {SegundoProducto}\n» "))
        TotalMaterialS1P2MB = (UnidadesaProducirS1P2*RequerimentoMaterialS1P2MB)
        #  S1P2MC         S1 : Semestre 1, P2 : Producto 2, MA : Material C
        print("------Material C------")
        RequerimentoMaterialS1P2MC = float(input(f"Ingrese el Requerimento de material C del producto {SegundoProducto}\n» "))
        TotalMaterialS1P2MC = (UnidadesaProducirS1P2*RequerimentoMaterialS1P2MC)
        #  S1P3MA         S1 : Semestre 1, P2 : Producto 3, MA : Material A
        print("------Material A------")
        RequerimentoMaterialS1P3MA = float(input(f"Ingrese el Requerimento de material A del producto {TercerProducto}\n» "))
        TotalMaterialS1P3MA = (UnidadesaProducirS1P3*RequerimentoMaterialS1P3MA)
        #  S1P3MB         S1 : Semestre 1, P2 : Producto 3, MA : Material B
        print("------Material B------")
        RequerimentoMaterialS1P3MB = float(input(f"Ingrese el Requerimento de material B del producto {TercerProducto}\n» "))
        TotalMaterialS1P3MB = (UnidadesaProducirS1P3*RequerimentoMaterialS1P3MB)
        #  S1P3MC         S1 : Semestre 1, P2 : Producto 3, MA : Material C
        print("------Material C------")
        RequerimentoMaterialS1P3MC = float(input(f"Ingrese el Requerimento de material C del producto {TercerProducto}\n» "))
        TotalMaterialS1P3MC = (UnidadesaProducirS1P3*RequerimentoMaterialS1P3MC)
        # Aqui se calculara el Total de Requerimentos de los materiales A.B y C del Semestre 1
        #S1MA : S1: Semestre 1, MA: Material A
        TotalRequerimentosS1MA = (TotalMaterialS1P1MA+TotalMaterialS1P2MA+TotalMaterialS1P3MA)
        #S1MB : S1: Semestre 1, MB: Material B
        TotalRequerimentosS1MB = (TotalMaterialS1P1MB+TotalMaterialS1P2MB+TotalMaterialS1P3MB)
        #S1MC : S1: Semestre 1, MC: Material C
        TotalRequerimentosS1MC = (TotalMaterialS1P1MC+TotalMaterialS1P2MC+TotalMaterialS1P3MC)
        print("\nAhora se ingresará del 2do Semestre\n")
        #  S2P1MA         S2: Semestre 2, P1 : Producto 1, MA : Material A
        print("------Material A------")
        RequerimentoMaterialS2P1MA = float(input(f"Ingrese el Requerimento de material A del producto {PrimerProducto}\n» "))
        TotalMaterialS2P1MA = (UnidadesaProducirS2P1*RequerimentoMaterialS2P1MA)
        #  S2P1MB         S1 : Semestre 2, P1 : Producto 1, MA : Material B
        print("------Material B------")
        RequerimentoMaterialS2P1MB = float(input(f"Ingrese el Requerimento de material B del producto {PrimerProducto}\n» "))
        TotalMaterialS2P1MB = (UnidadesaProducirS2P1*RequerimentoMaterialS2P1MB)
        #  S2P1MC         S1 : Semestre 2, P1 : Producto 1, MA : Material C
        print("------Material C------")
        RequerimentoMaterialS2P1MC = float(input(f"Ingrese el Requerimento de material C del producto {PrimerProducto}\n» "))
        TotalMaterialS2P1MC = (UnidadesaProducirS2P1*RequerimentoMaterialS2P1MC)
        #  S2P2MA         S1 : Semestre 2, P2 : Producto 2, MA : Material A
        print("------Material A------")
        RequerimentoMaterialS2P2MA = float(input(f"Ingrese el Requerimento de material A del producto {SegundoProducto}\n» "))
        TotalMaterialS2P2MA = (UnidadesaProducirS2P2*RequerimentoMaterialS2P2MA)
        #  S2P2MB         S1 : Semestre 2, P2 : Producto 2, MA : Material B
        print("------Material B------")
        RequerimentoMaterialS2P2MB = float(input(f"Ingrese el Requerimento de material B del producto {SegundoProducto}\n» "))
        TotalMaterialS2P2MB = (UnidadesaProducirS2P2*RequerimentoMaterialS2P2MB)
        #  S2P2MC         S1 : Semestre 2, P2 : Producto 2, MA : Material C
        print("------Material C------")
        RequerimentoMaterialS2P2MC = float(input(f"Ingrese el Requerimento de material C del producto {SegundoProducto}\n» "))
        TotalMaterialS2P2MC = (UnidadesaProducirS2P2*RequerimentoMaterialS2P2MC)
        #  S2P3MA         S1 : Semestre 2, P2 : Producto 3, MA : Material A
        print("------Material A------")
        RequerimentoMaterialS2P3MA = float(input(f"Ingrese el Requerimento de material A del producto {TercerProducto}\n» "))
        TotalMaterialS2P3MA = (UnidadesaProducirS2P3*RequerimentoMaterialS2P3MA)
        #  S2P3MB         S1 : Semestre 2, P2 : Producto 3, MA : Material B
        print("------Material B------")
        RequerimentoMaterialS2P3MB = float(input(f"Ingrese el Requerimento de material B del producto {TercerProducto}\n» "))
        TotalMaterialS2P3MB = (UnidadesaProducirS2P3*RequerimentoMaterialS2P3MB)
        #  S2P3MC         S1 : Semestre 2, P2 : Producto 3, MA : Material C
        print("------Material C------")
        RequerimentoMaterialS2P3MC = float(input(f"Ingrese el Requerimento de material C del producto {TercerProducto}\n» "))
        TotalMaterialS2P3MC = (UnidadesaProducirS2P3*RequerimentoMaterialS2P3MC)
        # Aqui se calculara el Total de Requerimentos de los materiales A.B y C del Semestre 2
        #S2MA : S2: Semestre 2, MA: Material A
        TotalRequerimentosS2MA = (TotalMaterialS2P1MA+TotalMaterialS2P2MA+TotalMaterialS2P3MA)
        #S2MB : S2: Semestre 2, MB: Material B
        TotalRequerimentosS2MB = (TotalMaterialS2P1MB+TotalMaterialS2P2MB+TotalMaterialS2P3MB)
        #S2MC : S2: Semestre 2, MC: Material C
        TotalRequerimentosS2MC = (TotalMaterialS2P1MC+TotalMaterialS2P2MC+TotalMaterialS2P3MC)
        # Ahora se calculara el total de material del año
        # P1MA : P1: Producto 1, MA: Material A
        TotalMaterialRequeridoP1MA = (TotalMaterialS1P1MA+TotalMaterialS2P1MA)
        # P1MB : P1: Producto 1, MB: Material B
        TotalMaterialRequeridoP1MB = (TotalMaterialS1P1MB+TotalMaterialS2P1MB)
        # P1MC : P1: Producto 1, MC: Material C
        TotalMaterialRequeridoP1MC = (TotalMaterialS1P1MC+TotalMaterialS2P1MC)
        # P2MA : P2: Producto 2, MA: Material A
        TotalMaterialRequeridoP2MA = (TotalMaterialS1P2MA+TotalMaterialS2P2MA)
        # P2MB : P2: Producto 2, MB: Material B
        TotalMaterialRequeridoP2MB = (TotalMaterialS1P2MB+TotalMaterialS2P2MB)
        # P2MC : P2: Producto 2, MC: Material C
        TotalMaterialRequeridoP2MC = (TotalMaterialS1P2MC+TotalMaterialS2P2MC)
        # P3MA : P3: Producto 3, MA: Material A
        TotalMaterialRequeridoP3MA = (TotalMaterialS1P3MA+TotalMaterialS2P3MA)
        # P3MB : P3: Producto 3, MB: Material B
        TotalMaterialRequeridoP3MB = (TotalMaterialS1P3MB+TotalMaterialS2P3MB)
        # P3MC : P3: Producto 3, MC: Material C
        TotalMaterialRequeridoP3MC = (TotalMaterialS1P3MC+TotalMaterialS2P3MC)
        # Aqui se calculara el Total de Requerimentos de los materiales A.B y C del año
        # MA: Material A
        TotalRequerimentosMA = (TotalRequerimentosS1MA+TotalRequerimentosS2MA)
        # MB: Material B
        TotalRequerimentosMB = (TotalRequerimentosS1MB+TotalRequerimentosS2MB)
        # MC: Material C
        TotalRequerimentosMC = (TotalRequerimentosS1MC+TotalRequerimentosS2MC)

        # Mostrar tabla
        fig, ax = plt.subplots(figsize=(6, 9), dpi=150)
        data = [["PRODUCTO " + PrimerProducto, "","",""],
                ["Unidades a producir",UnidadesaProducirS1P1,UnidadesaProducirS2P1,TotaldeUnidadesaProducirP1],
                ["","","",""],
                ["Material A","","",""],
                ["Requerimiento de material",str(RequerimentoMaterialS1P1MA),str(RequerimentoMaterialS2P1MA),str(RequerimentoMaterialS1P1MA)],
                ["Total de Material A requerido",TotalMaterialS1P1MA,TotalMaterialS2P1MA,TotalMaterialRequeridoP1MA],
                ["Material B","","",""],
                ["Requerimiento de material",RequerimentoMaterialS1P1MB,RequerimentoMaterialS2P1MB,RequerimentoMaterialS1P1MB],
                ["Total de Material B requerido",TotalMaterialS1P1MB,TotalMaterialS2P1MB,TotalMaterialRequeridoP1MB],
                ["Material C","","",""],
                ["Requerimiento de material",RequerimentoMaterialS1P1MC,RequerimentoMaterialS2P1MC,RequerimentoMaterialS1P1MC],
                ["Total de Material C requerido",TotalMaterialS1P1MC,TotalMaterialS2P1MC,TotalMaterialRequeridoP1MC],
                ["","","",""],
                ["PRODUCTO "+ SegundoProducto,"","",""],
                ["Unidades a producir",UnidadesaProducirS1P2,UnidadesaProducirS2P2,TotaldeUnidadesaProducirP2],
                ["","","",""],
                ["Material A","","",""],
                ["Requerimiento de material",RequerimentoMaterialS1P2MA,RequerimentoMaterialS1P2MA,RequerimentoMaterialS1P2MA],
                ["Total de Material A requerido",TotalMaterialS1P2MA,TotalMaterialS2P2MA,TotalMaterialRequeridoP2MA],
                ["Material B","","",""],
                ["Requerimiento de material",RequerimentoMaterialS1P2MB,RequerimentoMaterialS2P2MB,RequerimentoMaterialS1P2MB],
                ["Total de Material B requerido",TotalMaterialS1P2MB,TotalMaterialS2P2MB,TotalMaterialRequeridoP2MB],
                ["Material C","","",""],
                ["Requerimiento de material",RequerimentoMaterialS1P2MC,RequerimentoMaterialS2P1MC,RequerimentoMaterialS1P2MC],
                ["Total de Material C requerido",TotalMaterialS1P2MC,TotalMaterialS2P2MC,TotalMaterialRequeridoP2MC],
                ["","","",""],
                ["PRODUCTO "+ TercerProducto,"","",""],
                ["Unidades a producir",UnidadesaProducirS1P3,UnidadesaProducirS2P3,TotaldeUnidadesaProducirP3],
                ["","","",""],
                ["Material A","","",""],
                ["Requerimiento de material",RequerimentoMaterialS1P3MA,RequerimentoMaterialS1P3MA,RequerimentoMaterialS1P3MA],
                ["Total de Material A requerido",TotalMaterialS1P3MA,TotalMaterialS2P2MA,TotalMaterialRequeridoP2MA],
                ["Material B","","",""],
                ["Requerimiento de material",RequerimentoMaterialS1P3MB,RequerimentoMaterialS1P3MB,RequerimentoMaterialS1P3MB],
                ["Total de Material B requerido",TotalMaterialS1P3MB,TotalMaterialS2P2MB,TotalMaterialRequeridoP2MB],
                ["Material C","","",""],
                ["Requerimiento de material",RequerimentoMaterialS1P3MC,RequerimentoMaterialS1P3MC,RequerimentoMaterialS1P3MC],
                ["Total de Material C requerido",TotalMaterialS1P3MC,TotalMaterialS2P3MC,TotalMaterialRequeridoP3MC],
                ["","","",""],
                ["","","",""],
                ["Total de Requerimientos ","","",""],
                ["Material A",TotalRequerimentosS1MA,TotalRequerimentosS2MA,TotalRequerimentosMA],
                ["Material B",TotalRequerimentosS1MB,TotalRequerimentosS2MB,TotalRequerimentosMB],
                ["Material C",TotalRequerimentosS1MC,TotalRequerimentosS2MC,TotalRequerimentosMC]]
        column_labels = ["", "1er. Semestre", "2do. Semestre","Total "+str(AñoAct)]
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText = data, colLabels = column_labels, loc="center")
        table.set_fontsize(12)
        table.scale(1.2, 1.2)
        #plt.title("4. Presupuesto de Requerimiento de Materiales")
        plt.show()

    elif PreModulo4 == 2:
        break

    # Módulo 5
    PreModulo5 = int(input("\nA continuacion sigue el Modulo 5.Presupuesto de Compra de Materiales. ¿Desea continuar? \n\t[1]Si \n\t[2]No\n» "))
    if PreModulo5 == 1:
        print('\n--------- ENTRANDO AL MODULO 5 ---------')
        print('\n--------- Presupuesto de Compra de Materiales ---------')
        print("\nPrimero se ingresará el 1er Semestre\n")

        # MA: Material A
        InventarioFinalS1MA = float(input("Ingrese el inventario final del Material A\n» "))
        TotalMaterialesS1MA = (TotalRequerimentosS1MA+InventarioFinalS1MA)
        # Inventario Inicial aqui en este modulo viene siendo lo mismo que Inventario Final, usar esa variable para mostrar el Inventario Inicial
        MaterialaComprarS1MA = (TotalMaterialesS1MA-InventarioFinalS1MA)
        PreciodeCompraS1MA = float(input("Ingrese el precio de compra del Material A\n» "))
        TotalMaterialS1MA = (MaterialaComprarS1MA*PreciodeCompraS1MA)
        # MB: Material B
        InventarioFinalS1MB = float(input("Ingrese el inventario final del Material B\n» "))
        TotalMaterialesS1MB = (TotalRequerimentosS1MB+InventarioFinalS1MB)
        # Inventario Inicial aqui en este modulo viene siendo lo mismo que Inventario Final, usar esa variable para mostrar el Inventario Inicial
        MaterialaComprarS1MB = (TotalMaterialesS1MB-InventarioFinalS1MB)
        PreciodeCompraS1MB = float(input("Ingrese el precio de compra del Material B\n» "))
        TotalMaterialS1MB = (MaterialaComprarS1MB*PreciodeCompraS1MB)
        # MC: Material C
        InventarioFinalS1MC = float(input("Ingrese el inventario final del Material C\n» "))
        TotalMaterialesS1MC = (TotalRequerimentosS1MC+InventarioFinalS1MC)
        # Inventario Inicial aqui en este modulo viene siendo lo mismo que Inventario Final, usar esa variable para mostrar el Inventario Inicial
        MaterialaComprarS1MC = (TotalMaterialesS1MC-InventarioFinalS1MC)
        PreciodeCompraS1MC = float(input("Ingrese el precio de compra del Material C\n» "))
        TotalMaterialS1MC = (MaterialaComprarS1MC*PreciodeCompraS1MC)
        # Aqui se calculara el total de compras del semestre 1
        # MS1: Material Semestre 1
        ComprasTotalesMS1 = (TotalMaterialS1MA+TotalMaterialS1MB+TotalMaterialS1MC)
        print("\nAhora se ingresará del 2do Semestre\n")
        # MA: Material A
        InventarioFinalS2MA = float(input("Ingrese el inventario final del Material A\n» "))
        TotalMaterialesS2MA = (TotalRequerimentosS2MA+InventarioFinalS2MA)
        # Inventario Inicial aqui en este modulo viene siendo lo mismo que Inventario Final, usar esa variable para mostrar el Inventario Inicial
        MaterialaComprarS2MA = (TotalMaterialesS2MA-InventarioFinalS1MA)
        PreciodeCompraS2MA = float(input("Ingrese el precio de compra del Material A\n» "))
        TotalMaterialS2MA = (MaterialaComprarS2MA*PreciodeCompraS2MA)
        # MB: Material B
        InventarioFinalS2MB = float(input("Ingrese el inventario final del Material B\n» "))
        TotalMaterialesS2MB = (TotalRequerimentosS2MB+InventarioFinalS2MB)
        # Inventario Inicial aqui en este modulo viene siendo lo mismo que Inventario Final, usar esa variable para mostrar el Inventario Inicial
        MaterialaComprarS2MB = (TotalMaterialesS2MB-InventarioFinalS1MB)
        PreciodeCompraS2MB = float(input("Ingrese el precio de compra del Material B\n» "))
        TotalMaterialS2MB = (MaterialaComprarS2MB*PreciodeCompraS2MB)
        # MC: Material C
        InventarioFinalS2MC = float(input("Ingrese el inventario final del Material C\n» "))
        TotalMaterialesS2MC = (TotalRequerimentosS2MC+InventarioFinalS2MC)
        # Inventario Inicial aqui en este modulo viene siendo lo mismo que Inventario Final, usar esa variable para mostrar el Inventario Inicial
        MaterialaComprarS2MC = (TotalMaterialesS2MC-InventarioFinalS1MC)
        PreciodeCompraS2MC = float(input("Ingrese el precio de compra del Material C\n» "))
        TotalMaterialS2MC = (MaterialaComprarS2MC*PreciodeCompraS2MC)
        # Aqui se calculara el total de compras del semestre 2
        # MS2: Material Semestre 2
        ComprasTotalesMS2 = (TotalMaterialS2MA+TotalMaterialS2MB+TotalMaterialS2MC)
        # Aqui se calculara el total de los dos semestres
        # MA: Material A
        TotaldeMaterialesMA = (TotalRequerimentosMA+InventarioFinalS2MA)
        MaterialaComprarMA = (TotaldeMaterialesMA-InventarioFinalS1MA)
        TotaldeMaterialA = (TotalMaterialS1MA+TotalMaterialS2MA)
        # MB: Material B
        TotaldeMaterialesMB = (TotalRequerimentosMB+InventarioFinalS2MB)
        MaterialaComprarMB = (TotaldeMaterialesMB-InventarioFinalS1MB)
        TotaldeMaterialB = (TotalMaterialS1MB+TotalMaterialS2MB)
        # MC: Material C
        TotaldeMaterialesMC = (TotalRequerimentosMC+InventarioFinalS2MC)
        MaterialaComprarMC = (TotaldeMaterialesMC-InventarioFinalS1MC)
        TotaldeMaterialC = (TotalMaterialS1MC+TotalMaterialS2MC)
        # Aqui se calculara el total de compras de los dos semestres
        # M: Material
        ComprasTotalesM = (ComprasTotalesMS1+ComprasTotalesMS2)

    # Mostrar tabla
    fig, ax = plt.subplots(figsize=(9, 6), dpi=150)
    data = [["MATERIAL A", "","",""],
            ["Requerimiento de materiales",TotalRequerimentosS1MA,TotalRequerimentosS2MA,TotalRequerimentosMA],
            ["( + ) Inventario Final", InventarioFinalS1MA,InventarioFinalS2MA,InventarioFinalS2MA],
            ["Total de Materiales", TotalMaterialesS1MA,TotalMaterialesS2MA,TotaldeMaterialesMA],
            ["( - ) Inventario Inicial",InventarioFinalS1MA,InventarioFinalS1MA,InventarioFinalS1MA],
            ["Material a comprar",MaterialaComprarS1MA,MaterialaComprarS2MA,MaterialaComprarMA],
            ["Precio de Compra", PreciodeCompraS1MA,PreciodeCompraS2MA,""],
            ["Total de Material A en $:",TotalMaterialS1MA,TotalMaterialS2MA,TotaldeMaterialA],
            ["", "","",""],
            ["Material B", "","",""],
            ["Requerimiento de materiales",TotalRequerimentosS1MB,TotalRequerimentosS2MB,TotalRequerimentosMB],
            ["Inventario Final", InventarioFinalS1MB,InventarioFinalS2MB,InventarioFinalS2MB],
            ["Total de Materiales", TotalMaterialesS1MB,TotalMaterialesS2MB,TotaldeMaterialesMB],
            ["Inventario Inicial",InventarioFinalS1MB,InventarioFinalS1MB,InventarioFinalS1MB],
            ["Material a comprar",MaterialaComprarS1MB,MaterialaComprarS2MB,MaterialaComprarMB],
            ["Precio de Compra", PreciodeCompraS1MB,PreciodeCompraS2MB,""],
            ["Total de Material B en $:",TotalMaterialS1MB,TotalMaterialS2MB,TotaldeMaterialB],
            ["", "","",""],
            ["Material C", "","",""],
            ["Requerimiento de materiales",TotalRequerimentosS1MC,TotalRequerimentosS2MC,TotalRequerimentosMC],
            ["Inventario Final", InventarioFinalS1MC,InventarioFinalS2MC,InventarioFinalS2MC],
            ["Total de Materiales", TotalMaterialesS1MC,TotalMaterialesS2MC,TotaldeMaterialesMC],
            ["Inventario Inicial",InventarioFinalS1MC,InventarioFinalS1MC,InventarioFinalS1MC],
            ["Material a comprar",MaterialaComprarS1MC,MaterialaComprarS2MC,MaterialaComprarMC],
            ["Precio de Compra", PreciodeCompraS1MC,PreciodeCompraS2MC,""],
            ["Total de Material C en $:",TotalMaterialS1MC,TotalMaterialS2MC,TotaldeMaterialC],
            ["", "","",""],
            ["Compras totales:", ComprasTotalesMS1,ComprasTotalesMS2,ComprasTotalesM],
        ["","","",""]]
    column_labels = ["", "1er. Semestre", "2do. Semestre", "Total "+str(AñoAct)]
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText = data, colLabels = column_labels, loc="center")
    table.set_fontsize(14)
    table.scale(0.9, 1.1)
    #plt.title("5. Presupuesto de compra de Materiales")
    plt.show()

    if PreModulo5 == 2:
        break

    # Modulo 6
    PreModulo6 = int(input("\nA continuacion sigue el Modulo 6.Determinacion del saldo de Proveedores y Flujo de Salidas. ¿Desea continuar? \n\t[1]Si \n\t[2]No\n» "))

    if PreModulo6 == 1:
        print('\n\t\t--------- ENTRANDO AL MODULO 6 ---------')
        print('\n--------- Determinacion del saldo de Proveedores y Flujo de Salidas ---------')

        SaldodeProveedoresAñoViejo = float(input(f"Ingrese el saldo de proveedores del año {AñoAnt}\n» "))
        TotalProveedoresAñoAct = (SaldodeProveedoresAñoViejo+ComprasTotalesM)
        ProvedooresAñoAntPorcentaje = int(input(f"Ingrese el porcentaje(%) que se pagara del saldo proveedores del {AñoAnt} (Ej:100)\n» "))
        ProveedoresAñoAntConversion = (ProvedooresAñoAntPorcentaje/100)
        ProveedoresAñoAnt = (SaldodeProveedoresAñoViejo*ProveedoresAñoAntConversion)
        ProvedooresAñoActPorcentaje = int(input(f"Ingrese el porcentaje(%) que se pagara de las compras presupuestadas del {AñoAct} (Ej:50)\n» "))
        ProveedoresAñoActConversion = (ProvedooresAñoActPorcentaje/100)
        ProveedoresAñoAct = (ComprasTotalesM*ProveedoresAñoActConversion)
        TotaldeSalidas = (ProveedoresAñoAnt+ProveedoresAñoAct)
        SaldodeProveedoresAñoAct = (TotalProveedoresAñoAct-TotaldeSalidas)

        # Mostrar tabla
        fig, ax = plt.subplots(figsize=(9, 5), dpi=150)
        data = [["Saldo de Proveedores "+AñoAct,"","$"+str(SaldodeProveedoresAñoViejo)],
                ["Compras "+AñoAct,"","$"+str(ComprasTotalesM)],
                ["Total de Proveedores "+AñoAct,"","$"+str(TotalProveedoresAñoAct)],
                ["","",""],
                ["Salidas de Efectivo:","",""],
                ["Por Proveedores del "+AñoAnt,"$"+str(ProveedoresAñoAnt),""],
                ["Por Proveedores del "+AñoAct,"$"+str(ProveedoresAñoAct),""],
                ["Total de Salidas "+AñoAct,"","$"+str(TotaldeSalidas)],
                ["","",""],
                ["Saldo de Proveedores del "+AñoAct,"","$"+str(SaldodeProveedoresAñoAct)]]
        column_labels = ["Descripción", "Importe", "Total"]
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText = data, colLabels = column_labels, loc="center")
        table.set_fontsize(16)
        table.scale(1.2, 1.6)
        plt.title("6. Determinación del saldo de Proveedores y Flujo de Salidas")
        plt.show()

    if PreModulo6 == 2:
        break

    # Modulo 7
    PreModulo7 = int(input("\nA continuacion sigue el Modulo 7.Presupuesto de Mano de Obra Directa. ¿Desea continuar? \n\t[1]Si \n\t[2]No\n» "))

    if PreModulo7 == 1:
        print('\n--------- ENTRANDO AL MODULO 7 ---------')
        print('\n--------- Presupuesto de Mano de Obra Directa ---------')
        print("\nPrimero se ingresará el 1er Semestre\n")

        HorasRequeridasxUnidadS1P1 = float(input(f"Ingrese las horas requeridas por unidad del producto {PrimerProducto}\n» "))
        TotaldeHorasRequeridasS1P1 = (UnidadesaProducirS1P1*HorasRequeridasxUnidadS1P1)
        CuotaxHoraS1P1 = float(input(f"Ingrese la cuota por hora del producto {PrimerProducto}\n» "))
        ImportedeMODS1P1 = (TotaldeHorasRequeridasS1P1*CuotaxHoraS1P1)

        HorasRequeridasxUnidadS1P2 = float(input(f"Ingrese las horas requeridas por unidad del producto {SegundoProducto}\n» "))
        TotaldeHorasRequeridasS1P2 = (UnidadesaProducirS1P2*HorasRequeridasxUnidadS1P2)
        CuotaxHoraS1P2 = float(input(f"Ingrese la cuota por hora del producto {SegundoProducto}\n» "))
        ImportedeMODS1P2 = (TotaldeHorasRequeridasS1P2*CuotaxHoraS1P2)

        HorasRequeridasxUnidadS1P3 = float(input(f"Ingrese las horas requeridas por unidad del producto {TercerProducto}\n» "))
        TotaldeHorasRequeridasS1P3 = (UnidadesaProducirS1P3*HorasRequeridasxUnidadS1P3)
        CuotaxHoraS1P3 = float(input(f"Ingrese la cuota por hora del producto {TercerProducto}\n» "))
        ImportedeMODS1P3 = (TotaldeHorasRequeridasS1P3*CuotaxHoraS1P3)

        TotaldeHorasRequeridasxS1 = (TotaldeHorasRequeridasS1P1+TotaldeHorasRequeridasS1P2+TotaldeHorasRequeridasS1P3)
        TotaldeMODxS1 = (ImportedeMODS1P1+ImportedeMODS1P2+ImportedeMODS1P3)

        print("\nAhora se ingresará del 2do Semestre\n")
        val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12, val13, val14, val15, val16, val17, val18, val19, val20, val21, val22, val23, val24, val25, val26, val27, val28, val29, val30, val31, val32, val33, val34, val35, val36, val37, val38, val39, val40, val41, val42  = 2400,1300,3700,15,18,360000,234000,594000,13500,10800,24300,1,1,1,13500,10800,24300,15,18,202500,194400,396900,7000,7500,14500,1.5,1.5,1.5,10500,11250,21750,15,18,157500,202500,360000,48000,35050,83050,720000,630900,1350900

        HorasRequeridasxUnidadS2P1 = float(input(f"Ingrese las horas requeridas por unidad del producto {PrimerProducto}\n» "))
        TotaldeHorasRequeridasS2P1 = (UnidadesaProducirS2P1*HorasRequeridasxUnidadS2P1)
        CuotaxHoraS2P1 = float(input(f"Ingrese la cuota por hora del producto {PrimerProducto}\n» "))
        ImportedeMODS2P1 = (TotaldeHorasRequeridasS2P1*CuotaxHoraS2P1)

        HorasRequeridasxUnidadS2P2 = float(input(f"Ingrese las horas requeridas por unidad del producto {SegundoProducto}\n» "))
        TotaldeHorasRequeridasS2P2 = (UnidadesaProducirS2P2*HorasRequeridasxUnidadS2P2)
        CuotaxHoraS2P2 = float(input(f"Ingrese la cuota por hora del producto {SegundoProducto}\n» "))
        ImportedeMODS2P2 = (TotaldeHorasRequeridasS2P2*CuotaxHoraS2P2)

        HorasRequeridasxUnidadS2P3 = float(input(f"Ingrese las horas requeridas por unidad del producto {TercerProducto}\n» "))
        TotaldeHorasRequeridasS2P3 = (UnidadesaProducirS2P3*HorasRequeridasxUnidadS2P3)
        CuotaxHoraS2P3 = float(input(f"Ingrese la cuota por hora del producto {TercerProducto}\n» "))
        ImportedeMODS2P3 = (TotaldeHorasRequeridasS2P3*CuotaxHoraS2P3)

        TotaldeHorasRequeridasxS2 = (TotaldeHorasRequeridasS2P1+TotaldeHorasRequeridasS2P2+TotaldeHorasRequeridasS2P3)
        TotaldeMODxS2 = (ImportedeMODS2P1+ImportedeMODS2P2+ImportedeMODS2P3)

        # Aqui se calculara el total en el año
        TotaldeHorasRequeridasP1 = (TotaldeHorasRequeridasS1P1+TotaldeHorasRequeridasS2P1)
        TotaldeImportedeMODP1 = (ImportedeMODS1P1+ImportedeMODS2P1)

        TotaldeHorasRequeridasP2 = (TotaldeHorasRequeridasS1P2+TotaldeHorasRequeridasS2P2)
        TotaldeImportedeMODP2 = (ImportedeMODS1P2+ImportedeMODS2P2)

        TotaldeHorasRequeridasP3 = (TotaldeHorasRequeridasS1P3+TotaldeHorasRequeridasS2P3)
        TotaldeImportedeMODP3 = (ImportedeMODS1P3+ImportedeMODS2P3)

        TotaldeHorasRequeridasxAño = (TotaldeHorasRequeridasxS1+TotaldeHorasRequeridasxS2)
        TotaldeMODxAño = (TotaldeMODxS1+TotaldeMODxS2)

        # Mostrar tabla
        fig, ax = plt.subplots(figsize=(13, 6), dpi=100)
        data = [["PRODUCTO CL","","",""],
                ["Unidades a producir",UnidadesaProducirS1P1,UnidadesaProducirS2P1,TotaldeUnidadesaProducirP1],
                ["Horas requeridas por unidad",HorasRequeridasxUnidadS1P1,HorasRequeridasxUnidadS2P1,HorasRequeridasxUnidadS1P1],
                ["Total de horas requeridas",val1,val2,val3],
                ["Cuota por hora",val4,val5,""],
                ["Importe de M.O.D.",val6,val7,val8],
                ["","","",""],
                ["PRODUCTO CE",val9,val10,val11],
                ["Unidades a producir",val12,val13,val14],
                ["Horas requeridas por unidad",val5,val6,val7],
                ["Total de horas requeridas",val18,val19,val20],
                ["Cuota por hora",val21,val22,""],
                ["Importe de M.O.D.",val23,val24,val25],
                ["","","",""],
                ["PRODUCTO CR","","",""],
                ["Unidades a producir",val26,val27,val28],
                ["Horas requeridas por unidad",val29,val30,val31],
                ["Total de horas requeridas",val26,val30,val31],
                ["Cuota por hora",val32,val33,""],
                ["Importe de M.O.D.",val34,val35,val36],
                ["","","",""],
                ["Total de horas requeridas por semestre",val37,val38,val39],
                ["Total de M.O.D. por semestre",val40,val41,val42]]
        column_labels = ["", "1er. Semestre", "2do. Semestre", "Total"+AñoAct]
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText = data, colLabels = column_labels, loc="center")
        table.set_fontsize(16)
        table.scale(1.2, 1.6)
        #plt.title("7.")
        plt.show()

    if PreModulo7 == 2:
        break

    # Modulo 8
    PreModulo8 = int(input("\nA continuacion sigue el Modulo 8.Presupuesto de Gastos Indirectos de Fabricación. ¿Desea continuar? \n\t[1]Si \n\t[2]No\n» "))

    if PreModulo8 == 1:
        print('\n\t--------- ENTRANDO AL MODULO 8 ---------')
        print('\n--------- Presupuesto de Gastos Indirectos de Fabricación ---------')
        print("\nPrimero se ingresará el 1er Semestre\n")

        DepreciacionGIFS1 = float(input("Ingrese el importe de la depreciacion del semestre 1\n» "))
        SegurosGIFS1 = float(input("Ingrese el importe de los seguros del semestre 1\n» "))
        MantenimientoGIFS1 = float(input("Ingrese el importe de los mantenimientos del semestre 1\n» "))
        EnergeticosGIFS1 = float(input("Ingre el importe de los energeticos del semestre 1\n» "))
        VariosGIFS1 = float(input("Ingrese el importe que tenga en varios del semestre 1\n» "))
        TotalGIFxS1 = (DepreciacionGIFS1+SegurosGIFS1+MantenimientoGIFS1+EnergeticosGIFS1+VariosGIFS1)

        print("\nAhora se ingresará del 2do Semestre\n")
        val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11 = 80000, 25000,58000,75000,25000,138000,125000,263000,263000,83050,3.17
        DepreciacionGIFS2 = float(input("Ingrese el importe de la depreciacion del semestre 2\n» "))
        SegurosGIFS2 = float(input("Ingrese el importe de los seguros del semestre 2\n» "))
        MantenimientoGIFS2 = float(input("Ingrese el importe de los mantenimientos del semestre 2\n» "))
        EnergeticosGIFS2 = float(input("Ingre el importe de los energeticos del semestre 2\n» "))
        VariosGIFS2 = float(input("Ingrese el importe que tenga en varios del semestre 2\n» "))
        TotalGIFxS2 = (DepreciacionGIFS2+SegurosGIFS2+MantenimientoGIFS2+EnergeticosGIFS2+VariosGIFS2)

        # Aqui se calculara el año
        DepreciacionGIFxAño = (DepreciacionGIFS1+DepreciacionGIFS2)
        SegurosxAño = (SegurosGIFS1+SegurosGIFS2)
        MantenimientoxAño = (MantenimientoGIFS1+MantenimientoGIFS2)
        EnergeticosxAño = (EnergeticosGIFS1+EnergeticosGIFS2)
        VariosxAño = (VariosGIFS1+VariosGIFS2)
        TotalGIFxAño = (TotalGIFxS1+TotalGIFxS2)

        # Coeficiente para determinar el costo por hora de Gastos Indirectos de Fabricacion ↓
        CostoxHoradeGIF = (TotalGIFxAño/TotaldeHorasRequeridasxAño)

         # Mostrar tabla
        fig, ax = plt.subplots(figsize=(13, 6), dpi=100)
        data = [["Depreciación",DepreciacionGIFS1,DepreciacionGIFS2,val1],
                ["Seguros",SegurosGIFS1,SegurosGIFS2,val2],
                ["Mantenimiento",MantenimientoGIFS1,MantenimientoGIFS2,val3],
                ["Energéticos",EnergeticosGIFS1,EnergeticosGIFS2,val4],
                ["Varios",VariosGIFS1,VariosGIFS2,val5],
                ["Total G.I.F. por semestre",val6,val7,val8],
                ["","","",""],
                ["Coeficiente para determinar","el costo por hora","de Gastos Indirectos",""],
                ["Total de G.I.F.","","",val9],
                ["(/) Total horas M.O.D. Anual","","",val10],
                ["(=) Costo por Hora de G.I.F.","","",val11]]
        column_labels = ["", "1er. Semestre", "2do. Semestre", "Total"+AñoAct]
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText = data, colLabels = column_labels, loc="center")
        table.set_fontsize(16)
        table.scale(1.2, 1.6)
        plt.title("8. Presupuesto de Gastos Indirectos de Fabricación")
        plt.show()

    if PreModulo8 == 2:
        break

    # Modulo 9
    PreModulo9 = int(input("\nA continuacion sigue el Modulo 9.Presupuesto de Gastos de Operación. ¿Desea continuar? \n\t[1]Si \n\t[2]No\n» "))

    if PreModulo9 == 1:
        print('\n--------- ENTRANDO AL MODULO 9 ---------')
        print('\n--------- Presupuesto de Gastos de Operación ---------')
        print("\nPrimero se ingresará el 1er Semestre\n")

        DepreciacionGOS1 = float(input("Ingrese el importe de la depreciacion del semestre 1\n» "))
        SueldosySalariosGOS1 = float(input("Ingrese el importe de Sueldos y Salarios del semestre 1\n» "))
        ComisionPorcentajeGOS1 = int(input("Ingrese la comision que se aplicara a las ventas proyectadas(Unicamente el numero, sin el %)\n» "))
        ComisionGOS1 = (ComisionPorcentajeGOS1/100)
        ComisionesGOS1 = (Totaldeventas1S*ComisionGOS1)
        VariosGOS1 = float(input("Ingrese el importe que tenga en varios del semestre 1\n» "))
        InteresesxObligacionesGOS1 = float(input("Ingrese el importe que tenga en intereses por obligaciones del semestre 1\n» "))
        TotaldeGastosdeOperacionGOS1 = (DepreciacionGOS1+SueldosySalariosGOS1+ComisionesGOS1+VariosGOS1+InteresesxObligacionesGOS1)

        print("\nAhora se ingresará del 2do Semestre\n")
        val1, val2, val3, val4, val5, val6, val7, val8 = 15000, 250000, 172330, 18000, 5000, 231750, 227580, 460330

        DepreciacionGOS2 = float(input("Ingrese el importe de la depreciacion del semestre 2\n» "))
        SueldosySalariosGOS2 = float(input("Ingrese el importe de Sueldos y Salarios del semestre 2\n» "))
        ComisionPorcentajeGOS2 = int(input("Ingrese la comision que se aplicara a las ventas proyectadas(Unicamente el numero, sin el %)\n» "))
        ComisionGOS2 = (ComisionPorcentajeGOS2/100)
        ComisionesGOS2 = (Totaldeventas2S*ComisionGOS2)
        VariosGOS2 = float(input("Ingrese el importe que tenga en varios del semestre 2\n» "))
        InteresesxObligacionesGOS2 = float(input("Ingrese el importe que tenga en intereses por obligaciones del semestre 2\n» "))
        TotaldeGastosdeOperacionGOS2 = (DepreciacionGOS1+SueldosySalariosGOS1+ComisionesGOS1+VariosGOS1+InteresesxObligacionesGOS1)

        # Aqui se calculara del año
        DepreciacionGOxAño = (DepreciacionGOS1+DepreciacionGOS2)
        SueldosySalariosGOxAño = (SueldosySalariosGOS1+SueldosySalariosGOS2)
        ComisionesGOxAño = (ComisionesGOS1+ComisionesGOS2)
        VariosGOxAño = (VariosGOS1+VariosGOS2)
        InteresesxObligacionesGOxAño = (InteresesxObligacionesGOS1+InteresesxObligacionesGOS2)
        TotaldeGastosdeOperacionGOxAño = (TotaldeGastosdeOperacionGOS1+TotaldeGastosdeOperacionGOS2)

         # Mostrar tabla
        fig, ax = plt.subplots(figsize=(13, 6), dpi=100)
        data = [["Depreciación",DepreciacionGOS1,DepreciacionGOS2,val1],
                ["Sueldos y Salarios",SueldosySalariosGOS1,SueldosySalariosGOS2,val2],
                ["Comisiones",ComisionPorcentajeGOS1,ComisionPorcentajeGOS2,val3],
                ["Varios",VariosGOS1,VariosGOS2,val4],
                ["Intereses por Obligaciones",InteresesxObligacionesGOS1,InteresesxObligacionesGOS2,val5],
                ["Total de Gasto de Operación:",val6,val7,val8]]
        column_labels = ["", "1er. Semestre", "2do. Semestre", "Total"+AñoAct]
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText = data, colLabels = column_labels, loc="center")
        table.set_fontsize(16)
        table.scale(1.2, 1.6)
        plt.title("9. Presupuesto de Gastos de Operación")
        plt.show()

    if PreModulo9 == 2:
        break

    # Modulo 10
    PreModulo10 = int(input("\nA continuacion sigue el Modulo 10.Determinacion del Costo Unitario de Productos Terminados. ¿Desea continuar? \n\t[1]Si \n\t[2]No\n» "))

    if PreModulo10 == 1:
        print('\n\t--------- ENTRANDO AL MODULO 10 ---------')
        print('\n--------- Determinacion del Costo Unitario de Productos Terminados ---------')

        print("Reciclando datos obtenidos anteriormente")
        # MO: Mano de obra
        CostoUnitarioMAP1 = (PreciodeCompraS2MA*RequerimentoMaterialS2P1MA)
        CostoUnitarioMBP1 = (PreciodeCompraS2MB*RequerimentoMaterialS2P1MB)
        CostoUnitarioMCP1 = (PreciodeCompraS2MC*RequerimentoMaterialS2P1MC)
        CostoUnitarioMOP1 = (CuotaxHoraS2P1*HorasRequeridasxUnidadS2P1)
        CostoUnitarioGIFP1 = (CostoxHoradeGIF*HorasRequeridasxUnidadS2P1)
        CostoUnitarioP1 = (CostoUnitarioMAP1+CostoUnitarioMBP1+CostoUnitarioMCP1+CostoUnitarioMOP1+CostoUnitarioGIFP1)

        CostoUnitarioMAP2 = (PreciodeCompraS2MA*RequerimentoMaterialS2P2MA)
        CostoUnitarioMBP2 = (PreciodeCompraS2MB*RequerimentoMaterialS2P2MB)
        CostoUnitarioMCP2 = (PreciodeCompraS2MC*RequerimentoMaterialS2P2MC)
        CostoUnitarioMOP2 = (CuotaxHoraS2P2*HorasRequeridasxUnidadS2P2)
        CostoUnitarioGIFP2 = (CostoxHoradeGIF*HorasRequeridasxUnidadS2P2)
        CostoUnitarioP2 = (CostoUnitarioMAP2+CostoUnitarioMBP2+CostoUnitarioMCP2+CostoUnitarioMOP2+CostoUnitarioGIFP2)

        CostoUnitarioMAP3 = (PreciodeCompraS2MA*RequerimentoMaterialS2P3MA)
        CostoUnitarioMBP3 = (PreciodeCompraS2MB*RequerimentoMaterialS2P3MB)
        CostoUnitarioMCP3 = (PreciodeCompraS2MC*RequerimentoMaterialS2P3MC)
        CostoUnitarioMOP3 = (CuotaxHoraS2P3*HorasRequeridasxUnidadS2P3)
        CostoUnitarioGIFP3 = (CostoxHoradeGIF*HorasRequeridasxUnidadS2P3)
        CostoUnitarioP3 = (CostoUnitarioMAP3+CostoUnitarioMBP3+CostoUnitarioMCP3+CostoUnitarioMOP3+CostoUnitarioGIFP3)
        
         # Mostrar tabla
        fig, ax = plt.subplots(figsize=(13, 6), dpi=120)
        data = [["Descripcion","Costo","Cantidad","Costo Unitario"],
                ["Material A",12,1,12],
                ["Material B",3,0.5,1.50],
                ["Material C",2,10,20],
                ["Mano de Obra",18,2,36],
                ["Gastos Indirectos de Fabricación",3.17,2,6.33],
                ["Costo Unitario","","",75.83],
                ["","","",""],
                ["","Producto CE","",""],
                ["Descripcion","Costo","Cantidad","Costo Unitario"],
                ["Material A",12,1.2,14.40],
                ["Material B",3,0.6,1.80],
                ["Material C",2,25,50],
                ["Mano de Obra",18,1,18],
                ["Gastos Indirectos de Fabricación",3.17,1,3.17],
                ["Costo Unitario","","",87.37],
                ["","","",""],
                ["","Producto CR","",""],
                ["Descripcion","Costo","Cantidad","Costo Unitario"],
                ["Material A",12,1.2,14.40],
                ["Material B",3,0.6,1.80],
                ["Material C",2,25,50],
                ["Mano de Obra",18,1,18],
                ["Gastos Indirectos de Fabricación",3.17,1,3.17],
                ["Costo Unitario","","",87.37],
                ["","","",""]]
        column_labels = ["", "PRODUCTO CL","","",""]
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText = data, colLabels = column_labels, loc="center")
        table.set_fontsize(12)
        table.scale(0.8, 0.9)
        #plt.title("10. Determinación del Costo Unitario de Productos Terminaods")
        plt.show()
        
    if PreModulo10 == 2:
        break

    # Modulo 11
    PreModulo11 = int(input("\nA continuacion sigue el Modulo 11.Valuación de Inventarios Finales. ¿Desea continuar? \n\t[1]Si \n\t[2]No\n» "))

    if PreModulo11 == 1:
        print('\n--------- ENTRANDO AL MODULO 11 ---------')
        print('\n--------- Valuación de Inventarios Finales ---------')

        print("Reciclando datos obtenidos anteriormente")

        CostoTotalMA = (InventarioFinalS2MA*PreciodeCompraS2MA)
        CostoTotalMB = (InventarioFinalS2MA*PreciodeCompraS2MB)
        CostoTotalMC = (InventarioFinalS2MA*PreciodeCompraS2MC)
        CostoTotalInventarioFinaldeMateriales = (CostoTotalMA+CostoTotalMB+CostoTotalMC)

        CostoTotalP1 = (InventarioFinalS2P1*CostoUnitarioP1)
        CostoTotalP2 = (InventarioFinalS2P2*CostoUnitarioP2)
        CostoTotalP3 = (InventarioFinalS2P3*CostoUnitarioP3)
        CostoTotalInventarioFinaldeProductoTerminado = (CostoTotalP1+CostoTotalP2+CostoTotalP3)
        
         # Mostrar tabla
        fig, ax = plt.subplots(figsize=(13, 6), dpi=100)
        data = [["Descripción","Unidades","Costo Unitario","Costo Total"],
                ["Material A",3,12,36],
                ["Material B",2.5,3,7500],
                ["Material C",1.8,2,3600],
                ["Inventario Final de Materiales","","",47100],
                ["","","",""],
                ["","Inventario Final de ","Producto Terminado",""],
                ["Descripcion","Unidades","Costo Unitario","Costo Total"],
                ["Producto CL",6500,75.83,492918],
                ["Producto CE",7500,87.37,655251],
                ["Producto CR",5000,68.75,343751],
                ["Inventario Final de Producto Terminado","","","1491919"],
                ["","","",""]]
        column_labels = ["", "Inventario Final", "de materiales", ""]
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText = data, colLabels = column_labels, loc="center")
        table.set_fontsize(16)
        table.scale(1.2, 1.6)
        plt.title("11. Valuación de Inventarios Finales")
        plt.show()
        
    if PreModulo11 == 2:
        break

    # Presupuesto Financiero
    print('\n--------- Presupuesto Financiero ---------')

    PrePF1 = int(input("\nA continuacion sigue Estado de Costo de Produccion y Ventas. ¿Desea continuar? \n\t[1]Si \n\t[2]No\n» "))

    if PrePF1 == 1:
        print('\n--------- Estado de Costo de produccion y Ventas ---------')
        print(f"Presupuesto del 1 de Enero al 31 de Diciembre del {AñoAct}")

        SaldoInicialdeM = float(input("Ingrese el saldo inicial de materiales\n» "))
        MaterialDisponible = (SaldoInicialdeM+ComprasTotalesM)
        MaterialesUtilizados = (MaterialDisponible-CostoTotalInventarioFinaldeMateriales)
        CostodeProduccion = (MaterialesUtilizados+TotaldeMODxAño+TotalGIFxAño)
        InventarioInicialdeProductosTerminados = float(input("Ingrese el inventario inicial de productos terminados\n» "))
        TotaldeProduccionDisponible = (CostodeProduccion+InventarioInicialdeProductosTerminados)
        CostodeVentas = (TotaldeProduccionDisponible-CostoTotalInventarioFinaldeProductoTerminado)
        
         # Mostrar tabla
        fig, ax = plt.subplots(figsize=(13, 6), dpi=100)
        data = [["Saldo Inicial de Materiales","","",45000],
                ["(+) Compras de Materiales","","",2141010],
                ["(=) Material Disponible","","",2186010],
                ["(-) Inventario Final de Materiales","","",47100],
                ["(=) Materiales Utilizados","","",2138910],
                ["(+) Mano de Obra Directa","","",1350900],
                ["(+) Gastos de Fabricación Indirectos","","",263000],
                ["(=) Costo de Producción","","",3752810],
                ["(+) Inventario Inicial de Productos Terminados","","",135000],
                ["(=) Total de Producción Disponible","","",3887810],
                ["(-) Inventario Final de Productos Terminados","","",1491919],
                ["(=) Costo de Ventas","","",2395891]]
        column_labels = ["", "1er. Semestre", "2do. Semestre", "Total"+AñoAct]
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText = data, colLabels = column_labels, loc="center")
        table.set_fontsize(16)
        table.scale(1.2, 1.6)
        #plt.title("8. Presupuesto de Gastos Indirectos de Fabricación")
        plt.show()
        
    if PrePF1 == 2:
        break

    # Estado de resultados
    PrePF2 = int(input("\nA continuacion sigue Estado de Resultados. ¿Desea continuar? \n\t[1]Si \n\t[2]No\n» "))

    if PrePF2 == 1:
        print('\n--------- Estado de Resultados ---------')
        print(f"Presupuesto del 1 de Enero al 31 de Diciembre del {AñoAct}")

        UtilidadBruta = (TotaldeVentasdelaño-CostodeVentas)
        UtilidaddeOperacion = (UtilidadBruta-TotaldeGastosdeOperacionGOxAño)
        ISRPorcentaje = int(input("Ingrese la Tasa de ISR(Unicamente el numero, sin el %)\n» "))
        ISRConversion = (ISRPorcentaje/100)
        ISr = (UtilidaddeOperacion*ISRConversion)
        PTUPorcentaje = int(input("Ingrese la Tasa de PTU(Unicamente el numero, sin el %)\n» "))
        PTUConversion = (PTUPorcentaje/100)
        PTu = (UtilidaddeOperacion*PTUConversion)
        UtilidadNeta = (UtilidaddeOperacion-ISr-PTu)
          
         # Mostrar tabla
        fig, ax = plt.subplots(figsize=(13, 6), dpi=100)
        data = [["Ventas","","",17233000],
                ["(-) Costo de Ventas","","",2395891],
                ["(=) Utilidad Bruta","","",14837109],
                ["(-) Gastos de Operación","","",460330],
                ["(=) Utilidad de Operación","","",14376779],
                ["(-) ISR","","",5031873],
                ["(-) PTU","","",1437678],
                ["(=) Utilidad Neta","","",7907229]]
        column_labels = ["", "1er. Semestre", "2do. Semestre", "Total"+AñoAct]
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText = data, colLabels = column_labels, loc="center")
        table.set_fontsize(16)
        table.scale(1.2, 1.6)
        #plt.title("8. Presupuesto de Gastos Indirectos de Fabricación")
        plt.show()
        
    if PrePF2 == 2:
        break

    # Estado de flujo de efectivo
    PrePF3 = int(input("\nA continuacion sigue Estado de Flujo de Efectivo. ¿Desea continuar? \n\t[1]Si \n\t[2]No\n» "))

    if PrePF3 == 1:
        print('\n--------- Estado de Flujo de Efectivo ---------')
        print(f"Presupuesto del 1 de Enero al 31 de Diciembre del {AñoAct}")

        SaldoInicialdeEfectivo = float(input("Ingrese el saldo inicial de efectivo\n» "))
        TotaldeEntradasEFE = (CobranzaAñoAnt+CobranzaAñoAnt)
        EfectivoDisponible = (SaldoInicialdeEfectivo+TotaldeEntradasEFE)
        CompradeActivoFijo = float(input("Ingrese el importe de la compra de activo fijo(maquinaria)\n» "))
        PagoGIF = (TotalGIFxAño-DepreciacionGIFxAño)
        PagoGO = (TotaldeGastosdeOperacionGOxAño-DepreciacionGOxAño)
        PagoISRAñoAnt = float(input(f"Ingrese el ISR por pagar en {AñoAnt}\n» "))
        PagoISRAñoAct = float(input(f"Ingrese el ISR por pagar en {AñoAct}\n» "))
        TotaldeSalidasEFE = (ProveedoresAñoAct+ProveedoresAñoAnt+TotaldeMODxAño+PagoGIF+PagoGO+CompradeActivoFijo+PagoISRAñoAnt+PagoISRAñoAct)
        FlujodeEfectivoActual = (EfectivoDisponible-TotaldeSalidasEFE)
        
         # Mostrar tabla
        fig, ax = plt.subplots(figsize=(13, 6), dpi=100)
        data = [["Saldo Inicial de Efectivo","","",100000],
                ["Entradas:","","",""],
                ["Cobranza 2016","",13786400,""],
                ["Cobranza 2015","",80000,""],
                ["Total de Entradas","","",13866400],
                ["Efectivo Disponible","","",13966400],
                ["Salidas:","","",""],
                ["Proveedores 2016",1070505,"",""],
                ["Proveedores 2015",33500,"",""],
                ["Pago Mano de Obra Directa",1350900,"",""],
                ["Pago Gastos Indirectos de Fabricación",183000,"",""],
                ["Pago de Gastos de Operación",445330,"",""],
                ["Compra de Activo Fijo (Maquinaria)",85000,"",""],
                ["Pago ISR 2015",50000,"",""],
                ["Pago ISR 2016","","",""],
                ["Total de Salidas","","",3218235],
                ["Flujo de Efectivo Actual","","",10748165]]
        column_labels = ["", "1er. Semestre", "2do. Semestre", "Total"+AñoAct]
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText = data, colLabels = column_labels, loc="center")
        table.set_fontsize(16)
        table.scale(1.2, 1.6)
        #plt.title("8. Presupuesto de Gastos Indirectos de Fabricación")
        plt.show()
        
    if PrePF3 == 2:
        break

    # Balance general
    PrePF4 = int(input("\nA continuacion sigue Balance General. ¿Desea continuar? \n\t[1]Si \n\t[2]No\n» "))

    if PrePF4 == 1:
        print('\n--------- Balance General ---------')
        print(f"Presupuesto al 31 de Diciembre del {AñoAct}")

        print("Activo ↓")
        print("Circulante")
        DeduoresDiversos = float(input("Ingrese el importe de deudores diversos\n» "))
        FuncionariosYEmpleados = float(input("Ingrese el importe de Funcionarios y Empleados\n» "))
        TotalActivosCirculantes = (FlujodeEfectivoActual+SaldodeClientesAñoAct+DeduoresDiversos+FuncionariosYEmpleados+CostoTotalInventarioFinaldeMateriales+CostoTotalInventarioFinaldeProductoTerminado)
        print("No Circulante")
        Terreno = float(input("Ingrese el importe del terreno\n» "))
        PlantayEquipoTEMP = float(input("Ingrese el importe de planta y Equipo\n» "))
        PlantayEquipo = (PlantayEquipoTEMP+CompradeActivoFijo)
        DepreciacionAcumuladaTEMP = float(input("Ingrese el importe de la depreciacion acumulada\n» "))
        DepreciacionAcumulada = (DepreciacionAcumuladaTEMP+DepreciacionGOxAño+DepreciacionGIFxAño)
        TotaActivosNoCiruclante = (Terreno+PlantayEquipo) - DepreciacionAcumulada
        ActivoTotal = (TotalActivosCirculantes+TotaActivosNoCiruclante)
        print("PASIVO ↓")
        print("Corto plazo")
        DocumentosxPagar = float(input("Ingrese los documentos por pagar\n» "))
        TotaldePasivoCP = (SaldodeProveedoresAñoAct+DocumentosxPagar+ISr+PTu)
        print("Largo plazo")
        PrestamosBancarios = float(input("Ingrese el importe de los prestamos bancarios\n» "))
        TotaldePasivoLP = (PrestamosBancarios)
        PasivoTotal = (TotaldePasivoCP+TotaldePasivoLP)
        print("CAPITAL CONTABLE ↓")
        CapitalContribuido = float(input("Ingrese el importe del capital contribuido\n» "))
        CapitalGanado = float(input("Ingrese el importe del capital ganado\n» "))
        TotaldeCapitalContable = (CapitalContribuido+CapitalGanado+UtilidadNeta)
        SumadePasivoyCapital = (PasivoTotal+TotaldeCapitalContable)
        Comprobacionde0 = (ActivoTotal-SumadePasivoyCapital) # ESTO DEBERIA DAR 0 SI SE HIZO CORRECTAMENTE
        
         # Mostrar tabla
        fig, ax = plt.subplots(figsize=(13, 6), dpi=130)
        data = [["ACTIVO","","",""],
                ["Circulante","","",""],
                ["Efectivo",10748165,"",""],
                ["Clientes",3446600,"",""],
                ["Deudores Diversos",35000,"",""],
                ["Funcionarios y Empleados",10500,"",""],
                ["Inventario de Materiales",47100,"",""],
                ["Inventario de Producto Terminado",1491919,"",""],
                ["Total de Activos Circulantes:","","",15779224],
                ["","","",""],
                ["No Circulante","","",""],
                ["Terreno","",905000,""],
                ["Planta y Equipo","",1585000,""],
                ["Depreciación Acumulada","",745000,""],
                ["Total Activos No Circulante","","",1745000],
                ["","","",""],
                ["ACTIVO TOTAL","","",17524284],
                ["","","",""],
                ["PASIVO","","",""],
                ["Corto Plazo","","",""],
                ["Proveedores","",1070505,""],
                ["Documentos por Pagar","",95000,""],
                ["ISR por Pagar","",5031873,""],
                ["PTU por Pagar","",1437678,""],
                ["Total de Pasivo Corto Plazo:","","",7635056],
                ["","","",""],
                ["Largo Plazo","","",""],
                ["Préstamos bancarios",120000,"",""],
                ["Total de Pasivo Largo Plazo:","","",120000],
                ["","","",""],
                ["PASIVO TOTAL","","",7755056],
                ["","","",""],
                ["CAPITAL CONTABLE","","",""],
                ["Capital Contribuido","",1500000,""],
                ["Capital Ganado","",362000,""],
                ["Utilidad del Ejercicio","",7907229,""],
                ["Total de Capital Contable","","",9769229,
                ["","","",""],
                ["SUMA DE PASIVO Y CAPITAL","","",17524284]]
        column_labels = ["", "1er. Semestre", "2do. Semestre", "Total"+AñoAct]
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText = data, colLabels = column_labels, loc="center")
        table.set_fontsize(12)
        table.scale(0.8, 0.9)
        #plt.title("8. Presupuesto de Gastos Indirectos de Fabricación")
        plt.show()
        
    if PrePF4 == 2:
        break