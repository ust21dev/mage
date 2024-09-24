from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.constants import ActionType, Axis
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action
from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def execute_transformer_action(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Execute Transformer Action: ActionType.AVERAGE
    """
    action = build_transformer_action(
        df,
        action_type=ActionType.AVERAGE,
        action_code='',  # Enter filtering condition on rows before aggregation
        arguments=['Fare', 'Age'],  # Enter the columns to compute aggregate over
        axis=Axis.COLUMN,
        options={'groupby_columns': ['Embarked']},  # Enter columns to group by
        outputs=[
            # The number of outputs below must match the number of arguments
            {'uuid': 'avg_fare_by_embarked_loc', 'column_type': 'number_with_decimals'},
            {'uuid': 'avg_age_by_embarked_loc', 'column_type': 'number_with_decimals'},
        ],
    )

    return BaseAction(action).execute(df)
