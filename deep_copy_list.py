def deepcopier(userlist):
    copy_list=[]
    for i in range(len(userlist)):
        if isinstance(userlist[i],list):
            copy_list.append(deepcopier(userlist[i]*1))
        else: copy_list.append(userlist[i]*1)
    return copy_list
