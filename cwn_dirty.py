from sqlite3 import connect

conn=connect('cwn_dirty.sqlite')
cursor=conn.cursor()

def lemma_type_to_lemma_ids(lemma_type='晃'): #return lemma_ids=['080601',] or None
    cursor.execute('select lemma_id from cwn_lemma where lemma_type="%s"' % lemma_type)
    return cursor.fetchall()#[0]

def lemma_id_to_sense_ids(lemma_id='093020'): #return sense_id=['08060101',] or None
    cursor.execute('select sense_id from cwn_sense where lemma_id="%s"' % lemma_id)
    return cursor.fetchall()#[0]

def sense_id_to_sense_def(sense_id='08060101'): #return sense_def or None
    cursor.execute('select sense_def from cwn_sense where sense_id="%s"' % sense_id)
    return cursor.fetchone()#[0]

def cwn_id_to_example_cont(cwn_id='03000101'): #return example_cont or None
    cursor.execute('select example_cont from cwn_example where cwn_id="%s"' % cwn_id)
    return cursor.fetchone()#[0]

#conn.close()
