from pbi_core.static_files.layout.visual_container import VisualContainer

from pbi_ruff.base_rule import BaseRule, RuleResult


class RequireAltText(BaseRule):
    id = "VIZ-002"
    name = "Require Alt Text for Visuals"
    description = "Alt text should be defined for visuals to ensure accessibility for users with visual impairments."

    @classmethod
    def check(cls, visual: VisualContainer) -> list[RuleResult]:
        # If there's no query, it's a static visual, so no alt text is required.
        if visual.query is None:
            return []

        if visual.config.singleVisual is None:
            return []
        sv = visual.config.singleVisual
        if sv.vcObjects is None or sv.vcObjects.general is None or sv.vcObjects.general[0].properties.altText is None:
            return [
                RuleResult(
                    rule=cls,
                    message=f"Alt text is required for visual {visual.name()}.",
                    context_vars={
                        "visual_name": visual.name(),
                        "visual_id": visual.id,
                    },
                    trace=("visual", visual.pbi_core_id()),
                ),
            ]
        return []
