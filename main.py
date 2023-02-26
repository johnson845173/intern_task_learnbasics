import pandas as pd

student_df = pd.read_excel("Input_1 - Python Developer Intern - Task 2 - Datasets.xlsx")

final_df = pd.DataFrame(columns = ['Name','Username','Chapter Tag','Test_Name','answered','correct score','skipped','time-taken (seconds)','wrong'])

student_df.rename(columns=lambda x: x.replace(" ",""),inplace=True)

test_names  = [column_headers.split("-")[0].strip() for column_headers in student_df.columns[3:]]

parameters = ['score','time-taken (seconds)','answered','correct','wrong','skipped']

for index,row in student_df.iterrows():
    for test in set(test_names):
        if row[f'{test}-answered'] != "-":
            final_df.loc[len(final_df.index)] = [row['Name'],row['id'],row['ChapterTag'],test,row[f'{test}-answered'],row[f'{test}-score'],row[f'{test}-skipped'],row[f'{test}-time-taken(seconds)'],row[f'{test}-wrong']] 

final_df.to_csv('output.csv')

