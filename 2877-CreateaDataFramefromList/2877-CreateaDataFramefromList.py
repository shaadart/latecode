# Last updated: 26/08/2026, 17:12:28
1import pandas as pd
2
3def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
4    return  pd.DataFrame(student_data, columns = ["student_id", "age"])
5
6    