#!/usr/bin/env python
# -*- coding: utf-8 -*-

# --------------------------------------------------------
#    urscape_menu - QGIS plugins menu class
##  --------------------------------------------------------

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from .urscape_dialogs import *
from .urscape_library import *
from functools import partial


# ---------------------------------------------
class urscape_menu ():
    def __init__(self, iface):
        self.iface = iface
        self.urscape_menu = None

    def urscape_add_submenu(self, submenu):
        if self.urscape_menu != None:
            self.urscape_menu.addMenu(submenu)
        else:
            self.iface.addPluginToMenu("&URSCAPE", submenu.menuAction())

    def initGui(self):
        # Uncomment the following two lines to have urscape accessible from a top-level menu
        self.urscape_menu = QMenu(QCoreApplication.translate("URSCAPE", "URSCAPE"))
        self.iface.mainWindow().menuBar().insertMenu(self.iface.firstRightStandardMenu().menuAction(), self.urscape_menu)
        
        # Utilities Menu
        self.utilities_menu = QMenu(u'Utilities')
                
        # Create Grid SubMenu
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_grid.png")
        self.urscape_menu.addMenu(self.utilities_menu)	        
        self.creategrid_action = QAction(icon, u'Create Grid', self.iface.mainWindow())
        self.creategrid_action.triggered.connect(self.creategrid)
        self.utilities_menu.addAction(self.creategrid_action)

         # Hub Distance SubMenu
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_hub.png")
        self.urscape_menu.addMenu(self.utilities_menu)	        
        self.hub_action = QAction(icon, u'Hub Distance', self.iface.mainWindow())
        self.hub_action.triggered.connect(self.hub)
        self.utilities_menu.addAction(self.hub_action)

        # Raster Value to Grid
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_raster.png")
        self.urscape_menu.addMenu(self.utilities_menu)	        
        self.raster_action = QAction(icon, u'Raster Value to Grid', self.iface.mainWindow())
        self.raster_action.triggered.connect(self.raster)
        self.utilities_menu.addAction(self.raster_action)

        # Building Area per Grid Cell
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_build.png")
        self.urscape_menu.addMenu(self.utilities_menu)	        
        self.build_action = QAction(icon, u'Building Area per Grid Cell', self.iface.mainWindow())
        self.build_action.triggered.connect(self.build)
        self.utilities_menu.addAction(self.build_action)

        # Population per Grid Cell
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_pop.png")
        self.urscape_menu.addMenu(self.utilities_menu)	        
        self.pop_action = QAction(icon, u'Population per Grid Cell', self.iface.mainWindow())
        self.pop_action.triggered.connect(self.pop)
        self.utilities_menu.addAction(self.pop_action)
              
        
        # QGIS 2 UrScape SubMenu
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_urscape.png")
        self.urscape_menu.addMenu(self.utilities_menu)	        
        self.importer_action = QAction(icon, u'Urscape Importer', self.iface.mainWindow())
        self.importer_action.triggered.connect(self.importer)
        self.utilities_menu.addAction(self.importer_action)

        
        # OpenData_basemap submenu
        self.basemap_menu = QMenu(u'BaseMap')		
        self.urscape_add_submenu(self.basemap_menu)

        ##https://mc.bbbike.org/mc/?num=2&mt0=mapnik&mt1=watercolor
        #https://gitlab.com/GIS-projects/Belgium-XYZ-tiles/tree/b538df2c2de0d16937641742f25e4709ca94e42e
        
        #############
        #Google Maps
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_googlemaps.png")
        self.googlemaps_action = QAction(icon, u'Google Maps', self.iface.mainWindow())
        self.googlemaps_action.triggered.connect(lambda: urscape_basemap('Google Maps'))		
        self.basemap_menu.addAction(self.googlemaps_action)
        
        #Google Satellite
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_googlemaps.png")
        self.googlesatellite_action = QAction(icon, u'Google Satellite', self.iface.mainWindow())
        self.googlesatellite_action.triggered.connect(lambda: urscape_basemap('Google Satellite'))		
        self.basemap_menu.addAction(self.googlesatellite_action)

        #Google Satellite Hybrid
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_googlemaps.png")
        self.urscape_googlesatellitehybrid_action = QAction(icon, u'Google Satellite Hybrid', self.iface.mainWindow())
        self.urscape_googlesatellitehybrid_action.triggered.connect(lambda: urscape_basemap('Google Satellite Hybrid'))		
        self.basemap_menu.addAction(self.urscape_googlesatellitehybrid_action)

                
        #Google Terrain
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_googlemaps.png")
        self.urscape_googleterrain_action = QAction(icon, u'Google Terrain', self.iface.mainWindow())
        self.urscape_googleterrain_action.triggered.connect(lambda: urscape_basemap('Google Terrain'))		
        self.basemap_menu.addAction(self.urscape_googleterrain_action)

        #Google Terrain Hybrid
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_googlemaps.png")
        self.urscape_googleterrainhybrid_action = QAction(icon, u'Google Terrain Hybrid', self.iface.mainWindow())
        self.urscape_googleterrainhybrid_action.triggered.connect(lambda: urscape_basemap('Google Terrain Hybrid'))		
        self.basemap_menu.addAction(self.urscape_googleterrainhybrid_action)

        
        #############
        #Bing Virtual Earth
        #############
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_bing.png")
        self.bingaerial_action = QAction(icon, u'Bing Virtual Earth', self.iface.mainWindow())
        self.bingaerial_action.triggered.connect(lambda: urscape_basemap('Bing Virtual Earth'))	
        self.basemap_menu.addAction(self.bingaerial_action)
 

        #Carto Antique
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_carto.png")
        self.cartoantique_action = QAction(icon, u'Carto Antique', self.iface.mainWindow())
        self.cartoantique_action.triggered.connect(lambda: urscape_basemap('Carto Antique'))		
        self.basemap_menu.addAction(self.cartoantique_action)

        #Carto Dark
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_carto.png")
        self.cartodark_action = QAction(icon, u'Carto Dark', self.iface.mainWindow())
        self.cartodark_action.triggered.connect(lambda: urscape_basemap('Carto Dark'))		
        self.basemap_menu.addAction(self.cartodark_action)

        #Carto Eco
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_carto.png")
        self.cartoeco_action = QAction(icon, u'Carto Eco', self.iface.mainWindow())
        self.cartoeco_action.triggered.connect(lambda: urscape_basemap('Carto Eco'))		
        self.basemap_menu.addAction(self.cartoeco_action)

        #Carto Light
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_carto.png")
        self.cartolight_action = QAction(icon, u'Carto Light', self.iface.mainWindow())
        self.cartolight_action.triggered.connect(lambda: urscape_basemap('Carto Light'))		
        self.basemap_menu.addAction(self.cartolight_action)

        
        #########################		
        # ESRI https://gitlab.com/GIS-projects/Belgium-XYZ-tiles/tree/b538df2c2de0d16937641742f25e4709ca94e42e
        #####################
        #Esri Boundaries and Places 
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_esri.png")
        self.esriboundary_action = QAction(icon, u'Esri Boundaries and Places', self.iface.mainWindow())
        self.esriboundary_action.triggered.connect(lambda: urscape_basemap('Esri Boundaries and Places'))		
        self.basemap_menu.addAction(self.esriboundary_action)

        #Esri Dark Gray 
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_esri.png")
        self.esridarkgray_action = QAction(icon, u'Esri Dark Gray', self.iface.mainWindow())
        self.esridarkgray_action.triggered.connect(lambda: urscape_basemap('Esri Dark Gray'))		
        self.basemap_menu.addAction(self.esridarkgray_action)

        #Esri DeLorme World Base Map
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_esri.png")
        self.esridelorme_action = QAction(icon, u'ESri DeLorme', self.iface.mainWindow())
        self.esridelorme_action.triggered.connect(lambda: urscape_basemap('ESri DeLorme'))		
        self.basemap_menu.addAction(self.esridelorme_action)

        #Esri Imagery 
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_esri.png")
        self.esriimagery_action = QAction(icon, u'Esri Imagery', self.iface.mainWindow())
        self.esriimagery_action.triggered.connect(lambda: urscape_basemap('Esri Imagery'))		
        self.basemap_menu.addAction(self.esriimagery_action)
    
        #Esri Light Gray 
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_esri.png")
        self.esrilightgray_action = QAction(icon, u'Esri Light Gray', self.iface.mainWindow())
        self.esrilightgray_action.triggered.connect(lambda: urscape_basemap('Esri Light Gray'))		
        self.basemap_menu.addAction(self.esrilightgray_action)

        #Esri National Geographic World Map
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_esri.png")
        self.esrinational_action = QAction(icon, u'Esri National Geographic', self.iface.mainWindow())
        self.esrinational_action.triggered.connect(lambda: urscape_basemap('Esri National Geographic'))		
        self.basemap_menu.addAction(self.esrinational_action)

        #Esri Ocean Basemap
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_esri.png")
        self.esriocean_action = QAction(icon, u'Esri Ocean', self.iface.mainWindow())
        self.esriocean_action.triggered.connect(lambda: urscape_basemap('Esri Ocean'))		
        self.basemap_menu.addAction(self.esriocean_action)

        #Esri Physical Map
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_esri.png")
        self.esriphysical_action = QAction(icon, u'Esri Physical', self.iface.mainWindow())
        self.esriphysical_action.triggered.connect(lambda: urscape_basemap('Esri Physical'))		
        self.basemap_menu.addAction(self.esriphysical_action)

        #Esri Shaded Relief
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_esri.png")
        self.esrishaded_action = QAction(icon, u'Esri Shaded Relief', self.iface.mainWindow())
        self.esrishaded_action.triggered.connect(lambda: urscape_basemap('Esri Shaded Relief'))		
        self.basemap_menu.addAction(self.esrishaded_action)

        #Esri Street Map
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_esri.png")
        self.esristreet_action = QAction(icon, u'Esri Street', self.iface.mainWindow())
        self.esristreet_action.triggered.connect(lambda: urscape_basemap('Esri Street'))		
        self.basemap_menu.addAction(self.esristreet_action)

        #Esri Terrain Map
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_esri.png")
        self.esriterrain_action = QAction(icon, u'Esri Terrain', self.iface.mainWindow())
        self.esriterrain_action.triggered.connect(lambda: urscape_basemap('Esri Terrain'))		
        self.basemap_menu.addAction(self.esriterrain_action)
        
        #Esri World Topo Map
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_esri.png")
        self.esritopo_action = QAction(icon, u'Esri Topographic', self.iface.mainWindow())
        self.esritopo_action.triggered.connect(lambda: urscape_basemap('Esri Topographic'))		
        self.basemap_menu.addAction(self.esritopo_action)

        # """ #Esri World Transportation
        # icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_esri.png")
        # self.esritransport_action = QAction(icon, u'Esri Transport', self.iface.mainWindow())
        # self.esritransport_action.triggered.connect(self.esritransport_call)		
        # self.basemap_menu.addAction(self.esritransport_action)
        #  """
        
        ##############################
        # F4map - 2D
        #############################
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_f4map.png")
        self.f4map_action = QAction(icon, u'F4 Map - 2D', self.iface.mainWindow())
        self.f4map_action.triggered.connect(lambda: urscape_basemap('F4 Map - 2D'))		
        self.basemap_menu.addAction(self.f4map_action)

        ##############################
        # Mapbox
        #############################
        # icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_mapbox.png")
        # self.mapbox_action = QAction(icon, u'Mapbox', self.iface.mainWindow())
        # self.mapbox_action.triggered.connect(self.mapbox)		
        # self.basemap_menu.addAction(self.mapbox_action)

        ##############################
        # OpenTopoMap
        #############################
        # """ icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_opentopomap.png")
        # self.opentopomap_action = QAction(icon, u'OpenTopoMap', self.iface.mainWindow())
        # self.opentopomap_action.triggered.connect(self.opentopomap_call)		
        # self.basemap_menu.addAction(self.opentopomap_action) """
        

        
        #Stamen Toner
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_stamen.png")
        self.stamentoner_action = QAction(icon, u'Stamen Toner', self.iface.mainWindow())
        self.stamentoner_action.triggered.connect(lambda: urscape_basemap('Stamen Toner'))		
        self.basemap_menu.addAction(self.stamentoner_action)

        # Stamen Toner Background
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_stamen.png")
        self.stamentonerbkg_action = QAction(icon, u'Stamen Toner Background', self.iface.mainWindow())
        self.stamentonerbkg_action.triggered.connect(lambda: urscape_basemap('Stamen Toner Background'))		
        self.basemap_menu.addAction(self.stamentonerbkg_action)

        # Stamen Toner Hybrid
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_stamen.png")
        self.stamentonerhybrid_action = QAction(icon, u'Stamen Toner Hybrid', self.iface.mainWindow())
        self.stamentonerhybrid_action.triggered.connect(lambda: urscape_basemap('Stamen Toner Hybrid'))		
        self.basemap_menu.addAction(self.stamentonerhybrid_action)

        # Stamen Toner Lite
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_stamen.png")
        self.stamentonerlite_action = QAction(icon, u'Stamen Toner Lite', self.iface.mainWindow())
        self.stamentonerlite_action.triggered.connect(lambda: urscape_basemap('Stamen Toner Lite'))		
        self.basemap_menu.addAction(self.stamentonerlite_action)
        
        # Stamen Terrain
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_stamen.png")
        self.stamenterrain_action = QAction(icon, u'Stamen Terrain', self.iface.mainWindow())
        self.stamenterrain_action.triggered.connect(lambda: urscape_basemap('Stamen Terrain'))		
        self.basemap_menu.addAction(self.stamenterrain_action)

        # Stamen Terrain Background
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_stamen.png")
        self.stamenterrainbkg_action = QAction(icon, u'Stamen Terrain Background', self.iface.mainWindow())
        self.stamenterrainbkg_action.triggered.connect(lambda: urscape_basemap('Stamen Terrain Background'))		
        self.basemap_menu.addAction(self.stamenterrainbkg_action)
        
        # Stamen Watercolor
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_stamen.png")
        self.stamenwatercolor_action = QAction(icon, u'Stamen Watercolor', self.iface.mainWindow())
        self.stamenwatercolor_action.triggered.connect(lambda: urscape_basemap('Stamen Watercolor'))		
        self.basemap_menu.addAction(self.stamenwatercolor_action)
                
        # Wikimedia Maps
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_wikimedia.png")
        self.wikimedia_action = QAction(icon, u'Wikimedia Maps', self.iface.mainWindow())
        self.wikimedia_action.triggered.connect(lambda: urscape_basemap('Wikimedia Maps'))		
        self.basemap_menu.addAction(self.wikimedia_action)
    # """ 
    # 	# Strava Run
    # 	icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_strava.png")
    # 	self.stravarun_action = QAction(icon, u'Strava Run', self.iface.mainWindow())
    # 	self.stravarun_action.triggered.connect(self.stravarun_call)		
    # 	self.basemap_menu.addAction(self.stravarun_action)

    # 	# Strava All
    # 	icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_strava.png")
    # 	self.stravaall_action = QAction(icon, u'Strava All', self.iface.mainWindow())
    # 	self.stravaall_action.triggered.connect(self.stravaall_call)		
    # 	self.basemap_menu.addAction(self.stravaall_action) """	

    # """ # Wikimedia Hike Bike
    # 	icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_wikimedia.png")
    # 	self.wikimediahikebike_action = QAction(icon, u'Wikimedia Hike Bike', self.iface.mainWindow())
    # 	self.wikimediahikebike_action.triggered.connect(self.wikimediahikebike_call)		
    # 	self.basemap_menu.addAction(self.wikimediahikebike_action)
    # 	 """

        #Vietnam OSM Mapss
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_opendata.png")
        self.urscape_osm_action = QAction(icon, u'Vietnam OSM Maps', self.iface.mainWindow())
        self.urscape_osm_action.triggered.connect(lambda: urscape_basemap('Vietnam OSM Maps'))		
        self.basemap_menu.addAction(self.urscape_osm_action)

        #Viet Ban do
        icon = QIcon(os.path.dirname(__file__) + "/icons/urscape_vbd.png")
        self.urscape_vbd_action = QAction(icon, u'Vietbando Maps', self.iface.mainWindow())
        self.urscape_vbd_action.triggered.connect(lambda: urscape_basemap('Vietbando Maps'))	
        self.basemap_menu.addAction(self.urscape_vbd_action)
      
     
    def unload(self):
        if self.urscape_menu != None:
            self.iface.mainWindow().menuBar().removeAction(self.urscape_menu.menuAction())
        else:
            self.iface.removePluginMenu("&urscape", self.create_grid_menu.menuAction())
            self.iface.removePluginMenu("&urscape", self.basemap_menu.menuAction())
        
         
    ##########################	
    def creategrid(self):
        dialog = urscape_creategrid_dialog(self.iface)
        dialog.exec_()

    def hub(self):
        dialog = urscape_hub_dialog(self.iface)
        dialog.exec_()   

    def raster(self):
        dialog = urscape_raster_dialog(self.iface)
        dialog.exec_()   
    
    def build(self):
        dialog = urscape_build_dialog(self.iface)
        dialog.exec_()
    
    def pop(self):
        dialog = urscape_pop_dialog(self.iface)
        dialog.exec_()


    def importer(self):
        dialog = urscape_importer_dialog(self.iface)
        dialog.exec_()    
