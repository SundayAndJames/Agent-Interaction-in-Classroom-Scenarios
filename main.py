import openai
import random
import time


class ClassroomAgent:
    """基础课堂代理类，用于定义教师和学生的共同特性。"""

    def __init__(self, name, role, openai_key):
        self.name = name
        self.role = role
        self.openai_key = openai_key

    def speak(self, message):
        print(f"[{self.role} {self.name}]: {message}")


class Teacher(ClassroomAgent):
    """教师代理类，继承自ClassroomAgent。"""

    def ask_question(self, topic):
        # 使用OpenAI API生成问题
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Generate a question about the topic: {topic}",
            max_tokens=60,
            api_key=self.openai_key
        )
        question = response.choices[0].text.strip()
        self.speak(question)
        return question


class Student(ClassroomAgent):
    """学生代理类，继承自ClassroomAgent。"""

    def answer_question(self, question):
        # 使用OpenAI API自动生成回答
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Answer the following question: {question}",
            max_tokens=60,
            api_key=self.openai_key
        )
        answer = response.choices[0].text.strip()
        self.speak(answer)
        return answer


# 使用你的OpenAI API密钥
openai_api_key = "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"

# 创建课堂代理
teacher = Teacher("Smith", "Teacher", openai_api_key)
students = [Student("Alice", "Student", openai_api_key), Student("Bob", "Student", openai_api_key),
            Student("Charlie", "Student", openai_api_key)]

# 定义课程主题
course_topic = "The Solar System"

count = 0
# 模拟连续的课堂情境
for _ in range(15):  # 进行三轮提问和回答
    question = teacher.ask_question(course_topic)
    time.sleep(20)
    random.choice(students).answer_question(question)
    time.sleep(20)
