# Last updated: 26/08/2026, 17:15:42
1import pandas as pd
2
3def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
4    return employees.head(3)
5    