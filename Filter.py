from df2tables import render_inline, render
from pandas import read_csv


def main():
    data = read_csv("automated_payment_test_results.csv")

    output_str = render_inline(
        df=data,
        buttons=['copy', 'csv', 'excel', 'pdf'],
        render_opts={
            "load_column_control": True,
            "reorder": True,
            "add_expand_btn": True,
        },
        js_opts={
            "scrollY": 500, "paging": False,
            "fixedHeader": True,
            "order": {"idx": 1, "dir": "desc"},
        },
    )

    render(
        df=data,
        to_file="Test_Results.html",
        title="Test Results",
        buttons=['copy', 'csv', 'excel', 'pdf'],
        render_opts={
            "load_column_control": True,
            "reorder": True,
            "add_expand_btn": True,
        },
        js_opts={
            "scrollY": 500, "paging": False,
            "fixedHeader": True,
            "order": {"idx": 1, "dir": "desc"},
        },
    )

    return output_str


if __name__ == "__main__":
    main()