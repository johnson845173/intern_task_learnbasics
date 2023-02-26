import pandas as pd
from sqlalchemy import create_engine

# Database credentials
user_name =  "johnson"
password = "tMl2l7rHO6dQcP1xVBlmF2Wv3n0uBIcJ"
host = "dpg-cftdlharrk0c835ilaj0-a.oregon-postgres.render.com"
db= "stock_db_8mph"
port = 7777

student_df = pd.read_excel("Input_2 - Python Developer Intern - Task 2 - Datasets.xlsx")

final_df = pd.DataFrame(columns = ['Name','Username','Chapter Tag','Test_Name','answered','correct score','skipped','time-taken (seconds)','wrong'])

student_df.rename(columns=lambda x: x.replace(" ",""),inplace=True)

test_names  = [column_headers.split("-")[0].strip() for column_headers in student_df.columns[3:]]

parameters = ['score','time-taken (seconds)','answered','correct','wrong','skipped']

for index,row in student_df.iterrows():
    for test in set(test_names):
        if row[f'{test}-answered'] != "-":
            final_df.loc[len(final_df.index)] = [row['Name'],row['id'],row['ChapterTag'],test,row[f'{test}-answered'],row[f'{test}-score'],row[f'{test}-skipped'],row[f'{test}-time-taken(seconds)'],row[f'{test}-wrong']] 

final_df.to_csv('output.csv')

print("Pushing  data")
engine = create_engine(f"postgresql+psycopg2://{user_name}:{password}@{host}:{port}/{db}")
engine.connect()
final_df.to_sql(schema='public',name='student_response', con=engine, if_exists='append',index=False)
print("Data pushed succesfully")



