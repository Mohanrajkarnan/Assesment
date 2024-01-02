import requests
import gzip
import shutil
import pandas as pd
from pathlib import Path


folderPath = 'https://www1.ncdc.noaa.gov/pub/data/gsod/'


yearDf = pd.read_html(folderPath)
yearLst = yearDf[0].Name.tolist()
for year in yearLst:
    if str(year).endswith("/"):
        Path(f"./Assesment/Input/{year}/").mkdir(parents=True, exist_ok=True)
        downloadFile = pd.read_html(f"{folderPath}{year}")
        fileLst = downloadFile[0].Name.tolist()
        for zipFile in fileLst:
            print(f"******{zipFile}****{year}**")
            if str(zipFile).endswith(".gz"):
                r = requests.get(f'{folderPath}{year}/{zipFile}',verify=False)
                loadZip = f"./Assesment/Input/{year}/{zipFile}"
                open(loadZip, 'wb').write(r.content)
                with gzip.open(loadZip, 'rb') as file_in:
                    unzipFileName = zipFile[:-3]
                    with open(f'./Assesment/Input/{year}/{unzipFileName}.csv', 'wb') as file_out:
                        shutil.copyfileobj(file_in, file_out)
                        break
                
        




# r = requests.get('https://www1.ncdc.noaa.gov/pub/data/gsod/1929',verify=False)
# open('check.csv', 'wb').write(r.content)




# r = requests.get('https://www1.ncdc.noaa.gov/pub/data/gsod/1929/030050-99999-1929.op.gz',verify=False)
# open('check.gz', 'wb').write(r.content)

# path = "C:/Users/Mohanraj.Karnan/Downloads/030050-99999-1929.op.gz"
# path = "C:\\Users\\Mohanraj.Karnan\\.vscode\\TestWorplace\\check.gz"

# with gzip.open(path, 'rb') as file_in:
#     with open('set.csv', 'wb') as file_out:
#         shutil.copyfileobj(file_in, file_out)
#         print('example.json file created')



