from crudbuilder.abstract import BaseCrudBuilder
from crudbuilder.formset import BaseInlineFormset
from NavieraSkyApp.models import Contenedor, Cliente, Motorista, Producto, Salida, Ingreso


class SalidaInlineFormSet(BaseInlineFormset):
    inline_model = Salida
    parent_model = Contenedor
    fk_name = None


class IngresoInlineFormSet(BaseInlineFormset):
    inline_model = Ingreso
    parent_model = Contenedor
    fk_name = None


class ContenedorCrud(BaseCrudBuilder):
    model = Contenedor
    search_fields = ['codigo']
    tables2_fields = ('codigo', 'bahia')
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20
    login_required = True
    custom_postfix_url = 'Contenedores'


class ContenedorSalidaCrud(BaseCrudBuilder):
    model = Contenedor
    search_fields = ['codigo']
    tables2_fields = ('codigo', 'bahia')
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20
    inlineformset = SalidaInlineFormSet
    login_required = True
    custom_postfix_url = 'Salidas'


class ContenedorEntradaCrud(BaseCrudBuilder):
    model = Contenedor
    search_fields = ['codigo']
    tables2_fields = ('codigo', 'bahia')
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20
    inlineformset = IngresoInlineFormSet
    login_required = True
    custom_postfix_url = 'Ingresos'


class ClienteCrud(BaseCrudBuilder):
    model = Cliente
    search_fields = ['nombres', 'apellidos']
    tables2_fields = ('nombres', 'apellidos', 'pais')
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20
    login_required = True


class MotoristaCrud(BaseCrudBuilder):
    model = Motorista
    search_fields = ['nombres', 'apellidos']
    tables2_fields = ('nombres', 'apellidos', 'pais')
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20
    login_required = True


class ProductoCrud(BaseCrudBuilder):
    model = Producto
    search_fields = ['nombre', 'codigo']
    tables2_fields = ('existencia', 'nombre', 'codigo')
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20
    login_required = True
