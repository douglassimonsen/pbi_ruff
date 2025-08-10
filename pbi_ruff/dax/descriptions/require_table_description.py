from pbi_core.ssas.model_tables import Table

from pbi_ruff.base_rule import BaseRule, RuleResult


class RequireTableDescription(BaseRule):
    id = "DAX-011"
    name = "Require Table Descriptions"
    description = """
        Tables should have a description.
    """

    @classmethod
    def check(cls, table: Table) -> list[RuleResult]:
        if table.description is not None:
            return []
        return [
            RuleResult(
                rule=cls,
                message=f"A description is required for {table.name}.",
                context_vars={
                    "measure_name": table.name,
                    "measure_id": table.id,
                },
                trace=("measure", table.id),
            ),
        ]
