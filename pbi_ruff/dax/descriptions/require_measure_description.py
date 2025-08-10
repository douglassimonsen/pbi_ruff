from pbi_core.ssas.model_tables import Measure

from pbi_ruff.base_rule import BaseRule, RuleResult


class RequireMeasureDescription(BaseRule):
    id = "DAX-010"
    name = "Require Measure Descriptions"
    description = """
        Measures should have a description.
    """

    @classmethod
    def check(cls, measure: Measure) -> list[RuleResult]:
        if measure.description is not None:
            return []
        return [
            RuleResult(
                rule=cls,
                message=f"A description is required for {measure.full_name()}.",
                context_vars={
                    "measure_name": measure.full_name(),
                    "measure_id": measure.id,
                },
                trace=("measure", measure.id),
            ),
        ]
