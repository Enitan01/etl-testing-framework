import pandas as pd
from etl.pipeline import run_pipeline


def test_source_to_target_reconciliation():
    # Run the pipeline
    result_df = run_pipeline("data/source_data.csv")

    # Expected output
    target_df = pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
        "age_plus_ten": [35, 40, 45]
    })

    # Reset index for comparison
    result_df = result_df.reset_index(drop=True)
    target_df = target_df.reset_index(drop=True)

    # Compare DataFrames
    pd.testing.assert_frame_equal(result_df, target_df)
