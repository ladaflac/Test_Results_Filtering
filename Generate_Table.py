from df2tables import render_inline, render
from pandas import read_csv


def main():
    data = read_csv("automated_payment_test_results.csv")

    # Genrates a string with <table> element
    output_str = render_inline(
        df=data,
        buttons=['copy', 'csv', 'excel', 'pdf', 'colvis'],
        render_opts={
            "reorder": True,
            "add_expand_btn": False,
        },
        js_opts={
            "scrollY": 500,
            "paging": False,
            "fixedHeader": True,
            "order": {"idx": 0, "dir": "desc"},
        },
    )

    # Generates a full html and saves it to a file - see Test_Results_sample.html
    # output_html = render(
    #     df=data,
    #     to_file="Test_Results_sample.html",
    #     title="Test Results",
    #     buttons=['copy', 'csv', 'excel', 'pdf', 'colvis'],
    #     render_opts={
    #         "reorder": True,
    #         "add_expand_btn": False,
    #     },
    #     js_opts={
    #         "scrollY": 500,
    #         "paging": False,
    #         "fixedHeader": True,
    #         "order": {"idx": 0, "dir": "desc"},
    #     },
    # )

    return output_str


if __name__ == "__main__":
    main()