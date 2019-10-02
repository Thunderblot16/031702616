import re
import json

def CreatProvince():#创建省份列表
    list=[]
    list.append("北京")#0
    list.append("上海")#1
    list.append("天津")#2
    list.append("重庆")#3
    list.append("西藏自治区")#4
    list.append("新疆维吾尔族自治区")#5
    list.append("广西壮族自治区")#6
    list.append("宁夏回族自治区")#7
    list.append("内蒙古自治区")#8    
    list.append("河北")#9
    list.append("河南")#10
    list.append("山东")#11
    list.append("山西")#12
    list.append("江苏")#13
    list.append("安徽")#14
    list.append("陕西")#15
    list.append("甘肃")#16
    list.append("青海")#17
    list.append("湖北")#18
    list.append("湖南")#19
    list.append("浙江")#20
    list.append("江西")#21
    list.append("福建")#22
    list.append("贵州")#23
    list.append("四川")#24
    list.append("广东")#25
    list.append("云南")#26
    list.append("海南")#27
    list.append("黑龙江")#28
    list.append("吉林")#29
    list.append("辽宁")#30
    return list

def CreatCity():#创建市列表
    allCityList=[]
    allCityList.append(["北京"])#0
    allCityList.append(["上海"])#1
    allCityList.append(["天津"])#2
    allCityList.append(["重庆"])#3
    allCityList.append(["拉萨","昌都地区","山南地区","阿里地区","那曲地区","林芝地区","日喀则地区"])#4
    allCityList.append(["乌鲁木齐", "阿勒泰", "阿克苏", "昌吉", "哈密", "和田", "喀什", "克拉玛依", "石河子", "塔城", "库尔勒", "吐鲁番", "伊宁"])#5
    allCityList.append(["南宁", "桂林", "阳朔", "柳州", "梧州", "玉林", "桂平", "贺州", "钦州", "贵港", "防城港", "百色", "北海", "河池", "来宾", "崇左"])#6
    allCityList.append(["银川", "固原", "中卫", "石嘴山", "吴忠"])#7
    allCityList.append(["呼和浩特", "呼伦贝尔", "锡林浩特", "包头", "赤峰", "海拉尔", "乌海", "鄂尔多斯", "通辽"])#8   
    allCityList.append(["石家庄", "唐山", "张家口", "廊坊", "邢台", "邯郸", "沧州", "衡水", "承德", "保定", "秦皇岛"])#9
    allCityList.append(["郑州", "开封", "洛阳", "平顶山", "焦作", "鹤壁", "新乡", "安阳", "濮阳", "许昌", "漯河", "三门峡", "南阳", "商丘", "信阳", "周口", "驻马店"])#10
    allCityList.append(["济南", "青岛", "淄博", "威海", "曲阜", "临沂", "烟台", "枣庄", "聊城", "济宁", "菏泽", "泰安", "日照", "东营", "德州", "滨州", "莱芜", "潍坊"])#11
    allCityList.append(["太原", "阳泉", "晋城", "晋中", "临汾", "运城", "长治", "朔州", "忻州", "大同", "吕梁"])#12
    allCityList.append(["南京", "苏州", "昆山", "南通", "太仓", "吴县", "徐州", "宜兴", "镇江", "淮安", "常熟", "盐城", "泰州", "无锡", "连云港", "扬州", "常州", "宿迁"])#13
    allCityList.append(["合肥", "巢湖", "蚌埠", "安庆", "六安", "滁州", "马鞍山", "阜阳", "宣城", "铜陵", "淮北", "芜湖", "毫州", "宿州", "淮南", "池州"])#14
    allCityList.append(["西安", "韩城", "安康", "汉中", "宝鸡", "咸阳", "榆林", "渭南", "商洛", "铜川", "延安"])#15
    allCityList.append(["兰州", "白银", "庆阳", "酒泉", "天水", "武威", "张掖", "甘南", "临夏", "平凉", "定西", "金昌"])#16
    allCityList.append(["西宁", "海北", "海西", "黄南", "果洛", "玉树", "海东", "海南"])#17
    allCityList.append(["武汉", "宜昌", "黄冈", "恩施", "荆州", "神农架", "十堰", "咸宁", "襄樊", "孝感", "随州", "黄石", "荆门", "鄂州"])#18
    allCityList.append(["长沙", "邵阳", "常德", "郴州", "吉首", "株洲", "娄底", "湘潭", "益阳", "永州", "岳阳", "衡阳", "怀化", "韶山", "张家界"])#19
    allCityList.append(["杭州", "湖州", "金华", "宁波", "丽水", "绍兴", "雁荡山", "衢州", "嘉兴", "台州", "舟山", "温州"])#20
    allCityList.append(["南昌", "萍乡", "九江", "上饶", "抚州", "吉安", "鹰潭", "宜春", "新余", "景德镇", "赣州"])#21
    allCityList.append(["福州", "厦门", "龙岩", "南平", "宁德", "莆田", "泉州", "三明", "漳州"])#22
    allCityList.append(["贵阳", "安顺", "赤水", "遵义", "铜仁", "六盘水", "毕节", "凯里", "都匀"])#23
    allCityList.append(["成都", "泸州", "内江", "凉山", "阿坝", "巴中", "广元", "乐山", "绵阳", "德阳", "攀枝花", "雅安", "宜宾", "自贡", "甘孜州", "达州", "资阳", "广安", "遂宁", "眉山", "南充"] )#24
    allCityList.append(["广州", "深圳", "潮州", "韶关", "湛江", "惠州", "清远", "东莞", "江门", "茂名", "肇庆", "汕尾", "河源", "揭阳", "梅州", "中山", "德庆", "阳江", "云浮", "珠海", "汕头", "佛山"])#25
    allCityList.append(["昆明", "保山", "楚雄", "德宏", "红河", "临沧", "怒江", "曲靖", "思茅", "文山", "玉溪", "昭通", "丽江", "大理"])#26
    allCityList.append(["海口", "三亚", "儋州", "琼山", "通什", "文昌"])#27
    allCityList.append(["哈尔滨", "齐齐哈尔", "牡丹江", "大庆", "伊春", "双鸭山", "鹤岗", "鸡西", "佳木斯", "七台河", "黑河", "绥化", "大兴安岭"])#28
    allCityList.append(["长春", "延边", "吉林", "白山", "白城", "四平", "松原", "辽源", "大安", "通化"])#29
    allCityList.append(["沈阳", "大连", "葫芦岛", "旅顺", "本溪", "抚顺", "铁岭", "辽阳", "营口", "阜新", "朝阳", "锦州", "丹东", "鞍山"])#30
    return allCityList

