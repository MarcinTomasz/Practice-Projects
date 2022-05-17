#Script that downloads a youtube channel's API and analyzes its statistics.

from googleapiclient.discovery import build
import pandas as pd
from IPython.display import JSON

api_key = 'AIzaSyB1dXmejt8gwuzHrGdRQ5bzk1MEDAm3XQI'

channel_ids = ['UCF31eojFKhWQJviyMICWO2w'
                #more channels here 
              ]
               
api_service_name = "youtube"
api_version = "v3"
#client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

#Get credentials and create an API client
youtube = build(
    api_service_name, api_version, developerKey=api_key)    

def get_channel_stats(youtube, channel_ids):
    all_data= []
    
    request= youtube.channels().list(
        part= 'snippet, contentDetails, statistics',
        id= 'UCF31eojFKhWQJviyMICWO2w'
    )
    response= request.execute()
    
    #loop through items
    for item in response['items']:
        data = {'channelName': item['snippet']['title'], 
                'subscribers': item['statistics']['subscriberCount'],
                'views': item['statistics']['viewCount'],
                'totalVideos': item['statistics']['videoCount'],
                'playlistId': item['contentDetails']['relatedPlaylists']['uploads'],
                 }
        
        all_data.append(data)
        
    return(pd.DataFrame(all_data))

request = youtube.channels().list(
    part="snippet, contentDetails, statistics",
    #id=','.join(channel_ids)
    id='UCF31eojFKhWQJviyMICWO2w'
    )

response = request.execute()

JSON(response)

channel_stats= get_channel_stats(youtube, channel_ids)
print(channel_stats)
