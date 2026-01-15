
# pesawat/templatetags/currency_filters.py

from django import template

register = template.Library()

@register.filter(name='rupiah')
def rupiah(value):
    """
    Format angka ke format Rupiah
    Contoh: 1000000 -> Rp 1.000.000
    """
    try:
        value = int(value)
        # Format dengan pemisah ribuan menggunakan titik
        formatted = "{:,}".format(value).replace(',', '.')
        return "Rp {}".format(formatted)
    except (ValueError, TypeError):
        return value

@register.filter(name='idr')
def idr(value):
    """
    Format angka ke format IDR
    Contoh: 1000000 -> IDR 1.000.000
    """
    try:
        value = int(value)
        # Format dengan pemisah ribuan menggunakan titik
        formatted = "{:,}".format(value).replace(',', '.')
        return "IDR {}".format(formatted)
    except (ValueError, TypeError):
        return value
