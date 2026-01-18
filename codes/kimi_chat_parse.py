from runtime import Args
from typings.kimi_chat_parser.kimi_chat_parser import Input, Output
import re
reUserQuestion = re.compile(r'^User:\s',re.MULTILINE)
reKimiAnswer = re.compile(r'Kimi:\s',re.MULTILINE)

"""
Each file needs to export a function named `handler`. This function is the entrance to the Tool.

Parameters:
args: parameters of the entry function.
args.input - input parameters, you can get test input value by args.input.xxx.
args.logger - logger instance used to print logs, injected by runtime.

Remember to fill in input/output in Metadata, it helps LLM to recognize and use tool.

Return:
The return data of the function, which should match the declared output parameters.
"""
def chunk_parse(chunk:str) -> dict:
    mo = reKimiAnswer.search(chunk)
    if mo is None:
        raise ValueError('Chat history does not contain any line starting with Kimi: ')
    question = chunk[:mo.start()]
    answer = chunk[mo.end():]
    return {'question':question,'answer':answer}

def handler(args: Args[Input])->Output:
    chat_history = args.input.kimi_chathistory
    q_re_iter = reUserQuestion.finditer(chat_history)
    all_q_starts = []
    all_q_ends = []
    for q in q_re_iter:
        all_q_starts.append(q.start())
        all_q_ends.append(q.end())
    if len(all_q_starts) == 0:
        raise ValueError('chat history does not contain any line starting with User: ')

    chunks = []
    for s,s_next in zip(all_q_ends,(all_q_starts[1:]+[None])):
        chunks.append(chat_history[s:s_next])
    chunks = [chunk_parse(c) for c in chunks]
    answers = [c['answer'] for c in chunks]
    questions = [c['question'] for c in chunks]
    
    return {"chunks": chunks,"questions":questions,"answers":answers}