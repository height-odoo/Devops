
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class EventType(models.Model):
    _name = 'event.types'

    name = fields.Char(translate=True)
    code = fields.Char()

class EventGoals(models.Model):
    _name = 'event.goals'

    name = fields.Char(translate=True)
    code = fields.Char()

class EventFeeling(models.Model):
    _name = 'event.feeling'

    name = fields.Char(translate=True)
    code = fields.Char()

class EventMessage(models.Model):
    _name = 'event.message'

    name = fields.Char(translate=True)
    code = fields.Char()

class CRMEVENT(models.Model):
    _inherit = 'crm.lead'

    event_type_ids = fields.Many2many('event.types')
    event_goals_ids = fields.Many2many('event.goals')
    feeling_ids = fields.Many2many('event.feeling')
    event_message_ids = fields.Many2many('event.message')
