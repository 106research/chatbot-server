#from chatbot import chatbot

def Chat_with_Bot(sentence_in, project):
    # project = chatbot.Chatbot()
    # project.main(['--modelTag', '1108', '--test', 'daemon'])
    # --modelTag    1108
    # --test        daemon
    answer = project.daemonPredict(sentence=sentence_in)
    # project.daemonClose()
    del project
    return answer



if __name__ == "__main__":
    print(Chat_with_Bot())