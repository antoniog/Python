#!/usr/bin/env python
# This Python file uses the following encoding: utf-8

import sys
try:
    import pygtk
    pygtk.require("2.24")
except:
    pass
try:
    import gtk
    import gtk.glade
    import sys
    import datetime
    import sqlite3 as lite
except:
    sys.exit(1)


class mycounter:

    def __init__(self):

        #Configuro el archivo Glade
        self.gladefile = "mycounter.glade"
        self.wTree = gtk.glade.XML(self.gladefile, "mainWindow")

        #Creo el diccionario y lo destruyo
        dic = {"on_mainWindow_destroy": gtk.main_quit, "on_AddProceso": self.OnAddProceso}
        self.wTree.signal_autoconnect(dic)

        #Algunas variables para usarlas luego
        self.cID = 0
        self.cIDrep = 1
        self.cTstart = 2
        self.cTtotal = 3

        self.sID = "ID"
        self.sIDrep = "NRepa"
        self.sTstart = "Comienzo"
        self.sTtotal = "Total"

        #Genera vista de árbol del Widget Tree
        self.procesosView = self.wTree.get_widget("procesosView")
        #Añado toda la lista de columnas al procesosView
        self.AddProcesoListColumn(self.sID, self.cID)
        self.AddProcesoListColumn(self.sIDrep, self.cIDrep)
        self.AddProcesoListColumn(self.sTstart, self.cTstart)
        self.AddProcesoListColumn(self.sTtotal, self.cTtotal)

        #Creo el modelo procesosList para usar con procesosView
        self.procesosList = gtk.ListStore(str, str, str, str)
        #Pego el modelo a la vista de árbol
        self.procesosView.set_model(self.procesosList)

    def AddProcesoListColumn(self, title, columnId):
        """Esta función añade una columna a la vista lista.
        Primero crea el gtk.TreeviewColumn y despues configura
        algunas propiedades necesarias"""

        column = gtk.TreeViewColumn(title, gtk.CellRendererText(), text=columnId)
        column.set_resizable(True)
        column.set_sort_column_id(columnId)
        self.procesosView.append_column(column)

    def OnAddProceso(self, widget):
        """Llamado cuando el usuario quiere añadir un proceso"""
        #Crea el dialogo, lo muestra y guara el resultado
        ProcesoDlg = procesoDialog()
        result, newProceso = ProcesoDlg.run()

        if (result == gtk.RESPONSE_OK):
            """El usuario hace click en OK, añadimos el proceso a la lista"""
            self.procesosList.append(newProceso.getList())


class procesoDialog:
    """Esta clase muestra el dialogo del añadir proceso"""

    def __init__(self, ID="", NRepa="", Comienzo="", Total=""):

        #Configura el archivo Glade
        self.gladefile = "mycounter.glade"
        #Configura el proceso que mandaremos
        self.proceso = Proceso(ID, NRepa, Comienzo, Total)

    def run(self):
        """Esto mostrara el mycounter dialogo"""

        #Carga el diálogo del archivo glade
        self.wTree = gtk.glade.XML(self.gladefile, "ProcesoDlg")
        #Carga el dialogo widget actual
        self.dlg = self.wTree.get_widget("ProcesoDlg")
        #Carga todos los wigets y su texto
#        self.enID = self.wTree.get_widget("enID")
#        self.enID.set_text(self.proceso.ID)
        self.enNRepa = self.wTree.get_widget("enNRepa")
        self.enNRepa.set_text(self.proceso.NRepa)
        self.enComienzo = self.wTree.get_widget("enComienzo")
        self.enComienzo.set_text(self.proceso.Comienzo)
#        self.enTotal = self.wTree.get_widget("enTotal")
#        self.enTotal.set_text(self.proceso.Total)

        #Ejecuta el diálogo y guarda la respuesta
        self.result = self.dlg.run()
        #Carga el resultado de los campos introducidos
#        self.proceso.ID = self.enID.get_text()
        self.proceso.NRepa = self.enNRepa.get_text()
        self.proceso.Comienzo = self.enComienzo.get_text()
#        self.proceso.Total = self.enTotal.get_text()

        #Hemos acabado con el diálogo, lo destruimos boom
        self.dlg.destroy()

        #Retornamos junto con el proceso
        return self.result, self.proceso


class Proceso:
    """Esta clase representa la información del proceso"""

    def __init__(self, ID="", NRepa="", Comienzo="", Total=""):

        self.ID = ID
        self.NRepa = NRepa
        self.Comienzo = Comienzo
        self.Total = Total

    def getList(self):
        """Esta función se trae la lista de vino, así se puede obtener
        fácilmente el resultado"""
        return [self.ID, self.NRepa, self.Comienzo, self.Total]

if __name__ == "__main__":
    proceso = mycounter()
    gtk.main()
