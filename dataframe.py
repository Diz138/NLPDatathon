import pandas as pd
import logging as logger
df = pd.read_json("publications_text_100.json")
logger.debug(df)

print(df)