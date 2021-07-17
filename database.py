
import os
import json

class QuestionQueue(object):
    __queue = list()
    __filename = ""
    def __init__(self, filename):
        if os.path.exists(filename):
            with open(filename) as f:
                self.__queue = json.load(f)
        else:
            self.__queue = list()

        self.__filename = filename

    def enqueue(self, question:str):
        self.__queue.append(question)

    def dequeue(self):
        return self.__queue.pop(0)

    def save(self):
        with open(self.__filename, "w") as f:
            json.dump(self.__queue, f)

    def dump(self):
        return json.dumps(self.__queue)

    def get_list(self):
        return self.__queue


queue_template = """<html><body>
<h1>Radio School</h1>
<p>Current question queue:</p>
<ul>
{}
</ul>
</body>
</html>
"""

def HTML_queue(queue):
    q = queue.get_list()
    q = map(lambda x:"<li>" + str(x) + "</li>", q)
    string = "\n".join(q)
    return queue_template.format(string)