#将电话号码提取出来
def GetPhoneNumber(str):    
    num=re.findall("\d{11}",str)#文件中连续11位数字的必是电话号码
    return num

#把名字提取出来
def GetName(str):
    name=re.findall("!(\D*.*?),",str) 
    return name

#把地址（乱序）提取出来
def GetAddress(str):
    address=re.sub(r'\d{11}',"",str) #先把电话号码删掉
    address=re.findall("\D*.*?,(.*?)\.",address) #从文件中提取出地址
    address=("".join(address))
    return(Restore(address,GetDifficulty(str)))

#把提取出来的人名、电话号码、地址合并起来存在一个新的数组里
def Merge(str):
    sum=[]
    num=GetPhoneNumber(str)
    name=GetName(str)
    address=GetAddress(str)
    sum.append("".join(name))
    sum.append("".join(num))
    sum.append(address)
    return sum

#提取难度级别
def GetDifficulty(str):
    d=re.findall("(\d)!.",str) #把!前面的难度系数提取出来
    d=("".join(d))
    return d

#恢复地址顺序
def Restore(address,d):
    pro=CreatProvince()
    city=CreatCity()
    S=0
    #匹配省份
    for i in range(len(pro)):
        a=re.match(pro[i],address)
        if(a):
            S=i
            one=a.group()
            address=re.sub(one,"",address,1) #匹配到后把省份名字去掉
            if i<4:      #当匹配到的是直辖市的时候
                two=one+'市'
                if re.match(r'市',address):
                    address=re.sub(r'市',"",address,1)  #把“市”字去掉
            if 8<i<31:  #当匹配到的是普通省份的时候
                one+="省"
                if re.match(r'省',address):
                    address=re.sub(r'省',"",address,1) #把“省”字去掉                
            break

    #匹配市级   
    if S>3:
        if one!="": #即省份不缺失时
            for i in range(len(city[S])):
                a=re.match(city[S][i],address) 
                if a==None:#匹配不到时
                    two=""
                else:
                    two=a.group()
                    address=re.sub(two,"",address,1) #匹配到后把市级的名字去掉
                    two+="市"
                    if re.match(r'市',address):
                        address=re.sub(r'市',"",address)  #把“市”字去掉
                    break
    #匹配县级
    a=re.match(r'.*?(县|区|市)',address) #匹配县/区/县级市
    if a==None:
        three=""
    else:
        three=a.group()
        address=re.sub(three,"",address,1)
    #匹配乡镇级
    a=re.match(r'.*?(街道|镇|乡)',address)
    if a==None:
        four=""
    else:
        four=a.group()
        address=re.sub(four,"",address,1)

    #按照难度系数分离地址
    if d=='1':
        five=address
        sum=[]
        sum.append(one)
        sum.append(two)
        sum.append(three)
        sum.append(four)
        sum.append(five)
    else:
        #匹配路名
        a=re.match(r'.*?(路|街|巷)',address)
        if a==None:
            five=""
        else:
            five=a.group()
            address=re.sub(five,"",address,1)
        #匹配门牌号
        a=re.match(r'.*?号',address)
        if a==None:
            six=""
        else:
            six=a.group()
            address=re.sub(six,"",address,1)
        #匹配详细地址
        seven=address
        #将分级后的地址存入数组中
        sum=[]
        sum.append(one)
        sum.append(two)
        sum.append(three)
        sum.append(four)
        sum.append(five)
        sum.append(six)
        sum.append(seven)
    return sum



#main
str=input()
sum=Merge(str)
list=["姓名","手机","地址"]
book={}
for j in range(len(list)):
    book[list[j]]=sum[j]
Json=json.dumps(book,ensure_ascii=False)
print(Json)
