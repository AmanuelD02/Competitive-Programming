class Solution:
    def subdomainVisits(self, cpdomains):
        domains_count = {}
        
        for domain in cpdomains:
            visit, mainDomain = domain.split(" ")
            visit = int(visit)
            mainDomain_lst = mainDomain.split(".")
            
            for i in range(len(mainDomain_lst)):
                cur_dom = ".".join(mainDomain_lst[i:])
                domains_count[cur_dom]  = visit + domains_count.get(cur_dom, 0)
        
        result = []
        for key, val in domains_count.items():
            result.append("{val} {key}".format(val = val, key = key))
        
        
        return result
        
        
        