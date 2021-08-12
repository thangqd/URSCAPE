#!/usr/bin/env python
# -*- coding: utf-8 -*-

# --------------------------------------------------------
#    urscape_library - urscape operation functions
# --------------------------------------------------------

import io
import re
import csv
import sys
import locale
import random
#import xlrd
import urllib
import argparse
import json
import logging
import numbers
import requests
import zipfile
import stat
import operator
import tempfile
import urllib.request
import os.path
import xml.etree.ElementTree

from qgis.core import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.gui import QgsMessageBar
from math import *
# Used instead of "import math" so math functions can be used without "math." prefix
import qgis.utils
import processing   
from osgeo import gdal
from osgeo import ogr
from osgeo import osr
import os 

basemap_names = ['Google Maps', 'Google Satellite',\
                'Google Satellite Hybrid','Google Terrain', \
                'Google Terrain Hybrid','Bing Virtual Earth',\
                'Carto Antique','Carto Dark',\
                'Carto Eco','Carto Light',\
                'Esri Boundaries and Places','Esri Dark Gray',\
                'ESri DeLorme','Esri Imagery',\
                'Esri Light Gray','Esri National Geographic',\
                'Esri Ocean','Esri Physical',\
                'Esri Shaded Relief','Esri Street',\
                'Esri Terrain','Esri Topographic',\
                'F4 Map - 2D','Stamen Toner',
                'Stamen Toner Background','Stamen Toner Hybrid',\
                'Stamen Toner Lite','Stamen Terrain',\
                'Stamen Terrain Background','Stamen Watercolor',\
                'Wikimedia Maps','Vietbando Maps',\
                'Vietnam OSM Maps'
             ]
basemap_urls = ['mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}','mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',\
                'mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}','mt1.google.com/vt/lyrs=t&x={x}&y={y}&z={z}',\
                'mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}','ecn.t3.tiles.virtualearth.net/tiles/a{q}.jpeg?g=1',\
                'cartocdn_a.global.ssl.fastly.net/base-antique/{z}/{x}/{y}.png','a.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png',\
                'cartocdn_a.global.ssl.fastly.net/base-eco/{z}/{x}/{y}.png', 'a.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.pn',\
                'server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}','server.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}',\
                'server.arcgisonline.com/arcgis/rest/services/Specialty/DeLorme_World_Base_Map/MapServer/tile/{z}/{y}/{x}', 'server.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',\
                'server.arcgisonline.com/arcgis/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}','server.arcgisonline.com/arcgis/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}',\
                'server.arcgisonline.com/arcgis/rest/services/Ocean_Basemap/MapServer/tile/{z}/{y}/{x}','server.arcgisonline.com/arcgis/rest/services/World_Physical_Map/MapServer/tile/{z}/{y}/{x}',\
                'server.arcgisonline.com/arcgis/rest/services/World_Shaded_Relief/MapServer/tile/{z}/{y}/{x}', 'server.arcgisonline.com/arcgis/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',\
                'server.arcgisonline.com/arcgis/rest/services/World_Terrain_Base/MapServer/tile/{z}/{y}/{x}','server.arcgisonline.com/arcgis/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}',\
                'tile1.f4map.com/tiles/f4_2d/{z}/{x}/{y}.png','a.tile.stamen.com/toner/{z}/{x}/{y}.png',\
                'a.tile.stamen.com/toner-background/{z}/{x}/{y}.png','a.tile.stamen.com/toner-hybrid/{z}/{x}/{y}.png',\
                'a.tile.stamen.com/toner-lite/{z}/{x}/{y}.png','a.tile.stamen.com/terrain/{z}/{x}/{y}.png',\
                'a.tile.stamen.com/terrain-background/{z}/{x}/{y}.png','c.tile.stamen.com/watercolor/{z}/{x}/{y}.jpg',\
                'maps.wikimedia.org/osm-intl/{z}/{x}/{y}.png','images.vietbando.com/ImageLoader/GetImage.ashx?Ver%3D2016%26LayerIds%3DVBD%26Y%3D%7By%7D%26X%3D%7Bx%7D%26Level%3D%7Bz%7D',\
                'thuduc-maps.urscape.vn/thuducserver/gwc/service/wmts?layer=thuduc:thuduc_maps&style=&tilematrixset=EPSG:900913&Service=WMTS&Request=GetTile&Version=1.0.0&Format=image/png&TileMatrix=EPSG:900913:{z}&TileCol={x}&TileRow={y}'
                ]                 

