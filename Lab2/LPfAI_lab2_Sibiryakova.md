<h1>Лабораторная работа №2</h1> 
Выполнила Сибирякова Надежда, группа НПИмд-01-24

<h2> Задание:</h2>

1. Установить ROS2 Humble
2. Изучить планировщик [Pyperplan](https://github.com/aibasel/pyperplan)
3. Построить модель среды с tb3 (4) с манипулятором, либо любой другой 
колесный робот с манипулятором ([мануал](https://emanual.robotis.com/docs/en/platform/turtlebot3/machine_learning/))
4. Создать ROS узел с планировщиком.

<h3>1. Установка ROS2 Humble</h3>
На windows Ros2 humble либо работает плохо, либо совсем не запускается,
 поэтому нужно работать на виртуальной машине на Ubuntu 22.04.
  Устанавливать буду на Orcle VirtualBox.

Для установки нужно скачать iso-образ с 
[официального сайта Ubuntu](https://releases.ubuntu.com/jammy/) 
(с графическим интерфейсом)  
![alt text](/Lab2/images/image-3.png)

**Установка Oracle VirtualBox**    
* На [официальном сайте](https://www.virtualbox.org/wiki/Downloads)
 скачиваем установщик для вашей ОС (в моем случае это Windows)
* Открываем загрузки и запускаем .exe файл   
![alt text](/Lab2/images/image-1.png)
* Установливаем VirtualBox

**Создание виртуальной машины**
* Открываем VirtualBox и создаем новую виртуальную машину  
![alt text](/Lab2/images/image-2.png)
* Придумываем имя машины, указываем папку для хранения  и указываем 
iso-образ и кликаем "Далее"  
![alt text](/Lab2/images/image-4.png)
* Придумываем имя пользоателя и пароль, кликаем "Далее"  
![alt text](/Lab2/images/image-5.png)
* Выделяем оперативную память (минимум 4Гб, чтобы все потом грузилось)
 и процессоры  
 ![alt text](/Lab2/images/image-6.png)
* Выделяем память для жесткого диска  
![alt text](/Lab2/images/image-7.png)
* Все проверяем и кликаем "Готово"  
![alt text](/Lab2/images/image-8.png)
* Ура, виртуальная машина создана!

**Установка Ubuntu**
* Запускаем виртуальную машину и ждем пока закончится автоматическая 
установка  
![alt text](/Lab2/images/image-9.png)
* Установка прошла, ОС готова к работе
* **ОЧЕНЬ ВАЖНО НЕ ОБНОВЛЯТЬ СИСТЕМУ ДО 24.04 ВЕРСИИ (иначе не будет работать)**

Теперь можно устанавливать ROS2 Humble 

**Установка ROS2 Humble**

На официальном сайте ROS2 Humble есть подробный [туториал](https://docs.ros.org/en/humble/Installation/Alternatives/Ubuntu-Development-Setup.html)
по установке на Ubuntu 22.04.

* Сначала нужно дать потзователю полные права. Для этого в терминале пишем ```su -```, 
эта команда позволяет пользователю войти в систему под другим именем,
 не завершая текущий сеанс. Далее вводим пароль, открываем редактор командой 
```visudo```. В открывшемся редакторе в разделе 
<span style="color:blue">#User privilege specification</span> прописываем  строчку 
```<имя пользоателя> ALL=(ALL:ALL) ALL```
  
![alt text](/Lab2/images/image-12.png)

Нажимаем Ctrl+O и enter. Теперь у посльзователя полные права. 

* Проверка и установка необходимых пакетов:
```
locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings
```
Команды:  
```locale``` регионалльные настройки  
```sudo``` позволяет выполнять другие команды с правами администратора  
```apt``` пакетный менеджер   


![alt text](/Lab2/images/image-11.png)

* Добавление репозитория ROS2  
Установка пакета для управления репозиториями и установка репозитория:
```
sudo apt install software-properties-common
sudo add-apt-repository universe
```
Добавлем ключ ROS 2 GPG (для проверки подлинности и целостности пакетов и 
репозиториев, связанных с ROS2):
```
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```
Добавляем репозиторий в список источников:
```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```
* Обновление списка пакетов и установка ROS2:
```
sudo apt update
sudo apt upgrade
```

* Установка полного рабочего стола ROS2:
```
sudo apt install ros-humble-desktop-full
```
* Установка базовых компонентов ROS2:
```
sudo apt install ros-humble-ros-base
sudo apt install ros-dev-tools
```
* Настройка окружения:
```
source /opt/ros/humble/setup.bash
```

<h3>2.  Планировщик Pyperplan</h3>

Установить Pyperplan можно через ```pip install```, для этого сначала установим pip.
```
apt install python3-pip
pip install pyperplan
```

<h3>3. TurtleBot3</h3>

Устанавливать TurtleBot3 я буду по [гайду](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/).

Для начала устанавливаем gazebo (для симуляции мира),
 cartographer (для картографирования) и navigation (для навигации роботов):
```
sudo apt install ros-humble-gazebo-*
sudo apt install ros-humble-cartographer
sudo apt install ros-humble-cartographer-ros
sudo apt install ros-humble-navigation2
sudo apt install ros-humble-nav2-bringup
```

**Установка пакетов для TurtleBot3**  
Установливаем пакеты TurtleBot3:
```
source ~/.bashrc
sudo apt install ros-humble-dynamixel-sdk
sudo apt install ros-humble-turtlebot3-msgs
sudo apt install ros-humble-turtlebot3
```
_.bashrc_ — это файл скрипта, который выполняется при входе пользователя в систему    
_ros-humble-dynamixel-sdk_ — предоставляет интерфейс для работы с приводами DYNAMIXEL   
_ros-humble-turtlebot3-msgs_ — для передачи сообщений   
_ros-humble-turtlebot3_ — включаем все необходимые компоненты для работы с работами turtlebot3


**Конфигурация среды**  
Установка среды ROS
```
echo 'export ROS_DOMAIN_ID=30 #TURTLEBOT3' >> ~/.bashrc
source ~/.bashrc

echo 'source ~/turtlebot3_ws/install/setup.bash' >> ~/.bashrc
source ~/.bashrc
```

**Тестовый запуск**   
Запускала по этому [гайду](https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/). 

Сначала переходим в папку ```/turtlebot3_ws/src/``` и клонируем репозироний с
 симулциями для turtlebot3 и выбираем нужную ветку.  
Далее переходим в папку ```turtlebot3_ws``` и запускаем сборку ( Параметр 
_--symlink-install_ указывает colcon использовать символические ссылки вместо
 копирования файлов из исходной директории в директорию установки.)

```
cd ~/turtlebot3_ws/src/
git clone -b humble-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
cd ~/turtlebot3_ws && colcon build --symlink-install
```
Указываем источник для gazebo, выгружаем модель робота (в моем случае это waffle) и загружаем мир.

```
source /usr/share/gazebo/setup.sh
export TURTLEBOT3_MODEL=waffle
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```  
![](/Lab2/images/image-13.png)

**Запуск TurtleBot3 с манипулятором**  
Чтобы добавить на робота манипулятор устанавливаем недостающие пакеты
```
sudo apt install ros-humble-ros2-control 
sudo apt install ros-humble-ros2-controllers 
sudo apt install ros-humble-gripper-controllers 
sudo apt install ros-humble-moveit
```
_ros-humble-ros2-control_ — для управления роботом  
_ros-humble-ros2-controllers_ — для управления контроллерами  
_ros-humble-gripper-controllers_ — для управления захватами (грипперами)  
_ros-humble-moveit_ — для планирования движений и манипуляций   


Далее повторяем процедуру тестового запуска, но загружаем 
turtlebot3_manipulation_bringup:
```
cd ~/turtlebot3_ws/src/

git clone -b humble-devel https://github.com/ROBOTIS-GIT/turtlebot3_manipulation.git

cd ~/turtlebot3_ws && colcon build --symlink-install

source /usr/share/gazebo/setup.sh
export TURTLEBOT3_MODEL=waffle
ros2 launch turtlebot3_manipulation_bringup gazebo.launch.py
```

![alt text](/Lab2/images/image-14.png)


<h3>4. Создание узла</h3>
Для создания узла нужно создать директорию, провести сборку, указать источник, 
и создать пакет.

```
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build
source ~/ros2_ws/install/setup.bash
echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python a_node
```

![alt text](/Lab2/images/image-15.png)
