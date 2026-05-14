conversation_store:dict[str,list[dict]] = {}

def add_message(conversation_id:str,role:str,content:str):
    if conversation_id not in conversation_store:
        conversation_store[conversation_id] = []
    conversation_store[conversation_id].append({"role":role,"content":content})
    
    conversation_store[conversation_id]=conversation_store[conversation_id][-20:]


def get_messages(conversation_id:str)->list[dict]:
    return conversation_store.get(conversation_id,[])

def clear_messages(conversation_id:str):
    conversation_store.pop(conversation_id,None)
    
