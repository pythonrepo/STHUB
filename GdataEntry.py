__author__ = 'sin'
import gdata.docs
import gdata.docs.service
import gdata.spreadsheet.service
import gdata.spreadsheet
import sys

class GdataEntry(object):
     def checkEntry(self,password1):
        #credential for gmail login
        username        = 'sakibdroho'
        passwd          = ''
        doc_name      = 'EBL_Account_Info'

        # Connect to Google
        spr_client = gdata.spreadsheet.service.SpreadsheetsService()
        spr_client.email = username
        spr_client.password = passwd
        spr_client.source = 'payne.org-example-1'
        spr_client.ProgrammaticLogin()

        #Document query to get the spreadshit id and worksheet id
        q = gdata.spreadsheet.service.DocumentQuery()

        #Getting the spreadsheet id
        feed = spr_client.GetSpreadsheetsFeed(query=q)
        spreadsheet_id = feed.entry[0].id.text.rsplit('/',1)[1]

        #Getting the worksheet id
        feed = spr_client.GetWorksheetsFeed(spreadsheet_id)
        worksheet_id = feed.entry[0].id.text.rsplit('/',1)[1]

        #Key found in url of particular google doc
        key = '1o_uj31AQpqrypFwWP4D1yOqZuPJF3yjWTYDTxld1Mjs'

        #Making a list that will be passed as colunm header in the google doc
        headers = ['weight','height','sakib','palash','hossain']
        cells = spr_client.GetCellsFeed(spreadsheet_id,worksheet_id)
        size = len(cells.entry)
        print(size)
        for i in range(0,size,1):
            if cells.entry[i].cell.inputValue == password1:
                print("You have entered a correct password",i,size)
                return True
            else:
                if i==size-1:
                    print("Sorry, your password does not match with any entry in the data base",i,size-1)
                    entry1 = spr_client.UpdateCell(row=1,col=size+1,inputValue=password1, key=key,wksht_id=worksheet_id)
                   # entry1 = spr_client.UpdateCell(row=1,col=size+1,inputValue="", key=key,wksht_id=worksheet_id)
                    return False
                else:
                    continue
        if size==0:
             entry1 = spr_client.UpdateCell(row=1,col=1,inputValue=password1, key=key,wksht_id=worksheet_id)


        #entry1 = spr_client.UpdateCell(row=1,col=size+1,inputValue=password1, key=key,wksht_id=worksheet_id)







        '''
        for i, header in enumerate(headers):
            entry = spr_client.UpdateCell(row=1,col=i+1,inputValue=header, key=key,wksht_id=worksheet_id)
            cells = spr_client.GetCellsFeed(spreadsheet_id,worksheet_id)
            if cells.entry[i].cell.inputValue == 'weight':
                print('Welcome to our page')
            else:
                print('Wrong user name')
          '''

#for line in sys.stdin:
    #weight, height = line.strip.split('\t')
    #input_dict={'weight':weight,'height':height}
    #spr_client.InsertRow(input_dict,key)

