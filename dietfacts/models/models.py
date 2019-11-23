# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DietFacts_product_template(models.Model):
    _inherit = 'product.template'

    calories = fields.Integer("Calories")
    servingsize = fields.Float('Serving Size')
    lastupdated = fields.Date('Last Updated')
    is_diet = fields.Boolean('is a diet item')

    # nutrient_ids = fields.One2many('product.template.nutrient','product_id','Nutrients')

    @api.onchange('calories')
    def check_calories(self):
        if self.calories < 100:
            self.is_diet = True
        else:
            self.is_diet = False


class DietFacts_res_users_meal(models.Model):
    _name = 'res.users.meal'
    name = fields.Char("Meal Name")
    meal_date = fields.Datetime("Meal Date")
    # item_ids = fields.One2many('res.users.mealitem', 'meal_id')
    user_id = fields.Many2one('res.users', 'Meal User')
    largemeal = fields.Boolean("Large Meal")
