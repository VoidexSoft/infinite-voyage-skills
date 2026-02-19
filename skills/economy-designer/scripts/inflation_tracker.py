#!/usr/bin/env python3
"""
Economy Inflation Tracker - Monitors and analyses inflation in game economies.

Accepts economy simulation data (JSON) tracking currency supply over time,
calculates inflation rate, money velocity, and purchasing power index.
Detects inflation/deflation trends via moving averages and flags dangerous
thresholds.  Outputs a JSON health report with actionable recommendations.
"""

import argparse
import json
import math
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime
from dataclasses import dataclass, asdict, field


# ---------------------------------------------------------------------------
# Thresholds & defaults
# ---------------------------------------------------------------------------

DEFAULT_INFLATION_THRESHOLD = 5.0    # percent per period
DEFAULT_DEFLATION_THRESHOLD = -10.0  # percent per period
DEFAULT_MOVING_AVG_WINDOW = 5        # periods


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class PeriodSnapshot:
    """Single-period economy snapshot."""
    period: int
    currency_supply: float
    transaction_volume: float
    price_index: float
    inflation_rate: float
    money_velocity: float
    purchasing_power: float


@dataclass
class TrendAlert:
    """Alert raised when a metric crosses a dangerous threshold."""
    period: int
    metric: str
    value: float
    threshold: float
    severity: str   # 'warning', 'critical'
    message: str


@dataclass
class HealthReport:
    """Full economy health report."""
    generated_at: str
    periods_analysed: int
    snapshots: List[PeriodSnapshot]
    alerts: List[TrendAlert]
    summary: Dict[str, Any]
    trend_analysis: Dict[str, Any]
    recommendations: List[str]


# ---------------------------------------------------------------------------
# Core calculations
# ---------------------------------------------------------------------------

def calculate_inflation_rate(
    prev_supply: float,
    curr_supply: float,
) -> float:
    """
    Calculate period-over-period inflation rate as a percentage.

    Args:
        prev_supply: Currency supply in the previous period.
        curr_supply: Currency supply in the current period.

    Returns:
        Inflation rate as a percentage (positive = inflation, negative = deflation).
    """
    if prev_supply <= 0:
        return 0.0
    return ((curr_supply - prev_supply) / prev_supply) * 100.0


def calculate_money_velocity(
    transaction_volume: float,
    currency_supply: float,
) -> float:
    """
    Calculate money velocity (V = T / M).

    Args:
        transaction_volume: Total value of transactions in the period.
        currency_supply: Total currency supply in the period.

    Returns:
        Money velocity ratio.
    """
    if currency_supply <= 0:
        return 0.0
    return transaction_volume / currency_supply


def calculate_purchasing_power(
    base_price_index: float,
    current_price_index: float,
) -> float:
    """
    Calculate purchasing power index relative to the base period.

    A value of 1.0 means purchasing power is unchanged; lower values indicate
    that currency buys less.

    Args:
        base_price_index: Price index at period 0.
        current_price_index: Price index at the current period.

    Returns:
        Purchasing power index (1.0 = baseline).
    """
    if current_price_index <= 0:
        return 0.0
    return base_price_index / current_price_index


def moving_average(values: List[float], window: int) -> List[Optional[float]]:
    """
    Compute a simple moving average over *values*.

    Args:
        values: Input data series.
        window: Number of periods in the moving average window.

    Returns:
        List of the same length as *values*.  Entries where the window is not
        yet full are ``None``.
    """
    result: List[Optional[float]] = []
    for i in range(len(values)):
        if i < window - 1:
            result.append(None)
        else:
            window_slice = values[i - window + 1: i + 1]
            result.append(sum(window_slice) / len(window_slice))
    return result


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_economy_data(data_path: Path) -> List[Dict[str, Any]]:
    """
    Load economy data from a JSON file.

    Expected format::

        [
            {
                "period": 0,
                "currency_supply": 100000,
                "transaction_volume": 50000,
                "price_index": 100.0
            },
            ...
        ]

    ``transaction_volume`` and ``price_index`` are optional; sensible defaults
    are derived from ``currency_supply`` if absent.

    Args:
        data_path: Path to the JSON data file.

    Returns:
        List of period dictionaries.

    Raises:
        ValueError: If the file cannot be parsed or is empty.
    """
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if not isinstance(data, list) or len(data) == 0:
        raise ValueError(
            "Economy data must be a non-empty JSON array of period objects."
        )

    return data


