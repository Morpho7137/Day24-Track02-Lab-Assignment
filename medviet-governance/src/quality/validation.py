import pandas as pd
import great_expectations as gx
import great_expectations.expectations as gxe
from great_expectations.core.expectation_suite import ExpectationSuite


def build_patient_expectation_suite() -> ExpectationSuite:
    """Create an expectation suite for patient data quality validation."""
    context = gx.get_context()
    suite = ExpectationSuite(name="patient_data_suite")
    valid_conditions = ["Tiểu đường", "Huyết áp cao", "Tim mạch", "Khỏe mạnh"]

    suite.add_expectation(gxe.ExpectColumnValuesToNotBeNull(column="patient_id"))
    suite.add_expectation(gxe.ExpectColumnValueLengthsToEqual(column="cccd", value=12))
    suite.add_expectation(
        gxe.ExpectColumnValuesToBeBetween(
            column="ket_qua_xet_nghiem",
            min_value=0,
            max_value=50,
        )
    )
    suite.add_expectation(
        gxe.ExpectColumnValuesToBeInSet(column="benh", value_set=valid_conditions)
    )
    suite.add_expectation(
        gxe.ExpectColumnValuesToMatchRegex(
            column="email",
            regex=r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
        )
    )
    suite.add_expectation(gxe.ExpectColumnValuesToBeUnique(column="patient_id"))
    context.suites.add_or_update(suite)
    return suite


def validate_anonymized_data(filepath: str) -> dict:
    """Validate anonymized data and return a compact status report."""
    df = pd.read_csv(filepath)
    original_df = pd.read_csv("data/raw/patients_raw.csv")
    suite = build_patient_expectation_suite()

    context = gx.get_context()
    datasource_name = "patient_validation_source"
    try:
        datasource = context.data_sources.get(datasource_name)
    except Exception:
        datasource = context.data_sources.add_pandas(name=datasource_name)

    batch = datasource.read_dataframe(df, asset_name="patient_validation_asset")
    suite_validation = batch.validate(suite)

    results = {
        "success": True,
        "failed_checks": [],
        "stats": {
            "total_rows": len(df),
            "columns": list(df.columns),
            "gx_success": bool(suite_validation.success),
        },
    }

    if not suite_validation.success:
        results["success"] = False
        for item in suite_validation.results:
            if not item.success:
                results["failed_checks"].append(item.expectation_config.type)

    if df["cccd"].astype(str).str.fullmatch(r"\d{12}").any():
        results["success"] = False
        results["failed_checks"].append("cccd_still_plain_12_digits")

    required_columns = ["patient_id", "ho_ten", "cccd", "so_dien_thoai", "email"]
    if df[required_columns].isnull().any().any():
        results["success"] = False
        results["failed_checks"].append("null_values_in_required_columns")

    if len(df) != len(original_df):
        results["success"] = False
        results["failed_checks"].append("row_count_mismatch")

    results["failed_checks"] = list(dict.fromkeys(results["failed_checks"]))
    return results
