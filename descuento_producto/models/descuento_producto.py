# descuento_producto/models/descuento_producto.py
from odoo import models, fields, api

class DescuentoProducto(models.Model):
    _name = 'descuento.producto'
    _description = 'Descuento de Producto'

    name = fields.Selection([
        ('cliente_premium', 'Cliente Premium'),
        ('cliente_vip', 'Cliente VIP'),
        ('cliente_estandar', 'Cliente Estándar'),
    ], string="Tipo de Descuento", required=True)

    producto = fields.Many2one('product.product', string="Producto", required=True, store=True)
    cliente = fields.Many2one('res.partner', string="Cliente", required=True, store=True)
    precio_venta = fields.Float(string="Precio de Venta", related="producto.list_price", readonly=True)
    descuento = fields.Float(string="Descuento (%)", required=True)
    precio_final = fields.Float(string="Precio Final", compute="_compute_precio_final", store=True)
    observaciones = fields.Text(string="Observaciones del Descuento")

    @api.depends('precio_venta', 'descuento')
    def _compute_precio_final(self):
        for record in self:
            record.precio_final = record.precio_venta * (1 - record.descuento / 100)