def generate_sample_data(periods: int) -> List[Dict[str, Any]]:
    """
    Generate synthetic economy data for demonstration/testing.

    Simulates gradual supply growth with periodic shocks.

    Args:
        periods: Number of periods to generate.

    Returns:
        List of period dictionaries.
    """
    data: List[Dict[str, Any]] = []
    supply = 100_000.0
    price_index = 100.0

    for p in range(periods):
        # Gradual growth with occasional spikes
        growth_rate = 0.02  # 2% base growth per period
        if p > 0 and p % 10 == 0:
            growth_rate = 0.08  # 8% spike every 10 periods

        supply *= (1 + growth_rate)
        price_index *= (1 + growth_rate * 0.6)  # prices lag behind supply
        transaction_volume = supply * 0.45       # ~45% velocity

        data.append({
            'period': p,
            'currency_supply': round(supply, 2),
            'transaction_volume': round(transaction_volume, 2),
            'price_index': round(price_index, 2),
        })

    return data


# ---------------------------------------------------------------------------
# Analysis engine
# ---------------------------------------------------------------------------

def analyse_economy(
    raw_data: List[Dict[str, Any]],
    inflation_threshold: float = DEFAULT_INFLATION_THRESHOLD,
    deflation_threshold: float = DEFAULT_DEFLATION_THRESHOLD,
    ma_window: int = DEFAULT_MOVING_AVG_WINDOW,
) -> HealthReport:
    """
    Run full inflation analysis on the supplied economy data.

    Args:
        raw_data: List of period snapshots (see ``load_economy_data``).
        inflation_threshold: Inflation percentage that triggers a warning.
        deflation_threshold: Deflation percentage (negative) that triggers a warning.
        ma_window: Moving average window size.

    Returns:
        A populated HealthReport.
    """
    # --- Build snapshots ------------------------------------------------- #
    snapshots: List[PeriodSnapshot] = []
    inflation_rates: List[float] = []
    alerts: List[TrendAlert] = []

    base_price_index = raw_data[0].get('price_index', 100.0)

    for i, entry in enumerate(raw_data):
        period = entry.get('period', i)
        supply = entry.get('currency_supply', 0.0)
        volume = entry.get('transaction_volume', supply * 0.5)
        price_idx = entry.get('price_index', 100.0)

        # Inflation rate (period-over-period)
        if i == 0:
            rate = 0.0
        else:
            prev_supply = raw_data[i - 1].get('currency_supply', supply)
            rate = calculate_inflation_rate(prev_supply, supply)

        velocity = calculate_money_velocity(volume, supply)
        purchasing = calculate_purchasing_power(base_price_index, price_idx)

        inflation_rates.append(rate)

        snapshots.append(PeriodSnapshot(
            period=period,
            currency_supply=round(supply, 2),
            transaction_volume=round(volume, 2),
            price_index=round(price_idx, 4),
            inflation_rate=round(rate, 4),
            money_velocity=round(velocity, 4),
            purchasing_power=round(purchasing, 4),
        ))

    # --- Moving averages ------------------------------------------------- #
    ma_inflation = moving_average(inflation_rates, ma_window)

    # --- Threshold alerts ------------------------------------------------ #
    for i, snap in enumerate(snapshots):
        # Per-period inflation alert
        if snap.inflation_rate > inflation_threshold:
            severity = 'critical' if snap.inflation_rate > inflation_threshold * 2 else 'warning'
            alerts.append(TrendAlert(
                period=snap.period,
                metric='inflation_rate',
                value=round(snap.inflation_rate, 4),
                threshold=inflation_threshold,
                severity=severity,
                message=(
                    f"Period {snap.period}: inflation rate "
                    f"{snap.inflation_rate:.2f}% exceeds "
                    f"{inflation_threshold}% threshold"
                ),
            ))

        # Per-period deflation alert
        if snap.inflation_rate < deflation_threshold:
            severity = 'critical' if snap.inflation_rate < deflation_threshold * 2 else 'warning'
            alerts.append(TrendAlert(
                period=snap.period,
                metric='deflation_rate',
                value=round(snap.inflation_rate, 4),
                threshold=deflation_threshold,
                severity=severity,
                message=(
                    f"Period {snap.period}: deflation rate "
                    f"{snap.inflation_rate:.2f}% below "
                    f"{deflation_threshold}% threshold"
                ),
            ))

        # Moving-average trend alert (sustained inflation)
        ma_val = ma_inflation[i]
        if ma_val is not None and ma_val > inflation_threshold:
            alerts.append(TrendAlert(
                period=snap.period,
                metric='ma_inflation',
                value=round(ma_val, 4),
                threshold=inflation_threshold,
                severity='warning',
                message=(
                    f"Period {snap.period}: {ma_window}-period moving average "
                    f"inflation {ma_val:.2f}% exceeds {inflation_threshold}% "
                    f"(sustained inflation trend)"
                ),
            ))

        # Low purchasing power alert
        if snap.purchasing_power < 0.5:
            alerts.append(TrendAlert(
                period=snap.period,
                metric='purchasing_power',
                value=round(snap.purchasing_power, 4),
                threshold=0.5,
                severity='critical',
                message=(
                    f"Period {snap.period}: purchasing power "
                    f"{snap.purchasing_power:.2f} has dropped below 50% of baseline"
                ),
            ))

    # --- Summary statistics ---------------------------------------------- #
    all_rates = [s.inflation_rate for s in snapshots[1:]]  # skip period 0
    avg_inflation = sum(all_rates) / len(all_rates) if all_rates else 0.0
    max_inflation = max(all_rates) if all_rates else 0.0
    min_inflation = min(all_rates) if all_rates else 0.0

    first_snap = snapshots[0]
    last_snap = snapshots[-1]
    total_supply_change = (
        (last_snap.currency_supply - first_snap.currency_supply)
        / first_snap.currency_supply * 100
    ) if first_snap.currency_supply > 0 else 0.0

    avg_velocity = (
        sum(s.money_velocity for s in snapshots) / len(snapshots)
    ) if snapshots else 0.0

    summary = {
        'total_periods': len(snapshots),
        'initial_supply': first_snap.currency_supply,
        'final_supply': last_snap.currency_supply,
        'total_supply_change_pct': round(total_supply_change, 2),
        'average_inflation_rate': round(avg_inflation, 4),
        'max_inflation_rate': round(max_inflation, 4),
        'min_inflation_rate': round(min_inflation, 4),
        'average_money_velocity': round(avg_velocity, 4),
        'final_purchasing_power': last_snap.purchasing_power,
        'total_alerts': len(alerts),
        'critical_alerts': sum(1 for a in alerts if a.severity == 'critical'),
        'warning_alerts': sum(1 for a in alerts if a.severity == 'warning'),
    }

    # --- Trend analysis -------------------------------------------------- #
    # Classify the overall trend using the last N moving-average values
    recent_ma = [v for v in ma_inflation[-ma_window:] if v is not None]
    if len(recent_ma) >= 2:
        trend_direction = recent_ma[-1] - recent_ma[0]
        if trend_direction > 0.5:
            trend_label = 'accelerating_inflation'
        elif trend_direction < -0.5:
            trend_label = 'decelerating_inflation'
        else:
            trend_label = 'stable'
    elif recent_ma:
        trend_label = 'insufficient_data'
    else:
        trend_label = 'no_data'

    overall_health = 'healthy'
    if summary['critical_alerts'] > 0:
        overall_health = 'critical'
    elif summary['warning_alerts'] > 0:
        overall_health = 'at_risk'
    elif abs(avg_inflation) > inflation_threshold * 0.5:
        overall_health = 'watch'

    trend_analysis = {
        'trend_direction': trend_label,
        'overall_health': overall_health,
        'ma_window': ma_window,
        'latest_ma_inflation': round(recent_ma[-1], 4) if recent_ma else None,
    }

    # --- Recommendations ------------------------------------------------- #
    recommendations = _generate_recommendations(
        summary, trend_analysis, inflation_threshold, deflation_threshold,
    )

    return HealthReport(
        generated_at=datetime.now().isoformat(),
        periods_analysed=len(snapshots),
        snapshots=snapshots,
        alerts=alerts,
        summary=summary,
        trend_analysis=trend_analysis,
        recommendations=recommendations,
    )


