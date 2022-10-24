def counting_pages(total_page_num, input_page_info):
    pages = [0 for _ in range(total_page_num + 1)]
    
    page_info_list = input_page_info.split(",")
    
    for page_info in page_info_list:
        info = page_info.split("-")
        
        if len(info) == 1 or len(set(info)) == 1:
            if int(info[0]) < len(pages):
                pages[int(info[0])] = 1
        else:
            min_page, max_page = map(int, info)
            
            if (min_page > max_page) or (min_page > total_page_num):
                continue
            else:
                for page in range(min_page, max_page+1):
                    if page < len(pages):
                        pages[page] = 1
                    
    return sum(pages)



while True:
    total_page = int(input())
    
    if total_page == 0:
        break
        
    input_page_info = input()
    
    print(counting_pages(total_page, input_page_info))