#--------------------------------------------------------
#    Add basemap
# --------------------------------------------------------
def urscape_creategrid(gridtype,layer,cellsize, gridCRS,output,status_callback = None):		
    ## create skeleton/ media axis  
    i = 0
    steps = 2
    parameters1 = { 'TYPE': gridtype,
                   'EXTENT': layer.extent(),
                   'CRS': gridCRS,			
                   'HSPACING' : cellsize,		
                   'VSPACING' : cellsize,
                   'OUTPUT' : 'memory:grid_unclip'} 
    #points = processing.runAndLoadResults('qgis:creategrid', parameters1)
    grid_unclip = processing.run('qgis:creategrid', parameters1)
    i+=1
    percent = int((i/steps)*100)
    label = str(i)+ '/'+ str(steps)+ '. create grid'    
    if status_callback:
        status_callback(percent,label)
    else:
        print(label)  

    parameters2 = { 'INPUT': grid_unclip['OUTPUT'],
                   'OVERLAY': layer,
                   'OUTPUT' : output} 
    processing.runAndLoadResults('qgis:clip', parameters2)
    i+=1 

    percent = int((i/steps)*100)
    label = str(i)+ '/'+ str(steps)+ '. clip'    
    if status_callback:
        status_callback(percent,label)
    else:
        print(label)                 

    return

def urscape_creategrid2(gridtype,layer,cellsize, gridCRS,excluded_layers,output,status_callback = None):		
    i = 0
    steps = 4
    parameters1 = { 'TYPE': gridtype,
                   'EXTENT': layer.extent(),
                   'CRS': gridCRS,			
                   'HSPACING' : cellsize,		
                   'VSPACING' : cellsize,
                   'OUTPUT' : 'memory:grid_unclip'} 
    grid_unclip = processing.run('qgis:creategrid', parameters1)    
    i+=1 
    percent = int((i/steps)*100)
    label = str(i)+ '/'+ str(steps)+ '. create grid'
    if status_callback:
        status_callback(percent,label)
    else:
        print(label) 

    parameters2 = { 'INPUT': grid_unclip['OUTPUT'],
                   'OVERLAY': layer,
                   'OUTPUT' : 'memory:grid_clip'} 
    grid_clip = processing.run('qgis:clip', parameters2)
    i+=1
    percent = int((i/steps)*100)
    label = str(i)+ '/'+ str(steps)+ '. clip'
    if status_callback:
        status_callback(percent,label)
    else:
        print(label) 
      
    parameters3 = { 
                    'LAYERS' : excluded_layers,
                    'OUTPUT' : 'memory:merge_layer'} 
    merge_layer = processing.run('qgis:mergevectorlayers', parameters3)
    i+=1
    percent = int((i/steps)*100)
    label = str(i)+ '/'+ str(steps)+ '. merge'
    if status_callback:
        status_callback(percent,label)
    else:
        print(label)         
    
    # parameters4 = { 
    #             'INPUT': merge_layer['OUTPUT'],
    #             'AGGREGATES' : [], 
    #             'GROUP_BY' : 'NULL', 
    #             'OUTPUT' : 'memory:aggregate_layer'} 
    # aggregate_layer = processing.run('qgis:aggregate', parameters4)
    # i+=1
    # percent = int((i/steps)*100)
    # label = str(i)+ '/'+ str(steps)+ '. aggregate'    
    # if status_callback:
    #     status_callback(percent,label)
    # else:
    #     print(label)

    parameters5 = { 
                'INPUT': grid_clip['OUTPUT'],
                'INTERSECT': merge_layer['OUTPUT'],
                'PREDICATE' : [2] , # disjoint 
                #'OUTPUT' : 'memory:grid_final'
                'OUTPUT' : output}
    processing.runAndLoadResults('qgis:extractbylocation', parameters5)
    i+=1
    percent = int((i/steps)*100)
    label = str(i)+ '/'+ str(steps)+ '. final grid'    
    if status_callback:
        status_callback(percent,label)
    else:
        print(label)
    return

      
