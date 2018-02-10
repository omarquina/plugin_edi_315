#mapping-script

def filename(channeldict,filename,ta,*args,**kwargs):
    print "-------------------------"
    print "FILENAME(): "
    print "   filename: ",filename
    print "   ta: ",ta
    print "-------------------------"
    ta.synall()
    if ta.botskey:
        return filename + ta.botskey
    else:
        return filename


def main(inn,out):
    #print "---------- MAPPING del EDI FILE 315 DPWORLD ----- "
    #print "INN: ", inn.root
    out.ta_info['topartner'] = 'ZZDPWO'
    out.ta_info['frompartner'] = 'ZZVECO'
    print "PARAMETROS desde RESULT: ", inn.root
    equipo = inn.root['equipo']
    fecha = inn.root['fecha']
    #liberar = inn.root['liberar']
    status = inn.root['status']
    print "EQUIPO: ",equipo
    siglas_contenedor,numero = equipo.split('-')
    equipo_ajustado = siglas_contenedor + numero
    print "numero contenedor: ",numero
    print "siglas: ",siglas_contenedor
    codigo_inicial_contenedor = numero[0:(len(numero)-1)]
    ultimo_digito_contenedor = numero[(len(numero)-1)]
    id_mensaje = 0
    out.ta_info['filename'] = equipo_ajustado + ".edi"
    #print "--------------------------"
    #print "IN.ta_info: ",inn.ta_info
    #print "--------------------------"
    out.ta_info['equipo'] = equipo_ajustado
    #print "--------------------------"
    #print "OUT.ta_info: ",out.ta_info
    print "--------------------------"
    print "OUT.ROOT: ",dir(out.root)
    # Picar el contenedor
    # INICIO DEL MENSAJE
    out.put({'BOTSID':'ST','ST01':315})
    # Codigo del mensaje, lo hace unico para una transaccion
    out.put({'BOTSID':'ST','ST02':2457277})
    # CONTENIDO DEL MENSAJE
    out.put({'BOTSID':'ST'},{'BOTSID':'B4','B401':315})
    # Codigo para RELEASE/HOLE del equipo
    #out.put({'BOTSID':'ST'},{'BOTSID':'B4','B403':'UA'})
    out.put({'BOTSID':'ST'},{'BOTSID':'B4','B403':status})
    out.put({'BOTSID':'ST'},{'BOTSID':'B4','B405':siglas_contenedor})
    # Codigo del Contenedor con 6 digitos
    out.put({'BOTSID':'ST'},{'BOTSID':'B4','B406':codigo_inicial_contenedor})
    # ultimo codigo del contenedor, creo que es una verificacion
    out.put({'BOTSID':'ST'},{'BOTSID':'B4','B407':ultimo_digito_contenedor})
    # Codigo del contenedor completo
    out.put({'BOTSID':'ST'},{'BOTSID':'N9','N901':'EQ'})
    out.put({'BOTSID':'ST'},{'BOTSID':'N9','N902':equipo_ajustado})
    # Codigo del dueno del contenedor, al parecer
    out.put({'BOTSID':'ST'},{'BOTSID':'Q2','Q201':'9303754'})
    out.put({'BOTSID':'ST'},{'BOTSID':'Q2','Q210':'ZZ'})
    out.put({'BOTSID':'ST'},{'BOTSID':'Q2','Q211':'ZIMU'})
    out.put({'BOTSID':'ST'},{'BOTSID':'Q2','Q212':'L'})
    # CIERRE DEL MENSAJE 
    #    cantidad de lineas del mensaje
    out.put({'BOTSID':'ST'},{'BOTSID':'SE','SE01':5})
    # Codigo de cierre del mensaje, debe ser igual al inicio del mensaje
    out.put({'BOTSID':'ST'},{'BOTSID':'SE','SE02':2457277})

    print "SAlida: ",out.get({'BOTSID':'ST'},{'BOTSID':'B4','B401':None})
    print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    #out.put({'BOTSID':'articles'})          #have to put root element in first.
    #for article in inn.root['articles']:    #map the data from the query to the xml message 
    #    art = out.putloop({'BOTSID':'articles'},{'BOTSID':'article'})       #make new xml entity 'article' within root
    #    art.put({'BOTSID':'article','ccodeid':article[0],'leftcode':article[1],'rightcode':article[2]})
