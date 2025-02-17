




def rank_test(predict_file,label_file):
    predict_score = {}
    label_score = {}
    f1 = open(predict_file,'r')
    f2 = open(label_file,'r')
    
    for line in f1.readlines():
        line = line.strip().split()
        img_name = line[0]
        img_score = line[1]
        predict_score[img_name] = float(img_score)

    for line in f2.readlines():
        line = line.strip().split()
        img_name = line[0]
        img_score = line[1]
        label_score[img_name] = float(img_score)
    #print('predict: ',predict_score)
    #print('label: ',label_score)

    img_name_list = list(label_score.keys())
    img_name_list.sort()
    
    count = 0
    positive = 0 
    for i in range(len(img_name_list)):
        for j in range(i+1,len(img_name_list)):
            real_rank = 1 if label_score[img_name_list[i]] >= label_score[img_name_list[j]] else -1
            #print('label: ',img_name_list[i],img_name_list[j],real_rank)
            
            predict_rank = 1 if predict_score[img_name_list[i]] >= predict_score[img_name_list[j]] else -1
            
            #print('predict: ',img_name_list[i],predict_score[img_name_list[i]],img_name_list[j],predict_score[img_name_list[j]],predict_rank)
            #print('***************')
            count += 1
            if real_rank == predict_rank:
                positive += 1
    print('%d/%d'%(positive,count))
    accuracy = positive/count
    print('Full Accuracy: %f'%accuracy)
    return accuracy


def rank_pair_test(predict_file,label_file):
    predict_score = {}
    label_score = {}
    f1 = open(predict_file,'r')
    f2 = open(label_file,'r')
    
    for line in f1.readlines():
        line = line.strip().split()
        img_name = line[0]
        img_score = line[1]
        predict_score[img_name] = float(img_score)

    for line in f2.readlines():
        line = line.strip().split()
        img_name = line[0]
        img_score = line[1]
        label_score[img_name] = float(img_score)
    
    keys_list = list(label_score.keys())
    keys_list.sort()
    
    cursor = keys_list[0].split('_')[0]+'_'+keys_list[0].split('_')[1]
    class_num = 0
    for key in keys_list:      
        if cursor == key.split('_')[0]+'_'+key.split('_')[1]:
            class_num += 1
        else:
            break
    count = 0
    positive = 0
    for idx in range(0,len(keys_list),class_num):
        for i in range(idx,idx+class_num):
            for j in range(i+1,idx+class_num):
                #print(idx,i,j)
                
                real_rank = 1 if label_score[keys_list[i]] >= label_score[keys_list[j]] else -1
                #print('label: ',img_name_list[i],img_name_list[j],real_rank)
            
                predict_rank = 1 if predict_score[keys_list[i]] >= predict_score[keys_list[j]] else -1
            
                #print('predict: ',img_name_list[i],predict_score[img_name_list[i]],img_name_list[j],predict_score[img_name_list[j]],predict_rank)
                #print('***************')
                count += 1
                if real_rank == predict_rank:
                    positive += 1
                
    print('%d/%d'%(positive,count))
    accuracy = positive/count
    print('Aligned Pair Accuracy: %f'%accuracy)


    count1 = 0
    count2 = 0
    positive1 = 0
    positive2 = 0

    for idx in range(0,len(keys_list),class_num):

        i = idx
        j = i+1        
        real_rank = 1 if label_score[keys_list[i]] >= label_score[keys_list[j]] else -1
        #print('label: ',img_name_list[i],img_name_list[j],real_rank)
    
        predict_rank = 1 if predict_score[keys_list[i]] >= predict_score[keys_list[j]] else -1
    
        #print('predict: ',img_name_list[i],predict_score[img_name_list[i]],img_name_list[j],predict_score[img_name_list[j]],predict_rank)
        #print('***************')
        count += 1
        if real_rank == 1:
            count1 += 1
            if real_rank == predict_rank:
                positive1 += 1
        if real_rank == -1:
            count2 += 1                
            if real_rank == predict_rank:
                positive2 += 1

    print('%d/%d'%(positive1,count1))
    accuracy_esrganbig1 = positive1/count1
    print('accuracy_esrganbig: %f'%accuracy_esrganbig1)

    print('%d/%d'%(positive2,count2))
    accuracy_srganbig1 = positive2/count2
    print('accuracy_srganbig: %f'%accuracy_srganbig1)
    count1 = 0
    count2 = 0
    positive1 = 0
    positive2 = 0
    for idx in range(0,len(keys_list),class_num):

        i = idx
        j = i+2       
        real_rank = 1 if label_score[keys_list[i]] >= label_score[keys_list[j]] else -1
        #print('label: ',img_name_list[i],img_name_list[j],real_rank)
    
        predict_rank = 1 if predict_score[keys_list[i]] >= predict_score[keys_list[j]] else -1
    
        #print('predict: ',img_name_list[i],predict_score[img_name_list[i]],img_name_list[j],predict_score[img_name_list[j]],predict_rank)
        #print('***************')
        count += 1
        if real_rank == 1:
            count1 += 1
            if real_rank == predict_rank:
                positive1 += 1
        if real_rank == -1:
            count2 += 1                
            if real_rank == predict_rank:
                positive2 += 1

    print('%d/%d'%(positive1,count1))
    accuracy_esrganbig = positive1/count1
    print('accuracy2: %f'%accuracy_esrganbig)

    print('%d/%d'%(positive2,count2))
    accuracy_srganbig = positive2/count2
    print('accuracy2: %f'%accuracy_srganbig)
    
    count1 = 0
    count2 = 0
    positive1 = 0
    positive2 = 0

    for idx in range(0,len(keys_list),class_num):

        i = idx+1
        j = i+1        
        real_rank = 1 if label_score[keys_list[i]] >= label_score[keys_list[j]] else -1
        #print('label: ',img_name_list[i],img_name_list[j],real_rank)
    
        predict_rank = 1 if predict_score[keys_list[i]] >= predict_score[keys_list[j]] else -1
    
        #print('predict: ',img_name_list[i],predict_score[img_name_list[i]],img_name_list[j],predict_score[img_name_list[j]],predict_rank)
        #print('***************')
        count += 1
        if real_rank == 1:
            count1 += 1
            if real_rank == predict_rank:
                positive1 += 1
        if real_rank == -1:
            count2 += 1                
            if real_rank == predict_rank:
                positive2 += 1

    print('%d/%d'%(positive1,count1))
    accuracy_esrganbig = positive1/count1
    print('accuracy3: %f'%accuracy_esrganbig)

    print('%d/%d'%(positive2,count2))
    accuracy_srganbig = positive2/count2
    print('accuracy3: %f'%accuracy_srganbig)


    return accuracy,accuracy_esrganbig1,accuracy_srganbig1



