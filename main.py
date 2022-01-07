import re

listItems = []
titleList = []
unratedTitleList = []
ratingList = []
unratedRatingList = []
linkList = []
newLinkList = []
unratedLinkList = []
liList = []
finalTitleList = []
finalLinkList = []
finalRatingList = []
unratedFinalTitleList = []
unratedFinalLinkList = []
unratedFinalRatingList = []

liRE = "<li>.+<\/li>"
linkRE = "href=\".+\"\\s" 
titleRE = "noreferrer\">(.+)<\/a>"
ratingRE = "\(rated with (\d{1,2})"

#^.+\(rated.+\)$

with open('alist.txt', encoding='utf-8') as f:
    listItems = f.readlines()


for item in listItems:
    liList.append(re.findall(liRE, item))

for li in liList:
    if li:
        linkList.append(re.findall(linkRE, str(li)))
        titleList.append(re.findall(titleRE, str(li)))
        ratingList.append(re.findall(ratingRE, str(li)))


#Creates the linkList
for link in linkList:
    link = link[0].strip()
    link = link.split("href=\"")[1]
    newLinkList.append(link)

#Filter by rating
for i, rating in enumerate(ratingList):
    strBeginning = f"{titleList[i][0]} - {newLinkList[i]} - "
    if rating:
        finalTitleList.append(titleList[i])
        finalLinkList.append(newLinkList[i])
        finalRatingList.append(ratingList[i])
        strFinal = strBeginning + ratingList[i][0]
    else:
        unratedFinalTitleList.append(titleList[i])
        unratedFinalLinkList.append(newLinkList[i])
        unratedFinalRatingList.append(ratingList[i])
        strFinal = strBeginning + "unrated"     

with open("ratedTitleList.txt", "a", encoding="utf-8") as f:
    for title in finalTitleList:
        f.write(f"{title[0]} \n")

with open("ratedLinkList.txt", "a", encoding="utf-8") as f:
    for element in finalLinkList:
        element = element.split("\"")
        f.write(f"{element[0]} \n")

with open("ratedRatingList.txt", "a", encoding="utf-8") as f:
    for element in finalRatingList:
        f.write(f"{element[0]} \n")

with open("unratedTitleList.txt", "a", encoding="utf-8") as f:
    for title in unratedFinalTitleList:
        f.write(f"{title[0]} \n")

with open("unratedLinkList.txt", "a", encoding="utf-8") as f:
    for element in unratedFinalLinkList:
        element = element.split("\"")
        f.write(f"{element[0]} \n")

with open("unratedRatingList.txt", "a", encoding="utf-8") as f:
    for element in unratedFinalRatingList:
        f.write(f"unrated \n")



    
    
    






