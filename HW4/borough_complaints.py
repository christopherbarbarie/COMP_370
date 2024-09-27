import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', help='Name of the input file')
parser.add_argument('-s', help='Start date')
parser.add_argument('-e', help='End date')
parser.add_argument('-o', help='Name of the output file')
args = parser.parse_args()

def parse_date(date_str):
    for fmt in ('%m/%d/%Y %I:%M:%S %p', '%m/%d/%Y'):
        try:
            return pd.to_datetime(date_str, format=fmt)
        except ValueError:
            continue
    raise ValueError(f"Date format for {date_str} not recognized")

start_date = parse_date(args.s)
end_date = parse_date(args.e)

chunksize = 1000 
chunks = []

for chunk in pd.read_csv(args.i, chunksize=chunksize, usecols=[2, 3, 6, 17]):
    chunk.columns = ['start date', 'end date', 'complaint type', 'borough']
    chunk['start date'] = pd.to_datetime(chunk['start date'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')
    chunk['end date'] = pd.to_datetime(chunk['end date'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')
    
    filtered_chunk = chunk[(chunk['start date'] >= start_date) & (chunk['start date'] <= end_date)]
    chunks.append(filtered_chunk)

if chunks:
    data = pd.concat(chunks)
    complaint_counts = data.groupby(['complaint type', 'borough']).size().reset_index(name='count')

    if args.o:
        complaint_counts.to_csv(args.o, index=False)
    else:
        print(complaint_counts)