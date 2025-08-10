from pbi_core.ssas.model_tables import Column, Measure, Table
from pbi_core.ssas.model_tables.column.enums import ColumnType

from pbi_ruff.base_rule import RuleGroup, RuleResult

from .require_calc_column_description import RequireCalculatedColumnDescription
from .require_column_description import RequireColumnDescription
from .require_measure_description import RequireMeasureDescription
from .require_table_description import RequireTableDescription


class DaxDescriptionRules(RuleGroup):
    """Group of rules related to descriptions on DAX entities."""

    name = "DAX Description Rules"
    rules = (
        RequireColumnDescription,
        RequireCalculatedColumnDescription,
        RequireMeasureDescription,
        RequireTableDescription,
    )

    @classmethod
    def check(cls, dax_element: "Measure | Column | Table") -> list["RuleResult"]:
        """Check the measure for DAX formatting rules."""
        results: list[RuleResult] = []
        column, calc_column, measure, table = (
            [cls.rules[0]],
            [cls.rules[1]],
            [cls.rules[2]],
            [cls.rules[3]],
        )
        if isinstance(dax_element, Column):
            for rule in column:
                results.extend(rule.check(dax_element))
            if dax_element.type == ColumnType.CALCULATED:
                for rule in calc_column:
                    results.extend(rule.check(dax_element))
        elif isinstance(dax_element, Measure):
            for rule in measure:
                results.extend(rule.check(dax_element))
        elif isinstance(dax_element, Table):
            for rule in table:
                results.extend(rule.check(dax_element))
        return results
