''' This communication script reads the article-information from sqlite database. 
    A sqlite database is provided in this plugin.
    The parameters for the database-connection (in case of sqlite: only the path to the database) is in the channel (as configured in the GUI).
    For more information about the SQLite database connector: see regular python documentation about this.
    For other databases there are other database connectors, google them for the right information.
'''
#import sqlite3

def connect(channeldict):
    #open connection to the sqlite database
    #the connection is returned.
    #return sqlite3.connect(database=channeldict['path'])
    print "Creando conexion a la BD PARa el SCI"

def incommunicate(channeldict,dbconnection):
    ##cursor = dbconnection.cursor()
    ##cursor.execute(u'''SELECT ccodeid,leftcode,rightcode FROM ccode''')
    #use a python dictionary to put results from query in.
    #if passing the results without dictionary: bots would split this is in separate message; in this case that is not what you want.
    ##results =  {'articles':cursor.fetchall()}        
    ##cursor.close()
    #the resulting data is returned for use in the mapping script. 
    #please note the content in the database is not removed; to do that a seperate delete query would have to be used.
    #################################################################################################################################3
    print "INCOMUNICATE: Procesando los datos de la BD, para obtener los equipos a liberaer y/o bloquear para DPworld Inicialmente"
    #results = [{'equipo': 'FSTA0000001','fecha':'2018-02-05','status': 'UA',}]
    results = [
        {'equipo': 'XXXX-8621513','fecha':'2018-02-05','status': 'UA'},
        #{'equipo': 'ZCSU-8621513','fecha':'2018-02-05','status': 'UA'},
        #{'equipo': 'ZCSU-8621513','fecha':'2018-02-05','status': 'PU'}
    ]
    print "RESULTS: ", results
    return results
    
    
def disconnect(channeldict,dbconnection):
    #dbconnection.close()
    print "CERRANDO CONEXion"


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


def archivename(channeldict,idta,filename,*args,**kwargs):
     print "-----------------------"
     print "      ARCHIVE NAME:   Filename ",filename
     print "      ARCHIVE NAME:   IDTA: ",idta
     print "-----------------------"
      