#rank_test('predict_score.txt','label_score.txt')

def regression_test(predict_file,label_file):
    predict_score = {}
    label_score = {}
    f1 = open(predict_file,'r')
    f2 = open(label_file,'r')
    
    for line in f1.readlines():
        line = line.strip().split()
        img_name = line[0]
        img_score = line[1]
        predict_score[img_name] = float(img_score)

    for line in f2.readlines():
        line = line.strip().split()
        img_name = line[0]
        img_score = line[1]
        label_score[img_name] = float(img_score)
    
    keys_list = list(predict_score.keys())
    keys_list.sort()
    
    cursor = keys_list[0].split('_')[0]
    class_num = 0
    for key in keys_list:      
        if cursor == key.split('_')[0]:
            class_num += 1
        else:
            break
    
    count = 0
    positive = 0
    err_sum = 0
    for idx in range(0,len(keys_list),class_num):
        for i in range(idx,idx+class_num):
            #print(idx,i,j)
            err = label_score[keys_list[i]] - predict_score[keys_list[i]]
            err = abs(err)
            err_sum = err_sum+err
            #print('predict: ',img_name_list[i],predict_score[img_name_list[i]],img_name_list[j],predict_score[img_name_list[j]],predict_rank)
            #print('***************')
    err_final = err_sum/len(keys_list)
                
    # print('%d/%d'%(positive,count))
    # accuracy = positive/count
    # print('Aligned Pair Accuracy: %f'%accuracy)
    return err_final


#rank_test('predict_score.txt','label_score.txt')
