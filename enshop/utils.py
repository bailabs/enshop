import frappe


def update_website_context(context):
    context.most_popular_cards = _get_cards('most_popular_cards')
    context.featured_categories_cards = _get_cards('featured_categories_cards')


def _get_cards(parentfield):
    return frappe.get_all(
        "Enshop Settings Card",
        fields=["label", "hyperlink"],
        filters={"parentfield": parentfield}
    )