def _generate_recommendations(
    summary: Dict[str, Any],
    trend: Dict[str, Any],
    inflation_threshold: float,
    deflation_threshold: float,
) -> List[str]:
    """
    Produce plain-language recommendations based on the analysis results.

    Args:
        summary: Summary statistics dict.
        trend: Trend analysis dict.
        inflation_threshold: Configured inflation threshold.
        deflation_threshold: Configured deflation threshold.

    Returns:
        List of recommendation strings.
    """
    recs: List[str] = []

    avg = summary.get('average_inflation_rate', 0.0)
    health = trend.get('overall_health', 'unknown')
    direction = trend.get('trend_direction', 'unknown')

    # High inflation
    if avg > inflation_threshold:
        recs.append(
            f"Average inflation ({avg:.2f}%) exceeds threshold "
            f"({inflation_threshold}%). Add stronger currency sinks "
            f"(repair costs, taxes, cosmetic shops) to remove excess supply."
        )

    if direction == 'accelerating_inflation':
        recs.append(
            "Inflation is accelerating. Consider introducing limited-time "
            "currency sinks or reducing faucet output before the next period."
        )

    # High deflation
    if avg < deflation_threshold:
        recs.append(
            f"Average deflation ({avg:.2f}%) is below threshold "
            f"({deflation_threshold}%). Increase currency faucets "
            f"(quest rewards, daily bonuses) to stimulate the economy."
        )

    # Low purchasing power
    pp = summary.get('final_purchasing_power', 1.0)
    if pp < 0.5:
        recs.append(
            f"Purchasing power has dropped to {pp:.2f} (baseline 1.0). "
            f"Players may feel currency is worthless. Consider a price "
            f"rebalance or introducing a new currency tier."
        )

    # Velocity concerns
    vel = summary.get('average_money_velocity', 0.0)
    if vel < 0.2:
        recs.append(
            f"Money velocity is low ({vel:.2f}). Currency is being hoarded. "
            f"Introduce compelling spending opportunities or time-limited "
            f"offers to encourage circulation."
        )
    elif vel > 2.0:
        recs.append(
            f"Money velocity is very high ({vel:.2f}). Currency may be "
            f"changing hands too fast, signalling instability. Review "
            f"automated trading or exploit vectors."
        )

    # Healthy economy
    if health == 'healthy' and not recs:
        recs.append(
            "Economy appears healthy. Continue monitoring supply growth and "
            "ensure faucets and sinks remain balanced as new content is added."
        )

    return recs


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def render_report_json(report: HealthReport) -> str:
    """
    Serialise the health report to a JSON string.

    Args:
        report: The computed HealthReport.

    Returns:
        Pretty-printed JSON.
    """
    data = asdict(report)
    return json.dumps(data, indent=2, default=str)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Economy inflation tracker - analyse game economy health'
    )
    parser.add_argument(
        '--data',
        type=Path,
        default=None,
        help=(
            'Path to economy data JSON file. Each entry must have at least '
            '"period" and "currency_supply". If omitted, generates sample data.'
        ),
    )
    parser.add_argument(
        '--periods',
        type=int,
        default=50,
        help='Number of periods to generate when using sample data (default: 50)',
    )
    parser.add_argument(
        '--threshold',
        type=float,
        default=DEFAULT_INFLATION_THRESHOLD,
        help=f'Inflation warning threshold in percent (default: {DEFAULT_INFLATION_THRESHOLD})',
    )
    parser.add_argument(
        '--deflation-threshold',
        type=float,
        default=DEFAULT_DEFLATION_THRESHOLD,
        help=f'Deflation warning threshold in percent (default: {DEFAULT_DEFLATION_THRESHOLD})',
    )
    parser.add_argument(
        '--window',
        type=int,
        default=DEFAULT_MOVING_AVG_WINDOW,
        help=f'Moving average window size (default: {DEFAULT_MOVING_AVG_WINDOW})',
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=None,
        help='Output file path for JSON report (default: stdout)',
    )

    args = parser.parse_args()

    # Load or generate data
    if args.data:
        print(f"Loading economy data from {args.data}...")
        raw_data = load_economy_data(args.data)
        print(f"  Loaded {len(raw_data)} period(s)")
    else:
        print(f"No data file provided. Generating {args.periods} sample periods...")
        raw_data = generate_sample_data(args.periods)
        print(f"  Generated {len(raw_data)} period(s)")

    # Run analysis
    print("Analysing economy...")
    report = analyse_economy(
        raw_data,
        inflation_threshold=args.threshold,
        deflation_threshold=args.deflation_threshold,
        ma_window=args.window,
    )

    # Serialise
    output_json = render_report_json(report)

    # Write or print
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output_json)
        print(f"\nReport saved to {args.output}")
    else:
        print("")
        print(output_json)

    # Console summary
    s = report.summary
    t = report.trend_analysis
    print(f"\n{'='*60}")
    print("ECONOMY HEALTH SUMMARY")
    print(f"{'='*60}")
    print(f"  Periods analysed:       {s['total_periods']}")
    print(f"  Supply change:          {s['total_supply_change_pct']:+.2f}%")
    print(f"  Avg inflation rate:     {s['average_inflation_rate']:+.4f}% per period")
    print(f"  Max inflation rate:     {s['max_inflation_rate']:+.4f}%")
    print(f"  Min inflation rate:     {s['min_inflation_rate']:+.4f}%")
    print(f"  Avg money velocity:     {s['average_money_velocity']:.4f}")
    print(f"  Final purchasing power: {s['final_purchasing_power']:.4f}")
    print(f"  Overall health:         {t['overall_health']}")
    print(f"  Trend direction:        {t['trend_direction']}")
    print(f"  Alerts:                 {s['total_alerts']} "
          f"({s['critical_alerts']} critical, {s['warning_alerts']} warning)")

    if report.recommendations:
        print(f"\nRecommendations:")
        for i, rec in enumerate(report.recommendations, 1):
            print(f"  {i}. {rec}")


if __name__ == '__main__':
    main()
