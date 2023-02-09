class Solution:
    def reformatDate(self, date: str) -> str:
        month_map = {"Jan" : "01", "Feb" : "02", "Mar" : "03",
                     "Apr" : "04", "May" : "05", "Jun" : "06", 
                     "Jul" : "07", "Aug" : "08", "Sep" : "09",
                     "Oct" : "10", "Nov" : "11", "Dec" : "12",
                    }
        
        date = date.split(" ")
        day = date[-3][:-2].zfill(2)
        output = [date[-1] , month_map[date[-2]] , day]
        
        return "-".join(output)