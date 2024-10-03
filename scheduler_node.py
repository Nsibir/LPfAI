#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import time

# Класс узла с планировщиком задач
class TaskSchedulerNode:
    def __init__(self):
        # Инициализация ROS-узла с именем 'task_scheduler_node'
        rospy.init_node('task_scheduler_node', anonymous=True)

        # Создаем объект публикации, который отправляет сообщения типа String в топик '/task_status'
        self.pub = rospy.Publisher('/task_status', String, queue_size=10)

        # Устанавливаем таймер, который будет запускать метод `execute_task` каждые 5 секунд
        self.timer = rospy.Timer(rospy.Duration(5), self.execute_task)

        # Выводим сообщение в лог о запуске узла
        rospy.loginfo("Task Scheduler Node started")

    # Метод, который будет вызываться по таймеру для выполнения задачи
    def execute_task(self, event):
        # Логируем информацию о запуске задачи
        rospy.loginfo("Executing scheduled task...")

        # Создаем сообщение типа String
        msg = String()

        # Записываем в сообщение текущее время выполнения задачи
        msg.data = "Task executed at: {}".format(time.strftime("%Y-%m-%d %H:%M:%S"))

        # Публикуем сообщение в топик '/task_status'
        self.pub.publish(msg)

# Основная точка входа в программу
if __name__ == '__main__':
    try:
        # Создаем экземпляр класса планировщика
        node = TaskSchedulerNode()

        # Запускаем бесконечный цикл ожидания событий (работа узла продолжается до завершения)
        rospy.spin()
    except rospy.ROSInterruptException:
        # Обрабатываем исключение в случае прерывания работы ROS (например, при завершении работы)
        pass
