"""Reproduce an offline, deterministic CARA numerical differential review.

Uses no market data. The Decimal reference evaluates the supplied finite model
at 80 digits and tests arithmetic only, not whether economic inputs are true.
"""

import argparse
from decimal import Decimal, localcontext
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import random


DEFAULT_SKILL = Path(__file__).resolve().parents[1] / "skill"
SEED = 1871
CASES = 1200
ERROR_THRESHOLD = 1e-10


def decimal_reference(probabilities, wealth, liabilities, gamma):
    """Calculate CARA premium from exact Decimal representations of floats."""
    with localcontext() as context:
        context.prec = 80
        p = list(map(Decimal, probabilities))
        w = list(map(Decimal, wealth))
        loss = list(map(Decimal, liabilities))
        risk_aversion = Decimal(gamma)
        minimum_wealth = min(w)
        lower = min(loss)
        base = [
            prob.ln() - risk_aversion * (cash - minimum_wealth)
            for prob, cash in zip(p, w)
        ]
        numerator = [
            log_weight + risk_aversion * (claim - lower)
            for log_weight, claim in zip(base, loss)
        ]

        def log_sum_exp(values):
            maximum = max(values)
            return maximum + sum((value - maximum).exp() for value in values).ln()

        return float(lower + (log_sum_exp(numerator) - log_sum_exp(base)) / risk_aversion)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-root", type=Path, default=DEFAULT_SKILL)
    parser.add_argument("--source-file", type=Path, help="Optional standalone staging kernel")
    args = parser.parse_args()
    source = args.source_file or args.skill_root / "scripts" / "edge_mechanics.py"
    spec = importlib.util.spec_from_file_location("reviewed_edge_mechanics", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    random.seed(SEED)
    violations = []
    maximum_error = 0.0
    for case_number in range(CASES):
        count = random.randrange(2, 7)
        raw = [10 ** random.uniform(-12, 0) for _ in range(count)]
        probabilities = [weight / sum(raw) for weight in raw]
        scale = 10 ** random.uniform(-6, 12)
        wealth = [random.uniform(-1, 1) * scale for _ in probabilities]
        liabilities = [random.uniform(-1, 1) * scale for _ in probabilities]
        gamma = 10 ** random.uniform(-18, 1)
        actual = module.seller_reservation_premium(probabilities, wealth, liabilities, gamma)
        expected = decimal_reference(probabilities, wealth, liabilities, gamma)
        error = abs(actual - expected) / max(1, abs(expected))
        maximum_error = max(maximum_error, error)
        if error > ERROR_THRESHOLD:
            violations.append({
                "case": case_number, "error": error, "actual": actual,
                "expected": expected, "probabilities": probabilities,
                "wealth": wealth, "liabilities": liabilities, "gamma": gamma,
            })

    boundary_cases = []
    for amount in (1e6, 1e8, 1e12, 1e16):
        actual = module.seller_reservation_premium([.5, .5], [0, amount], [0, amount], 1)
        # Both states have W-L=0. Baseline E[exp(-W)]=(1+exp(-amount))/2.
        expected = math.log(2) - math.log1p(math.exp(-amount))
        boundary_cases.append({
            "wealth_and_liability_amount": amount,
            "actual": actual, "expected": expected,
            "absolute_error": abs(actual - expected),
        })

    print(json.dumps({
        "source": str(source),
        "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "seed": SEED,
        "cases": CASES,
        "decimal_precision": 80,
        "error_metric": "abs(actual-expected)/max(1,abs(expected))",
        "threshold": ERROR_THRESHOLD,
        "maximum_random_case_error": maximum_error,
        "random_case_violations": violations,
        "correlated_boundary_cases": boundary_cases,
    }, indent=2))
    return bool(violations) or any(
        case["absolute_error"] > ERROR_THRESHOLD for case in boundary_cases
    )


if __name__ == "__main__":
    raise SystemExit(main())
