from django.http import HttpResponse
from django.shortcuts import render
from cwn_fun import lemma_type_to_lemma_ids,lemma_id_to_sense_ids,sense_id_to_sense_def,cwn_id_to_example_cont

def home(request):
    res=[]
    try:
        lemma=request.POST['lemma']
        lemma_ids=lemma_type_to_lemma_ids(lemma_type=lemma)
#       lemma_ids=[lemma_id[0] for lemma_id in lemma_ids]
#        return HttpResponse(' '.join(lemma_ids))
        for lemma_id in lemma_ids:
#           res+=lemma_id#[0]#+sense_id+sense_def
            for sense_id in lemma_id_to_sense_ids(lemma_id):#[0]
                sense_def=sense_id_to_sense_def(sense_id)
                example_cont=cwn_id_to_example_cont(sense_id)
                res.append(' '.join([lemma,lemma_id,sense_def,sense_id,example_cont]))
#               if example_cont:res.append(' '.join([lemma,lemma_id,sense_id,sense_def,example_cont]))
#               else:res.append(' '.join([lemma,lemma_id,sense_id,sense_def]))
        return HttpResponse('<br>'.join(res))
        return HttpResponse(lemma_id+sense_id+sense_def)
    except:
        return render(request,'template.htm',{})
