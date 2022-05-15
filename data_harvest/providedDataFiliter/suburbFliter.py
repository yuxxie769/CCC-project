import json


# This program is for rearrange provided data to different suburbs in Melbourne

#read provided data file line by line
def async_kd_tokenizer(filename,grid_data_list):
    results =[]
    with open(filename, encoding='utf-8') as f:
        # Move pointer 
        # Skip the first line. 
        line = f.readline()
        linenum = 1
        while line:
            linenum +=1
            line = f.readline()[:-2]
            try:
                templinedic = json.loads(line)
            except:
                print (linenum)
                print('wrong format, discard')
                continue
            # Only retain tweets that have geo information
            tempGeo = templinedic['doc']['geo']
            if tempGeo != None:
                if tempGeo['type'] == 'Point':
                    # Find out which suburb does the tweet from
                    for index,grid_data in enumerate(grid_data_list):
                        if tempGeo['coordinates'][0]<grid_data[3] and tempGeo['coordinates'][0]>grid_data[1]:
                            if tempGeo['coordinates'][1]<grid_data[2] and tempGeo['coordinates'][1]>grid_data[0]:
                                if index == 0:
                                    suburb = "Melbourne City"
                                    print('find city')
                                elif index == 1:
                                    suburb = "Richmond"
                                else:
                                    suburb = "South Melbourne"
                                #rearrange the tweet data 
                                obj = {
                                    "_id": templinedic['doc']['_id'],
                                    "text": templinedic['doc']['text'],
                                    "created_at": str(templinedic['doc']['created_at']),
                                    "suburb": suburb
                                }
                                results.append(obj)
    print(len(results))
    with open('suburb_dataset.json','w',encoding='utf-8') as j:
            j.write(json.dumps({'docs':results}))


def main(twitter_data, grid_data_list):
    async_kd_tokenizer(twitter_data,grid_data_list)

        

if __name__ == "__main__":
    #Read file and set surburb bboxs 
    twitter_data = 'F:/datafile/twitter-melb.json'
    grid_data_list = [[144.948034,-37.823209,144.979105,-37.805173],
                    [144.988031,-37.830734,145.017128,-37.807817],
                    [144.945889,-37.842597,144.971466,-37.827074]]
    main(twitter_data, grid_data_list)
    # Print root core's execution time
