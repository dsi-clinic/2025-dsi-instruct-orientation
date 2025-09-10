"""Pipeline example"""

from utils.preprocess_util_lib_example import save_random_dataframe

if __name__ == "__main__":
    # This is an example of running the code as a pipeline
    # Rather than through a notebook
    output_file = "sample_output.csv"

    save_random_dataframe(
        output_file,
    )
