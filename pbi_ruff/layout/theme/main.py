from pbi_core.static_files.file_classes.theme import Theme

from pbi_ruff.base_rule import RuleGroup, RuleResult

from .theme_colors import ThemeColors, ThemeColorsDeuteranopia, ThemeColorsProtanopia, ThemeColorsTritanopia


class ThemeRules(RuleGroup):
    """Group of rules related to theme colors."""

    name = "Theme Rules"
    rules = (
        ThemeColors,
        ThemeColorsProtanopia,
        ThemeColorsDeuteranopia,
        ThemeColorsTritanopia,
    )

    @classmethod
    def check(cls, theme: dict[str, Theme]) -> list[RuleResult]:
        results: list[RuleResult] = []
        for rule in cls.rules:
            results.extend(rule.check(theme))
        return results
