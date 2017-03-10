# -*- coding=GBK -*-



tag1 = ["��֦׼","P.A.WORKS","2015��7��","ԭ��","key","TV","Charlotte","������","2015","У԰","��ħ��","ԭ������","ҵ������","2015��","PA","�������","������","ǳ���x֮","���","����","��ɽ����","����","��Ц","��������","��}�c��","ǳ����֮","��β","����","����","�v�ڿ���ζ"]
tag2 = ["key","J.C.STAFF","2012��10��","GAL��","key��","����","Busters!","TV","У԰","Little","�ȵû�����л��","�v����","����","������","2012","��Ϸ��","����","��֦׼","��ָ���","ܥ������","�������","����","��Ц","2012��","ɽ������","LB","LittleBusters!","Little_Busters!","2012ʮ�·�"]
#tag1 = ["����", "ʵ��", "����", "����", "���ݳ�չ", "����", "��Ѷ"]
#tag2 = ["����", "�ֳ�", "����", "���ʳ�չ", "����", "�׷�", "��Ѷ", "�ִ�", "����", "����"]


def similar(tag1,tag2):
    taglist = [([0] * (len(tag2))) for i in range(len(tag1))]
    for a in range(len(tag1)):
        taglist[a][0] = a
    for a in range(len(tag2)):
        taglist[0][a] = a
    for i in range(len(tag1)):
        for j in range(len(tag2)):
            if(tag1[i - 1] == tag2[j - 1]):
                temp = 0
            else:
                temp = 1
            taglist[i][j] = min(taglist[i - 1][j - 1] + temp, taglist[i][j - 1] + 1, taglist[i - 1][j] + 1)
    similarity = 1 - taglist[len(tag1)-1][len(tag2)-1] / float(max(len(tag1), len(tag2)))
    return similarity

print similar(tag1,tag2)
