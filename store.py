"""Simple checkout calculator for an online store.

TODO(team): implement the pricing rule(s) assigned to you in the README.
"""


def calculate_total(
    subtotal, apply_discount=False, apply_tax=False, apply_shipping=False
):
    """Calculate the final total a customer pays for their cart."""
    total = subtotal

    # TODO: Add an 8% sales tax to every order.
    # its argument (apply_discount, apply_tax, or apply_shipping)

    if apply_discount:
        if total > 50:
            total = total - (total*10/100)
            

    if apply_tax:
        total = total + (8/100)*total

    return total


if __name__ == "__main__":
    example_subtotal = 100.0
    print(
        f"Total for a ${example_subtotal:.2f} cart: ${calculate_total(example_subtotal):.2f}"
    )
    print(
        f"Total for a ${example_subtotal:.2f} cart with discount: ${calculate_total(example_subtotal, True, False):.2f}"
    )
    print(
        f"Total for a ${example_subtotal:.2f} cart with tax: ${calculate_total(example_subtotal, False, True):.2f}"
    )
    print(
        f"Total for a ${example_subtotal:.2f} cart with discount and tax: ${calculate_total(example_subtotal, True, True):.2f}"
    )