#--------------------------------------------------------
#    Add basemap
# --------------------------------------------------------

def urscape_basemap_load():
    sources = []
    for basemap_name in basemap_names:
        idx = basemap_names.index(basemap_name)
        basemap_url = basemap_urls[idx]
        basemap_uri = "http://"+basemap_url
        sources.append(["connections-xyz",basemap_name,"","","",basemap_uri,"","22","0"])
    i = 0
    for source in sources:
        connectionType = source[0]
        connectionName = source[1]
        QSettings().setValue("qgis/%s/%s/authcfg" % (connectionType, connectionName), source[2])
        QSettings().setValue("qgis/%s/%s/password" % (connectionType, connectionName), source[3])
        QSettings().setValue("qgis/%s/%s/referer" % (connectionType, connectionName), source[4])
        QSettings().setValue("qgis/%s/%s/url" % (connectionType, connectionName), source[5])
        QSettings().setValue("qgis/%s/%s/username" % (connectionType, connectionName), source[6])
        QSettings().setValue("qgis/%s/%s/zmax" % (connectionType, connectionName), source[7])
        QSettings().setValue("qgis/%s/%s/zmin" % (connectionType, connectionName), source[8])
        i+=1
        print(str(i) + ('. ')+ source[1] +' added')        
        try:
            qgis.utils.iface.reloadConnections()    
        except:
            print('Reload Connection failed!')
         
def urscape_basemap(basemap_name):
    idx = basemap_names.index(basemap_name)
    basemap_url = basemap_urls[idx]
    if ( basemap_name == 'Bing Virtual Earth' or basemap_name == 'Vietbando Maps') :
        basemap_uri = "type=xyz&url=http://"+basemap_url
        xyz_layer = QgsRasterLayer(basemap_uri,basemap_name, 'wms') 
        if xyz_layer.isValid():    
                QgsProject.instance().addMapLayer(xyz_layer)
    else:
        basemap_uri = "type=xyz&zmin=0&zmax=22&url=http://"+requests.utils.quote(basemap_url)
        xyz_layer = qgis.utils.iface.addRasterLayer(basemap_uri, basemap_name, "wms") 
        if not xyz_layer.isValid():
             QMessageBox.warning(None, "Basemap", 'Basemap loaded error!')        

    basemap_uri1 = "http://"+basemap_url
    source = ["connections-xyz",basemap_name,"","","",basemap_uri1,"","22","0"]   
    connectionType = source[0]
    connectionName = source[1]
    QSettings().setValue("qgis/%s/%s/authcfg" % (connectionType, connectionName), source[2])
    QSettings().setValue("qgis/%s/%s/password" % (connectionType, connectionName), source[3])
    QSettings().setValue("qgis/%s/%s/referer" % (connectionType, connectionName), source[4])
    QSettings().setValue("qgis/%s/%s/url" % (connectionType, connectionName), source[5])
    QSettings().setValue("qgis/%s/%s/username" % (connectionType, connectionName), source[6])
    QSettings().setValue("qgis/%s/%s/zmax" % (connectionType, connectionName), source[7])
    QSettings().setValue("qgis/%s/%s/zmin" % (connectionType, connectionName), source[8])
    qgis.utils.iface.reloadConnections()  