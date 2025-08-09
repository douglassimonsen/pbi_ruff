from pbi_core.static_files.layout.visual_container import VisualContainer

from pbi_ruff.base_rule import RuleGroup, RuleResult

from .implicit_measures import DiscourageImplicitMeasures


class VisualRules(RuleGroup):
    """Group of rules related to visuals."""

    name = "Visual Rules"
    rules = (DiscourageImplicitMeasures,)

    @classmethod
    def check(cls, visual: VisualContainer) -> list[RuleResult]:
        results: list[RuleResult] = []
        for rule in cls.rules:
            results.extend(rule.check(visual))
        return results
