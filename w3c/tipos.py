from random import choice

class Elemento(object):
    def get_xml_schema(self):
        pass
    def get_descripcion_textual(self):
        pass

class ElementoTipoSimpleInmediato(Elemento):
    def __init__(self, nombre, tipo):
        self.nombre     =   nombre
        self.tipo       =   tipo
    def get_xml_schema(self):
        plantilla="<xsd:element name={0} type={1}/>"
        return plantilla.format(self.nombre, self.tipo)
    def get_descripcion_textual(self):
        plantilla="Elemento <{0}> es de tipo {1}"
        cadena=plantilla.format(self.nombre, self.tipo.get_tipo_con_prefijo())
        return cadena

class ElementoRestriccionEnTipoNumerico(Elemento):
    def __init__(self, nombre, nombre_tipo_base, nombre_tipo=None):
        self.nombre=nombre
        if nombre_tipo==None:
            self.nombre_tipo="tipo"+self.nombre
        self.minimo=None
        self.maximo=None
        self.nombre_tipo_base=nombre_tipo_base
    def set_minimo(self, minimo):
        self.minimo=minimo
    def set_maximo(self, maximo):
        self.maximo=maximo
    def get_xml_schema(self):
        plantilla="""
        <xsd:simpleType name="{0}">
            <xsd:restriction base="{1}">
            {2}
            </xsd:restriction>
        </xsd:simpleType>
        """
        plantilla_min="<xsd:minInclusive value=\"{0}\"/>\n"
        plantilla_max="<xsd:maxInclusive value=\"{0}\"/>"
        restricciones=""
        if self.minimo!=None:
            restricciones = restricciones +plantilla_min.format(self.minimo)
        if self.maximo!=None:
            restricciones = restricciones +plantilla_max.format(self.maximo)
        cad=plantilla.format(self.nombre_tipo, self.nombre_tipo_base, restricciones)
        return cad
    def get_descripcion_textual(self):
        pass
        

class GeneradorCantidadTotalConTiposSimples(object):
    @staticmethod
    def get():
        nombres_cantidad=["cantidad", "cantidadtotal", "cantidad_en_total",
        "numelementos", "totalcontados", "recuentototal"]
        constructores=[Byte, Short]

        nombre_al_azar      =choice(nombres_cantidad)
        constructor_al_azar =choice(constructores)

        tipo_al_azar=constructor_al_azar()
        
        elemento=ElementoTipoSimpleInmediato(nombre_al_azar, tipo_al_azar)
        return elemento

class TipoW3C(object):
    
    def get_tipo_con_prefijo(self):
        return "xsd:"+self.get_tipo()
    def get_schema(self):
        pass

class Byte(TipoW3C):
    def get_descripcion_textual(self):
        descr="entero de 8 bits"
        return descr
    def get_tipo(self):
        tipo="byte"
        return tipo

class Short(TipoW3C):
    def get_descripcion_textual(self):
        descr="entero de 16 bits"
        return descr
    def get_tipo(self):
        tipo="short"
        return tipo

class Int(TipoW3C):
    def get_descripcion_textual(self):
        descr="entero de 32 bits"
        return descr
    def get_tipo(self):
        tipo="int"
        return tipo

class Long(TipoW3C):
    def get_descripcion_textual(self):
        descr="entero de 64 bits"
        return descr
    def get_tipo(self):
        tipo="long"
        return tipo


class String(TipoW3C):
    def get_descripcion_textual(self):
        descr="cadena de texto"
        return descr
    def get_tipo(self):
        tipo="string"
        return tipo

class TipoRestriccionNumericaMinMax(TipoW3C):
    def __init__(self, tipo_numerico):
        self.tipo_numerico=tipo_numerico