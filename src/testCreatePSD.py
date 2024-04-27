import pandas as pd
from orcasound_noise.pipeline.pipeline import NoiseAnalysisPipeline
from orcasound_noise.utils import Hydrophone
import datetime as dt

def main():
    if __name__ == '__main__':
        pipeline = NoiseAnalysisPipeline(Hydrophone.ORCASOUND_LAB,
                                     delta_f=1, bands=None,
                                     delta_t=60, mode='safe')
        psd_path, broadband_path = pipeline.generate_parquet_file(dt.datetime(2023, 3, 22, 12),
                                                                  dt.datetime(2023, 3, 22, 13),
                                                                  upload_to_s3=False)
