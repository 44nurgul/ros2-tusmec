#ROS2 Publisher Subscriber 

Bu ROS2 python paketi "Tusmec çalışıyor" mesajı yayınlayan bir talker ve onu dinleyen bir listener içerir.

#KULLANIM

'''bash
cd ~ros2_ws
colcon build --packages-select tusmec
source install setup.bash 

#Publisher
ros2 run tusmec talker

#Subscriber (başka bir terminalde)
ros2 run tusmec listener
