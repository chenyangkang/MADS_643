import pandas as pd

def merge_files(contact_info_file, other_info_file, output_file):
    contact_info_file = pd.read_csv(contact_info_file)
    other_info_file = pd.read_csv(other_info_file)
    merged = pd.merge(contact_info_file, other_info_file, left_on="respondent_id",\
                    right_on="respondent_id", how="outer")
    merged['birthdate'] = [i.date() for i in pd.to_datetime(merged['birthdate'])]
    merged.to_csv(output_file,index=False)

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("contact_info_file", help = "The respondent_contact.csv file")
    parser.add_argument("other_info_file", help = "The respondent_other.csv file")
    parser.add_argument("output_file", help="Output file path(name)")
    args = parser.parse_args()
    merge_files(args.contact_info_file, args.other_info_file, args.output_file)
    
    

