import pandas as pd
import glob
import os

from datetime import date

class Datahelper:
    """
    The class helps ontologically annotating input data files and creating metadata.
    """

    def __init__(self):

        self.oedatamodel_col_list = [
            "id",
            "region",
            "year",
            "timeindex_resolution",
            "timeindex_start",
            "timeindex_stop",
            "bandwidth_type",
            "version",
            "method",
            "source",
            "comment",
        ]
        self.json_col_list = [
            "bandwidth_type",
            "version",
            "method",
            "source",
            "comment",
        ]

        # define paths for csv and oeo_annotation folder
        self.csv_dir = os.path.join(os.getcwd(), "data", "input")
        self.oeo_annotation_path = os.path.join(os.getcwd(), "data", "oeo_annotation")

        os.makedirs(self.oeo_annotation_path, exist_ok=True)

        self.df_dict = self.prepare_df_dict(directory=self.csv_dir)