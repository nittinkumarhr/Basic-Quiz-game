from django.shortcuts import render
from Quiz_app import filter_data

data1 = []

def data_fill(request):
    template_name = 'home.html'
    template_name2 = 'play.html'
    

    if request.method == 'GET':
        return render(request, template_name)
    elif request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        category = request.POST.get('category')
        difficulty = request.POST.get('difficulty')
        type_data = request.POST.get('type')
        
        data = filter_data.get_data(number, category, difficulty, type_data)
        
        for item in data['results']:
            data1.append(item)
        
        context = {'data': data1}
        return render(request, template_name2, context=context)

def count_data(request):
    template_name = 'score.html'
    
    if request.method == 'GET':
        return render(request, template_name)
    elif request.method == 'POST':
        #=====Ftech the selected answer in dctionary=====
        my_dict = request.POST.dict()
        del my_dict["csrfmiddlewaretoken"]
        my_dict_value=list(my_dict.values())
        w=len(my_dict)
        s=0
        right_ans_data={}
        wrong_ans_data={}
        for data in data1:
            for my_dit in my_dict_value:
                if data['correct_answer'] == my_dit:
                    s+=1
                    print("yes")
                    print(data['question'])
                    right_ans_data[data['question']]=data['correct_answer']
                else:
                    wrong_ans_data[data['question']]=my_dict[data['question']]
                    
        for key in right_ans_data.keys():
            if key in wrong_ans_data:
                if right_ans_data[key] == wrong_ans_data[key]:
                    del wrong_ans_data[key]
        incorrect_answer=w-s
        avberage=float(s/w*100)
        
        print(s,incorrect_answer,avberage)
        context={'total_correct_answer':s,'total_incorrect_answer':incorrect_answer,'right_data':right_ans_data,'Presentage':avberage,'wrong_ans_data':wrong_ans_data}
        
        return render(request, template_name,context=context)


