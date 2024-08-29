from django import template

register = template.Library()


@register.filter
def get_trade_names(shortcode):
    TRADES = {
        "Ca": "Carpenter",
        "Pl": "Plumber",
        "El": "Electrician",
        "Pa": "Plasterer",
        "Gw": "Groundsworker",
        "De": "Decorator",
        "Ga": "Gas",
        "AD": "Planner"
    }
    return TRADES.get(shortcode, shortcode)
