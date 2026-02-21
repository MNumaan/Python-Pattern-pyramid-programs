def deepcopier(userlist):
    copy_list=[]
    for i in userlist:
        if isinstance(i,list):
            copy_list.append(deepcopier(i*1))
        else: copy_list.append(i*1)
    return copy_list
