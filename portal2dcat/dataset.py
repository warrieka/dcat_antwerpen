from datetime import datetime
from rdflib import Graph, BNode, URIRef,  Literal
from rdflib.namespace import RDF, FOAF, Namespace, NamespaceManager
from ns import ns, namespaces, dcat, dc
from config import CONTACT, HOME_URL 
from utils import obj2dateLiteral

class dataset:
    def __init__(self, subject=None, graph=None):
        "subject must be URIREF, if graph is given data wil be append to graph"
        self.s = URIRef( subject ) if subject is not None else BNode() #subject
        
        if graph is None:
            self.gx = Graph( namespace_manager = ns(namespaces).nsManager() )   
        else:
            self.gx = graph
        self.gx.add( (self.s, RDF.type, dcat.Dataset ) ) #subject predicate object
        #add agend
        self.gx.add( (URIRef(HOME_URL), RDF.type, FOAF.Agent ) )
        
    def dc_title(self, title="" ):
        self.title = Literal( title )
        self.gx.add( (self.s, dc.title, self.title ) )
        
    def dc_description(self, description="" ): 
        self.description = Literal( description )
        self.gx.add( (self.s, dc.description, self.description ) )
           
    def dc_identifier(self, identifier="" ):
        self.identifier = Literal( identifier ) if identifier else BNode()
        self.gx.add( (self.s, dc.identifier, self.identifier ) )
          
    def dc_issued (self, issued=None ):
        if issued is None: 
           issued = datetime.now()
        else: 
           issued = obj2dateLiteral( issued )
        self.issued = Literal( issued )
        self.gx.add( (self.s, dc.issued, self.issued ) )
        
    def dc_modified(self, modified=None):
        if modified is None: 
           modified = datetime.now()
        else: 
           modified = obj2dateLiteral( modified )
        self.modified = Literal( modified )
        self.gx.add( (self.s, dc.modified, self.modified ) )
      
    def dcat_contactPoint(self, contactPoint=CONTACT ):
        self.contactPoint = URIRef( contactPoint )
        self.gx.add( (self.s, dcat.contactPoint, self.contactPoint ) )
      
    def dcat_landingPage(self, landingPage=""):
        self.landingPage = URIRef( landingPage )
        self.gx.add( (self.s, dcat.landingPage, self.landingPage ) )
        
    def dc_publisher(self, publisher=HOME_URL):
        self.publisher = URIRef( publisher )
        self.gx.add( (self.s, dc.publisher, self.publisher ) )
        
    def dc_language(self, language="http://lexvo.org/id/iso639-3/nld"): 
        self.language = URIRef( language )
        self.gx.add( (self.s, dc.language, self.language ) )
        
    def dcat_distribution(self, distribution=[]):    
        self.distribution = []
        for dist in distribution:
            self.distribution.append( URIRef( dist ) )
            self.gx.add( (self.s, dcat.distribution, URIRef(dist) ) )
    
    def asText(self):
        return self.gx.serialize(format='n3')