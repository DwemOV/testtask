import logging

from odoo import models, fields, api

import uuid

_logger = logging.getLogger(__name__)


class Parcel(models.Model):
    _name = "meestchina.parcel"
    _description = "Посилка Meest China"

    name = fields.Char()
    description = fields.Char()

    # Ідентифікатори
    barcode_meest = fields.Char(string="Штрихкод MeestChina", size=25)
    # barcode_mmpo = fields.Char(string="Штрихкод ММПО", size=25)
    # uuid_wms = fields.Char(
    #     string="UUID WMS",
    #     default=lambda self: str(uuid.uuid4()),
    #     readonly=True
    # )

    # Зв'язки
    # recipient_id = fields.Many2one("meestchina.recipient", string="Отримувач")
    # carrier_id = fields.Many2one("meestchina.carrier", string="Перевізник")
    # project_id = fields.Many2one("meestchina.project", string="Проект")

    # Дати, існують перевизначаю.
    # create_date = fields.Datetime(
    #     string="Створено",
    #     readonly=True,
    #     default=fields.Datetime.now
    # )
    # write_date = fields.Datetime(
    #     string="Оновлено",
    #     readonly=True
    # )
    # planned_arrival_date = fields.Date(string="Планова дата поступлення")
    # received_date = fields.Datetime(string="Дата отримання")
    #
    # # Габарити та кількість
    # length = fields.Float(string="Довжина", digits=(6,2))
    # width = fields.Float(string="Ширина", digits=(6,2))
    # height = fields.Float(string="Висота", digits=(6,2))
    # weight = fields.Float(string="Вага", digits=(6,3))
    # places_qty = fields.Integer(string="Кількість місць")
    #
    # # Логічні
    # paid = fields.Boolean(string="Оплачена", default=False)
    # sendable = fields.Boolean(string="Можна надсилати", default=False)
