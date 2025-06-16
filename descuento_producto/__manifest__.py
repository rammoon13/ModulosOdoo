# desceunto_producto/__manifest__.py
{
    'name': 'Descuento de Producto',
    'version': '1.0',
    'summary': 'Modulo para gestionar descuentos en productos para clientes especificos',
    'category': 'Sales',
    'author': 'Ramon Herrera Robles',
    'website': 'https://tuweb.com',
    'depends': ['product', 'sale'],
    'icon': '/descuento_producto/static/description/prueba51.png',
    'data': [
        'security/ir.model.access.csv',
        'views/descuento_producto_views.xml',
    ],
    'application': True,
    'installable': True,
}
