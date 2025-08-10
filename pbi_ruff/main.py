from pbi_core import LocalReport

from .base_rule import RuleResult
from .dax import DaxFormattingRules, DaxPerformanceRules
from .dax.descriptions.main import DaxDescriptionRules
from .layout import LayoutRules, SectionRules, ThemeRules, VisualRules


def check_rules(report: LocalReport) -> list[RuleResult]:
    """Run all rules on the report."""
    # Run theme colors rule
    results: list[RuleResult] = []

    # Layout rules
    results.extend(LayoutRules.check(report.static_files.layout))

    for section in report.static_files.layout.sections:
        results.extend(SectionRules.check(section))
        for visual in section.visualContainers:
            results.extend(VisualRules.check(visual))

    # Other static files rules
    if False:
        results.extend(ThemeRules.check(report.static_files.themes))

    # SSAS rules

    for measure in report.ssas.measures:
        results.extend(DaxFormattingRules.check(measure))
        results.extend(DaxPerformanceRules.check(measure))
        results.extend(DaxDescriptionRules.check(measure))

    for table in report.ssas.tables:
        results.extend(DaxDescriptionRules.check(table))

    for column in report.ssas.columns:
        results.extend(DaxDescriptionRules.check(column))
    return results
