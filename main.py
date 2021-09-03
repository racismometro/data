import extract
import refine

from data.data_lake import DataLake

if __name__ == "__main__":
    data_lake = DataLake()
    extract.extract(data_lake)
    refine.refine(data_lake)