from pbi_core.ssas.model_tables import Column

from pbi_ruff.base_rule import BaseRule, RuleResult


class RequireCalculatedColumnDescription(BaseRule):
    id = "DAX-008"
    name = "Require Calculated Column Descriptions"
    description = """
        Calculated columns should have a description.
    """

    @classmethod
    def check(cls, column: Column) -> list[RuleResult]:
        if column.description is not None:
            return []
        return [
            RuleResult(
                rule=cls,
                message=f"A description is required for {column.full_name()}.",
                context_vars={
                    "column_name": column.full_name(),
                    "column_id": column.id,
                },
                trace=("column", column.id),
            ),
        ]
