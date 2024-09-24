import numpy as np
import pandas as pd
import argparse as ap
import sys
import os

parser = ap.ArgumentParser(description='Count complaints by borough')
parser.add_argument('-i', help='Name of the input file', required=True)
parser.add_argument('-s', help='Start date for filtering', required=True)
parser.add_argument('-e', help='End date for filtering', required=True)
parser.add_argument('-o',help='Name of the output file')
args = parser.parse_args()

