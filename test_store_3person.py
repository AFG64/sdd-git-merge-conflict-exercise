"""Tests for store.py — suite for 3-person groups (Features A, B, and C).

Each pricing rule is opt-in via its own argument (apply_discount,
apply_tax, apply_shipping), so these tests are independent of each other.
As each teammate's feature lands, its test starts passing and stays
passing; merging someone else's feature never breaks a test that was
already green.

- test_no_feature_yet always passes: no flags means no rules apply.
- test_discount_feature_alone passes once Feature A is implemented.
- test_tax_feature_alone passes once Feature B is implemented.
- test_shipping_feature_alone passes once Feature C is implemented.
- test_all_features_combined passes once all three features are merged and
  the conflict resolved so the rules apply in order A, then B, then C.
"""

from store import calculate_total


def test_no_feature_yet():
    assert calculate_total(100.0) == 100.0


def test_discount_feature_alone():
    # Feature A: 10% discount on carts over $50
    assert calculate_total(100.0, apply_discount=True) == 90.0


def test_tax_feature_alone():
    # Feature B: 8% sales tax on every order
    assert calculate_total(100.0, apply_tax=True) == 108.0


def test_shipping_feature_alone():
    # Feature C: flat $5 shipping fee
    assert calculate_total(100.0, apply_shipping=True) == 105.0


def test_all_features_combined():
    # Discount, then tax, then shipping:
    #   100 -> 90 (10% discount) -> 97.2 (8% tax) -> 102.2 (flat $5 shipping)
    result = calculate_total(
        100.0, apply_discount=True, apply_tax=True, apply_shipping=True
    )
    assert result == 102.2, (
        f"Expected 102.2, got {result}. "
        "Did you combine the features in the right order? See the README."
    )
