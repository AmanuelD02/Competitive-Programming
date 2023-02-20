class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        N  = "Neither"
    
        if ":" in queryIP:
            ipChunked = queryIP.split(":")
            if re.findall("[g-zG-Z]", queryIP) or len(ipChunked) != 8 or any(not(x) or len(x) > 4 for x in ipChunked):
                return "Neither"
            return "IPv6"
        
        else:
            chuncked = queryIP.split(".")
            if len(chuncked) != 4 or any([ not(x.isdigit()) for x in chuncked]) or any(not(x) or (len(x) > 1 and x[0] == '0' ) or int(x) > 255 or int(x) < 0 for x in chuncked):
                return N
            
            return "IPv4"
        