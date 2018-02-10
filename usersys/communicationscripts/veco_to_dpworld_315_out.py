import os
import bots.botslib as botslib

def filename(channeldict,filename,ta,*args,**kwargs):
    print "    veco_TO_DPWORLD_315: ta", ta
    print "    veco_TO_DPWORLD_315: filename", filename
    print "    veco_TO_DPWORLD_315: args", args
    print "    veco_TO_DPWORLD_315: kwargs", kwargs
    #ta_list = botslib.trace_origin(ta=ta,where={'status':EXTERNIN})
    #filename_in = os.path.basename(ta_list[0].filename) # just filename, remove path
    #return filename + filename_in
    return 'EQUIPO.edi'

def connect(channeldict,*args,**kwargs):
    #open connection to the sqlite database
    #the connection is returned.
    #return sqlite3.connect(database=channeldict['path'])
    print "?????????????????????? INICIO DPWORLD OUT"
    print "     Creando conexion PARA OUT DPWORLD: CHANNEL DICT:",channeldict
    print "     Creando conexion PARA OUT DPWORLD: args:",args
    print "     Creando conexion PARA OUT DPWORLD: KWargs:",kwargs

def main(channeldict,filename,ta,*args,**kwargs):
     print "      MAIN DE OUT"
     print "      MAIN OUT channeldict: ",channeldict
     print "      MAIN OUT filename",filename
     print "      MAIN OUT TA:",ta
     print "      MAIN OUT ARGS: ",args
     print "      MAIN OUT kwarg: ",kwargs

def disconnect(channeldict,*args,**kwargs):
     print "   DISCONNECT OUT DPWORLD"
